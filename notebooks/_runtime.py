"""Portable paths and explicit reuse of definitions shown in the notebooks."""
from pathlib import Path
import ast
import json
import linecache
import os
import shutil
import zipfile
import nbformat

ROOT=Path(__file__).resolve().parents[1]
WORK=ROOT/'.cache/experiment'
REUSABLE={'src-02-012','src-03-001','src-03-005','src-04-006',
          'src-04-008','src-04-010','src-05-001','src-06-001',
          'src-08-011','src-10-005','src-10-009','src-10-017'}

def repo_root():
    return ROOT

def initialize():
    for name in ['tables','state','models','predictions','figures','raw']:
        (WORK/name).mkdir(parents=True,exist_ok=True)
    for name in ['raw_selected_feed_inventory.json','experiment_config.json',
                 'main_preprocessing_state.json','lag_llama_checkpoint.json']:
        target=WORK/'state'/name
        if not target.exists():shutil.copy2(ROOT/'dataset/config'/name,target)
    # These are input-derived data, never training checkpoints or completion flags.
    for source in (ROOT/'dataset/derived').glob('*.parquet'):
        target=WORK/'tables'/source.name
        if not target.exists():shutil.copy2(source,target)
    for name in ['common_calendar_site_coverage.csv','split_summary.csv',
                 'rolling_origin_splits.csv','revised_split_target_counts.csv']:
        target=WORK/'tables'/name
        if not target.exists():shutil.copy2(ROOT/'artifacts'/name,target)
    raw=WORK/'raw'
    with zipfile.ZipFile(ROOT/'dataset/raw_meter_records.zip') as archive:
        for name in archive.namelist():
            target=raw/name
            if not target.resolve().is_relative_to(raw.resolve()):
                raise ValueError('Invalid meter archive path')
            if not target.exists():archive.extract(name,raw)
    manifest=WORK/'tables/raw_meter_manifest.csv'
    if not manifest.exists():
        import pandas as pd
        frame=pd.read_csv(ROOT/'artifacts/raw_meter_manifest.csv')
        frame['local_path']=[f'.cache/experiment/raw/{r.site}/{r.channel}.MYD' for r in frame.itertuples()]
        frame.to_csv(manifest,index=False)

def _catalog():
    result={}
    for path in sorted((ROOT/'notebooks').glob('*.ipynb')):
        for cell in nbformat.read(path,4).cells:
            if cell.cell_type=='code':result[cell.id]=(path,cell.source)
    return result

def reuse(cell_id,namespace,names=None):
    """Import only permitted setup blocks or explicitly named definitions."""
    path,source=_catalog()[cell_id]
    filename=str(path)+'#'+cell_id
    linecache.cache[filename]=(len(source),None,source.splitlines(True),filename)
    tree=ast.parse(source,filename)
    if names is not None:
        tree.body=[n for n in tree.body if isinstance(n,(ast.FunctionDef,ast.ClassDef)) and n.name in names]
        if {n.name for n in tree.body}!=set(names):raise ValueError(f'Missing definitions: {cell_id}: {names}')
    elif cell_id not in REUSABLE:
        raise ValueError(f'Experiment loops cannot be imported: {cell_id}')
    exec(compile(tree,filename,'exec'),namespace)

def source_document(prefix):
    """Current executable sources for data/code-dependent checkpoint keys."""
    cells={int(cid.rsplit('-',1)[1]):source for cid,(_,source) in _catalog().items()
           if cid.startswith('src-'+prefix+'-')}
    if not cells:raise ValueError(prefix)
    return nbformat.v4.new_notebook(cells=[nbformat.v4.new_code_cell(cells.get(i,'')) for i in range(max(cells)+1)])

def _fresh():
    return os.environ.get('IAGTPF_RESULTS','saved')=='fresh'

def result_tables():
    return WORK/'tables' if _fresh() else ROOT/'artifacts'

def result_state():
    return WORK/'state' if _fresh() else ROOT/'dataset/config'

def plot_data():
    return WORK/'tables/plot_data' if _fresh() else ROOT/'artifacts/plot_data'

def figure_stem(stem):
    mapping=json.loads((ROOT/'dataset/config/figure_names.json').read_text())
    return mapping.get(stem,stem.removeprefix('revision_'))
