# Figure collection

The main folder contains the 18 updated figures and six supplementary figures, with numbering taken from the supplied response document. English filenames translate its captions. Image bytes are preserved.

| Number | Figure |
|---|---|
| 1 | [Causal measurement preparation and dataset construction for IA-GTPF](1_causal_measurement_preparation_and_dataset_construction_for_ia_gtpf.png) |
| 2 | [Architecture of the IA-GTPF hybrid ensemble](2_architecture_of_the_ia_gtpf_hybrid_ensemble.png) |
| 3 | [Temporal availability of required net-load measurement channels](3_temporal_availability_of_required_net_load_measurement_channels.png) |
| 4 | [Training net-load distribution and relationship with photovoltaic generation](4_training_net_load_distribution_and_relationship_with_photovoltaic_generation.png) |
| 5 | [Observation provenance and quality of causal forecasting inputs](5_observation_provenance_and_quality_of_causal_forecasting_inputs.png) |
| 6 | [Net-load changes and mean grid exchange by photovoltaic regime](6_net_load_changes_and_mean_grid_exchange_by_photovoltaic_regime.png) |
| 7 | [Training-period lag correlations of net load](7_training_period_lag_correlations_of_net_load.png) |
| 8 | [Training daily net-load profiles of the primary cohort](8_training_daily_net_load_profiles_of_the_primary_cohort.png) |
| 9 | [Common-calendar four-period partition of the nine-site cohort](9_common_calendar_four_period_partition_of_the_nine_site_cohort.png) |
| 10 | [Neighbor graph context and local net-load dynamics](10_neighbor_graph_context_and_local_net_load_dynamics.png) |
| 11 | [Normalized training graph weights without self-edges](11_normalized_training_graph_weights_without_self_edges.png) |
| 12 | [Measured and predicted net load for IA-GTPF and ExtraTrees](12_measured_and_predicted_net_load_for_ia_gtpf_and_extratrees.png) |
| 13 | [Empirical absolute-error distributions of the principal models](13_empirical_absolute_error_distributions_of_the_principal_models.png) |
| 14 | [Paired IA-GTPF ablation effects with uncertainty estimates](14_paired_ia_gtpf_ablation_effects_with_uncertainty_estimates.png) |
| 15 | [IA-GTPF forecasts and 90-percent intervals at two horizons](15_ia_gtpf_forecasts_and_90_percent_intervals_at_two_horizons.png) |
| 16 | [Principal models across five chronological validation origins](16_principal_models_across_five_chronological_validation_origins.png) |
| 17 | [Coverage and width of prediction intervals](17_coverage_and_width_of_prediction_intervals.png) |
| 18 | [Forecast errors under small-change and unavailable-input regimes](18_forecast_errors_under_small_change_and_unavailable_input_regimes.png) |
| S1 | [Paired MAE differences with daily and seven-day block confidence intervals](S1_paired_mae_differences_with_daily_and_seven_day_block_confidence_intervals.png) |
| S2 | [Error change after removing residual correction across temporal origins](S2_error_change_after_removing_residual_correction_across_temporal_origins.png) |
| S3 | [Training and validation curves of modern neural models](S3_training_and_validation_curves_of_modern_neural_models.png) |
| S4 | [Quantile errors of probabilistic models](S4_quantile_errors_of_probabilistic_models.png) |
| S5 | [Conditional IA-GTPF interval coverage and width by regime and building type](S5_conditional_ia_gtpf_interval_coverage_and_width_by_regime_and_building_type.png) |
| S6 | [Forecast accuracy of the principal models by building](S6_forecast_accuracy_of_the_principal_models_by_building.png) |

## Original figure versions

The [original](original/) folder preserves the embedded images from `technologies-4580715.docx`. These use an earlier data protocol and are not the source of the benchmark values in the repository README. That DOCX contains figures 1 and 3–18; no embedded Figure 2 was found, so no substitute was assigned that number.

| Number | Figure |
|---|---|
| 1 | [Overview of the interpolation-aware data preparation pipeline for IA-GTPF](original/1_overview_of_the_interpolation_aware_data_preparation_pipeline_for_ia_gtpf.png) |
| 3 | [Temporary coverage of smart-meter data for OPSD Household Data objects](original/3_temporary_coverage_of_smart_meter_data_for_opsd_household_data_objects.png) |
| 4 | [Net load distribution and connection of PV generation with power-like network exchange values](original/4_net_load_distribution_and_connection_of_pv_generation_with_power_like_network_exchange_values.png) |
| 5 | [Interpolation load by objects and average data quality by building type](original/5_interpolation_load_by_objects_and_average_data_quality_by_building_type.png) |
| 6 | [Distribution of net load ramp events and average net load under different PV modes](original/6_distribution_of_net_load_ramp_events_and_average_net_load_under_different_pv_modes.png) |
| 7 | [Diagnostics of lag correlation of net load by objects and time horizons](original/7_diagnostics_of_lag_correlation_of_net_load_by_objects_and_time_horizons.png) |
| 8 | [Daily profile of average net load by object type](original/8_daily_profile_of_average_net_load_by_object_type.png) |
| 9 | [Chronological partitioning of the simulation set into train, validation, and test](original/9_chronological_partitioning_of_the_simulation_set_into_train_validation_and_test.png) |
| 10 | [Graph context net load and the relationship of PV state with ramp dynamics](original/10_graph_context_net_load_and_the_relationship_of_pv_state_with_ramp_dynamics.png) |
| 11 | [Graph adjacency matrix between objects based on train-only similarity of net-load profiles](original/11_graph_adjacency_matrix_between_objects_based_on_train_only_similarity_of_net_load_profiles.png) |
| 12 | [Comparative performance of the evaluated forecasting models across point, relative, ramp, and probabilistic evaluation metrics](original/12_comparative_performance_of_the_evaluated_forecasting_models_across_point_relative_ramp_and_probabilistic_evaluation_metrics.png) |
| 13 | [Comparison of IA-GTPF with the best baseline model for MAE on 15- and 60-minute horizons](original/13_comparison_of_ia_gtpf_with_the_best_baseline_model_for_mae_on_15_and_60_minute_horizons.png) |
| 14 | [Ablation analysis of IA-GTPF by MAE at a 15-minute horizon](original/14_ablation_analysis_of_ia_gtpf_by_mae_at_a_15_minute_horizon.png) |
| 15 | [An example of a probabilistic IA-GTPF forecast with a calibrated 90% interval](original/15_an_example_of_a_probabilistic_ia_gtpf_forecast_with_a_calibrated_90_interval.png) |
| 16 | [Robustness of rolling-origin validation for IA-GTPF-lite and Temporal HGB](original/16_robustness_of_rolling_origin_validation_for_ia_gtpf_lite_and_temporal_hgb.png) |
| 17 | [Calibration of IA-GTPF probability intervals and ablation configurations](original/17_calibration_of_ia_gtpf_probability_intervals_and_ablation_configurations.png) |
| 18 | [Error profile of IA-GTPF and the best baseline model in normal and weak-signal modes](original/18_error_profile_of_ia_gtpf_and_the_best_baseline_model_in_normal_and_weak_signal_modes.png) |
