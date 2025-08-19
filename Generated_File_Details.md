These are the files that are created while execution of program and the explanation of why it was created and what it contains

1. **`disasters.parquet`**

   * Contains disaster event data (economic damages in USD, frequency, severity).
   * Used to compute *shock impact scores* and measure vulnerability to disasters.

2. **`econ_core.parquet`**

   * Core economic indicators (GDP, inflation, unemployment, debt-to-GDP, etc.).
   * Forms the backbone for modeling GDP growth and resilience.

3. **`exports_annual.parquet`**

   * Annual country-level export data.
   * Used to compute *trade dependency indices* and diversification metrics.

4. **`imports_annual.parquet`**

   * Annual import data.
   * Complements exports to calculate overall trade exposure.

5. **`population.parquet`**

   * Population statistics (total, urban share, growth).
   * Needed for per-capita indicators (e.g., disaster damage per capita, GDP per capita).

6. **`trade_annual.parquet`**

   * Trade flows dataset (who trades with whom, how much).
   * Used for *trade network analysis* and resilience metrics.

7. **`welfare.parquet`**

   * Social indicators: life expectancy, poverty rates, inequality, education.
   * Used for *social spending efficiency* and *poverty forecasting*.

8. **`tren_master.parquet`**

   * The **integrated dataset**: merges econ\_core, disasters, trade, welfare, etc.
   * Serves as the master table for analysis and modeling.

9. **`tren_master_fe.parquet`**

   * Same as above but with **feature engineering applied**:

     * `resilience_score` (via PCA),
     * `shock_impact_score`,
     * `spending_efficiency`, etc.
   * Ready for modeling.

10. **`country_vulnerabilities.csv`**

    * Extracted *top 3 vulnerabilities per country*.
    * Inputs to policy briefs + visualization.

11. **`lgb_gdp_growth_model.pkl`**

    * Trained LightGBM model for GDP growth forecasting.
    * Saved for reproducibility.

12. **`lgb_gdp_growth_quantiles.pkl`**

    * Quantile regression version of the LightGBM model.
    * Produces uncertainty bands (low, median, high GDP growth).

13. **`backtest_results.csv`**

    * Backtesting evaluation of the GDP model against historical data.
    * Shows accuracy, bias, and residuals.

14. **`forecast_baseline_2025_2030.parquet`**

    * Raw baseline GDP growth forecasts for each country, yearly (2025–2030).

15. **`tren_forecasts_2030_baseline.json`**

    * 2030 projections under **no policy change (baseline)**.

16. **`tren_forecasts_2030_social_spending.json`**

    * 2030 projections under **increased social spending** scenario.

17. **`tren_forecasts_2030_trade_diversification.json`**

    * 2030 projections under **trade diversification** policy.

18. **`tren_forecasts_2030_global_crisis.json`**

    * 2030 projections under **global crisis scenario** (shock/recession).

19. **`tren_forecasts_2030_all_scenarios.csv`**

    * Combined CSV of all scenarios for comparison.

20. **`tren_forecasts_2030_all_scenarios.json`**

    * Same as above in JSON format (structured for APIs/visualizations).

21. **`policy_briefs_summary.csv`**

    * Table with GDP forecast + vulnerabilities for each country (summary stats).

22. **`policy_briefs_summary.json`**

    * Same as above, JSON format.
    * Input to LLM policy recommendation step.

23. **`policy_brief_llm.json`**

    * Final policy briefs with **LLM-generated recommendations** tailored per country.
    * Merges forecasts + vulnerabilities + AI recommendations.

24. **`heatmap_gdp_growth_2025_2030.png`**

    * Heatmap of projected GDP growth by country/region over 2025–2030.
    * Used for quick visual insights.

 **Why they were created?**

* **Raw data (`*.parquet`)** → collected and cleaned.
* **Processed (`tren_master*`)** → combined + engineered features.
* **Models (`.pkl`)** → trained predictors for GDP forecasts.
* **Forecasts (`*.json/csv`)** → outputs under different scenarios.
* **Policy (`*.json/csv`)** → summaries and LLM-based recommendations.
* **Visualization (`.png`)** → communicate results.


