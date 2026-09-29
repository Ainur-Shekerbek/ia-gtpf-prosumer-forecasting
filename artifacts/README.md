# Experimental tables

All CSV values are copied from the saved experiment. Units for MAE, RMSE and interval width are kW; R² and coverage are dimensionless. Five seeds apply to stochastic models, while deterministic baselines have a single run.

| Tables | Contents |
|---|---|
| `main_model_metrics.csv`, `final_main_model_comparison.csv` | Per-run final point errors and compact seed summaries |
| `probabilistic_metrics.csv`, `conditional_coverage_and_width.csv` | Interval coverage, width, scores and conditional calibration |
| `paired_statistical_summary.csv` | Paired MAE differences, block confidence intervals and adjusted tests |
| `rolling_origin_model_metrics.csv`, `repeated_ablation_metrics.csv` | Repeated temporal validation and component-removal experiments |
| `conditional_point_metrics.csv` | Site, building-type and regime-specific point errors |
| `measured_vs_interpolated_target_metrics.csv`, `pre_clip_vs_post_clip_metrics.csv` | Target provenance, raw-target and clipping sensitivity |
| `supplementary_public_*.csv` | Separately evaluated public-building cohorts |
| `foundation_*comparisons.csv`, `foundation_probabilistic_subset_metrics.csv` | Matched-subset foundation comparison |
| `runtime_complexity.csv` | Separate fitting, calibration, inference and memory measurements |
| `*_validation_*.csv`, `ia_gtpf_final_hyperparameters.csv` | Selected model settings and fitted configuration |
| `modern_training_curves.csv` | Neural training and validation losses by epoch |
| `split_summary.csv`, `rolling_origin_splits.csv`, `revised_split_target_counts.csv` | Chronological boundaries and eligible sample counts |
| `feature_dictionary.csv`, `common_calendar_site_coverage.csv`, `raw_meter_manifest.csv` | Feature meanings, site availability and original input identities |
| `publication_*.csv` | Compact result summaries, including counts and seed variability |
| `plot_data/` | The numeric inputs directly read by the figure cells |

`raw_meter_manifest.csv` retains source-workspace relative paths as provenance. The runtime utility maps these to the packaged raw-data directory. The figure command uses these saved tables; a full training run creates new working tables and figure inputs in `.cache/experiment/`.
