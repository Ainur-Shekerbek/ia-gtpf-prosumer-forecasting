"""Build figure inputs from a newly completed local experiment."""
from pathlib import Path
import shutil
import numpy as np
import pandas as pd

ROOT=Path(__file__).resolve().parent
TABLE=ROOT/'.cache/experiment/tables'
PRED=ROOT/'.cache/experiment/predictions'
OUT=TABLE/'plot_data'

def refresh():
    OUT.mkdir(exist_ok=True)
    def write(frame,stem,index=True):frame.to_csv(OUT/f'revision_{stem}.csv',index=index)
    panel=pd.read_parquet(TABLE/'modeling_dataset.parquet')
    train=panel.loc[panel.split.eq('train')]
    write(train[['net_load_kw','pv_power_kw']].dropna(),'net_load_distribution_pv')
    cols=['net_load_kw','graph_neighbor_net_load_kw','pv_power_kw','net_load_ramp_kw']
    write(train[cols].dropna(),'graph_context_relationships')
    rows=[]
    for site,g in train.groupby('site'):
        for lag,label in [(1,'15 min'),(4,'60 min'),(96,'24 h')]:
            pair=g[['net_load_kw',f'lag_{lag}_net_load_kw']].dropna()
            rows.append({'site':site,'lag':label,'correlation':pair.iloc[:,0].corr(pair.iloc[:,1]),'n_pairs':len(pair)})
    write(pd.DataFrame(rows),'lag_correlation_matrix')
    write(train.groupby(['building_type','hour']).net_load_kw.agg(['mean','count']).reset_index(),'daily_load_profiles')
    metrics=pd.read_csv(TABLE/'main_model_metrics.csv').query('reference=="measured"')
    summary=metrics.groupby(['model','horizon_minutes']).agg(MAE_mean=('MAE','mean'),MAE_std=('MAE','std'),RMSE_mean=('RMSE','mean'),R2_mean=('R2','mean'),runs=('MAE','size'),n=('n','min')).reset_index()
    summary.to_csv(TABLE/'final_main_model_comparison.csv',index=False)
    rolling=pd.read_csv(TABLE/'rolling_origin_model_metrics.csv').query('reference=="measured"')
    write(rolling.groupby(['model','horizon_minutes','origin'])[['MAE','RMSE','R2']].mean().reset_index(),'rolling_origins')
    ablation=pd.read_csv(TABLE/'repeated_ablation_metrics.csv').query('reference=="measured"')
    res=ablation.loc[ablation.model.isin(['IA-GTPF','IA-GTPF without residual'])].groupby(['origin','horizon_minutes','model']).MAE.mean().unstack()
    res['without_minus_full']=res['IA-GTPF without residual']-res['IA-GTPF']
    write(res,'residual_branch_effect')
    probability=pd.read_csv(TABLE/'probabilistic_metrics.csv')
    write(probability.groupby(['model','horizon_minutes','method'])[['coverage','width','calibration_error','interval_score']].mean().reset_index(),'coverage_width')
    quantiles=probability.loc[probability.method.eq('native_interval')|probability.method.isin(['raw_quantiles_pre_clip','dedicated_conformal_pre_clip'])].copy()
    quantiles['label']=quantiles.model
    quantiles.loc[quantiles.method.eq('raw_quantiles_pre_clip'),'label']='IA raw'
    quantiles.loc[quantiles.method.eq('dedicated_conformal_pre_clip'),'label']='IA conformal'
    write(quantiles.groupby(['horizon_minutes','label'])[['pinball_0.05','pinball_0.5','pinball_0.95']].mean(),'pinball_loss_by_quantile')
    conditional=pd.read_csv(TABLE/'conditional_coverage_and_width.csv',dtype={'value':str})
    conditional=conditional.loc[conditional.model.eq('IA-GTPF')&conditional.method.eq('dedicated_conformal_post_clip')].copy()
    labels={'high_interpolation_regime':'Input unavailable','pv_regime':'PV regime','target_provenance':'Target','building_type':'Type','weak_signal_regime':'Weak signal'}
    conditional=conditional.loc[conditional.condition.isin(labels)]
    conditional['regime']=conditional.condition.map(labels)+': '+conditional.value.replace({'supplier_interpolated':'supplier marked'})
    write(conditional.groupby(['regime','horizon_minutes'])[['coverage','width','n']].mean(),'conditional_interval_matrices')
    points=pd.read_csv(TABLE/'conditional_point_metrics.csv',dtype={'value':str})
    points=points.loc[points.benchmark_partition.eq('full_test')]
    buildings=points.loc[points.condition.eq('site')&points.model.isin(['ExtraTrees','QuantileForest','IA-GTPF','STGCN'])]
    write(buildings.groupby(['value','model','horizon_minutes'])[['MAE']].mean(),'building_error_heatmaps')
    regimes=points.loc[points.condition.isin(['weak_signal_regime','high_interpolation_regime'])&points.model.isin(['ExtraTrees','IA-GTPF'])]
    write(regimes.groupby(['condition','value','model','horizon_minutes']).MAE.mean().reset_index(),'weak_signal_missing_input_performance')
    predictions=[];errors=[];examples=[]
    for h in [1,4]:
        for model in ['Persistence','ExtraTrees','QuantileForest','IA-GTPF']:
            seed=0 if model=='Persistence' else 11
            data=pd.read_parquet(PRED/f'origin_0_h{h}_seed{seed}_{model}_test.parquet')
            measured=data.loc[data.target_measured].copy()
            error=np.sort((measured.actual-measured.pred).abs().to_numpy())
            errors.append(pd.DataFrame({'model':model,'horizon_minutes':15*h,'absolute_error_kw':error,'empirical_cdf':np.arange(1,len(error)+1)/len(error)}))
            if model in ['ExtraTrees','IA-GTPF']:
                predictions.append(measured[['actual','pred','site','timestamp']].assign(model=model,horizon_minutes=15*h))
            if model=='IA-GTPF':
                site=sorted(data.site.unique())[0];example=data.loc[data.site.eq(site)].copy()
                example['timestamp']=pd.to_datetime(example.timestamp,utc=True)
                examples.append(example.loc[example.timestamp.lt(example.timestamp.min()+pd.Timedelta(days=7))])
    write(pd.concat(predictions,ignore_index=True),'prediction_quality')
    write(pd.concat(errors,ignore_index=True),'absolute_error_distribution')
    write(pd.concat(examples,ignore_index=True),'forecast_intervals_example')
    # The architecture diagram's labels are configuration descriptions, not scores.
    shutil.copy2(ROOT/'artifacts/plot_data/revision_actual_ia_gtpf_architecture.csv',OUT/'revision_actual_ia_gtpf_architecture.csv')

if __name__=='__main__':refresh()
