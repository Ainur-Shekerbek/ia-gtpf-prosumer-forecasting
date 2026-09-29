# Dataset

Source: Open Power System Data. 2020. Data Package Household Data. Version 2020-04-15. [Dataset landing page](https://data.open-power-system-data.org/household_data/2020-04-15/). Primary data: CoSSMic.

The supplied `datapackage.json` identifies the data license as [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/). Its original metadata and attribution are retained in `OPSD_README.md`.

| Input | Purpose |
|---|---|
| `raw_meter_records.zip` | Exactly 29 original binary `.MYD` streams; extracted locally to `.cache/experiment/raw/` |
| `household_data_15min_singleindex.csv.gz` | Losslessly compressed supplier CSV for calendar availability and secondary interpolation reference |
| `datapackage.json` | Original source schema, units and licensing metadata |
| `config/raw_selected_feed_inventory.json` | Selected stream identities, ZIP offsets, sizes and CRC values |
| `config/experiment_config.json` | Recorded cohort, calendar, seeds, horizons and preprocessing constants |
| `config/main_preprocessing_state.json` | Recorded train-fitted feature and graph state for figure reproduction |
| `derived/causal_base_panel.parquet` | Input-derived causally aligned measurement panel |
| `derived/modeling_dataset.parquet` | Input-derived features, splits, targets and target provenance |

The source ZIP is downloaded only if a required extracted stream is absent; the repository already includes all selected streams. Notebook 01 checks stream sizes and CRC values, and records their SHA-256 values for subsequent parsing. The derived panels can be rebuilt with `python run_pipeline.py prepare`.

Supplier-filled values do not enter the measured forecasting inputs. The supplier CSV is retained because it defines availability and supports the separate secondary reference, not because its regularized readings are treated as original measurements.
