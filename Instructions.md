#  Instructions to Run the Project

This guide explains how to set up, run, and reproduce outputs for **DPL 2025**.

##  1. Source Code

* All source code is available in the GitHub repository under:

  ```
  /source_code/
  ├── 23R246_DPL_2025.ipynb   # Main Jupyter Notebook
  ├── 23R246_DPL_2025.py      # Python script version
  ```

You can choose to run either the `.ipynb` notebook (recommended in Google Colab) or the `.py` file (on local / server).


##  2. Input Data

* Input data and supporting files are stored in Google Drive.
* Access link is provided inside:

  ```
  DPL_2025/Drive_link.txt
  ```
* Open this link, download the entire folder **DPL 2025**, upload it to **your own Google Drive**, then mount it in Colab:

```python
from google.colab import drive
drive.mount('/content/drive')
```

Your project path will look like:

```
/content/drive/MyDrive/DPL 2025/
```


##  3. File Organization

Inside `DPL 2025/`, you will find:

* **Input files (keep these)**

  * `econ_core.parquet`, `population.parquet`, `trade_annual.parquet`, `welfare.parquet`, `disasters.parquet`, etc.

* **Artifacts / Outputs (you can delete or change directory)**

  * `policy_brief_llm.json`, `tren_forecasts_2030_all_scenarios.csv`, `heatmap_gdp_growth_2025_2030.png`, etc.

 You may **delete outputs** to re-generate fresh ones, or set a new output directory in code.

##  4. Running the Notebook

1. Open **`23R246_DPL_2025.ipynb`** in Google Colab.
2. Run cells step by step:

   * **Data Loading & Cleaning**
   * **Feature Engineering**
   * **Model Training & Forecasting**
   * **Scenario Forecasts (baseline, trade diversification, social spending, crisis)**
   * **Policy Brief Generation (LLM with HuggingFace API)**
   * **Visualization & Insights (heatmaps, trade networks, shock maps)**
3. Outputs will be saved inside:

   ```
   /content/drive/MyDrive/DPL 2025/artifacts/
   ```


##  5. Hugging Face API (LLM Policy Briefs)

* The code uses Hugging Face API for models like **Llama 3.1 8B Instruct**.
* Your token must be stored in environment variable:

```python
import os
os.environ["HF_TOKEN"] = "your_api_token_here"
```

* If you encounter an invalid token error:

  * Open file with link given in document :

    ```
    DPL_2025/additional_api.txt
    ```
  * Copy the spare API key, replace the one in code, and re-run.


##  6. Viewing Outputs

* **Forecasts** → `/artifacts/tren_forecasts_*.json` or `.csv`
* **Policy Briefs** → `/artifacts/policy_brief_llm.json`
* **Visuals** → `/artifacts/*.png`

You can open JSON/CSV files directly in Colab or download them locally for review.


## Summary

* Clone repo → Upload Drive folder → Mount Drive
* Run `.ipynb` notebook in Colab step by step
* Outputs appear in `/artifacts/`
* Use **spare API token** if HuggingFace request fails
