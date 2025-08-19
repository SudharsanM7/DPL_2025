# Instructions to run the Program is Given in Instructions.md

# Model Development & Training

## 1. Data Split

* We used an **80/20 split**:

  * **Training set (80%)** for fitting the models.
  * **Testing set (20%)** for final evaluation.
* For robustness, we also applied **5-fold cross-validation** on the training set to reduce overfitting and ensure stability of results.

## 2. Preprocessing

We applied the following preprocessing pipeline before modeling:

1. **Data Cleaning**

   * Handled missing values using column medians (for numeric data).
   * Removed duplicate rows.
   * Clipped extreme outliers for GDP growth, unemployment, and disaster damages (Winsorization at 1st and 99th percentiles).

2. **Feature Engineering**

   * **Resilience Score** → built from trade concentration, unemployment, disasters, and structural indicators (via PCA).
   * **Shock Impact Score** → computed from GDP growth drop after severe disaster years.
   * **Spending Efficiency** → derived from changes in government spending vs welfare (life expectancy).
   * Normalized all derived scores to **0–100 range**.

3. **Scaling**

   * Standardized numeric features with StandardScaler.
   * Applied one-hot encoding for categorical features (if present).

## 3. Model Architecture

We used a **stack of models** depending on the target:

* **GDP Growth Forecasting (Regression)**

  * Gradient Boosting Regressor (XGBoost)
  * Linear Regression (baseline)

* **Shock & Resilience Prediction (Classification / Scoring)**

  * Random Forest Classifier
  * Logistic Regression (baseline)

* **Scenario Modeling**

  * Baseline (no policy change) → trained on historical trends only.
  * Increased social spending → simulated by adjusting fiscal/spending features.
  * Trade diversification → simulated by reducing HHI / dependency scores.
  * Global crisis scenario → applied stress-tests by adding shocks to GDP and disaster variables.


## 4. Hyperparameter Tuning

We tuned models using **RandomizedSearchCV** + cross-validation.

### Example: XGBoost (GDP Growth Forecasting)

* n_estimators: 500
* max_depth: 6
* learning_rate: 0.05
* subsample: 0.8
* colsample_bytree: 0.8
* Final RMSE improved by \~15% compared to default settings.

### Example: Random Forest (Shock Impact Classification)

* n_estimators: 300
* max_depth: 10
* min_samples_split: 5
* Final accuracy: \~0.81 on validation.


## 5. Final Notes

* All models were **trained reproducibly** with fixed random seeds.
* Metrics reported: **RMSE (regression)**, **Accuracy/F1 (classification)**, and scenario-based comparative analysis.
* Outputs are stored in JSON + parquet format for easy visualization and policy brief generation.
