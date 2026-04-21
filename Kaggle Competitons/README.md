# 🧠 Kaggle ML Competition Notebooks
 
> A collection of machine learning projects developed for Kaggle competitions, covering Natural Language Processing and classification tasks. Each notebook is self-contained, well-documented, and built with a focus on clean preprocessing pipelines, feature engineering, and model interpretability.
 
---
 
## 📁 Projects Overview
 
| Notebook | Competition | Task Type | Key Techniques |
|---|---|---|---|
| `Spaceship_Titanic` | Spaceship Titanic | Binary Classification | Feature Engineering, Ensemble Models |
| `Titanic` | Titanic - ML from Disaster | Binary Classification | EDA, Feature Engineering, Classical ML |
 
---

## 🗂️ Notebooks
### 🚀 Spaceship Titanic
**Competition:** [Spaceship Titanic](https://www.kaggle.com/competitions/spaceship-titanic)
 
Predict which passengers were transported to an alternate dimension following a spacetime anomaly. A tabular classification problem with structured data, missing values, and rich feature engineering opportunities.
 
**Highlights:**
- In-depth exploratory data analysis (EDA) with visualizations
- Feature engineering from cabin codes, group IDs, and spending patterns
- Handling of missing values with domain-informed imputation strategies
- Ensemble approach combining XGBoost, LightGBM, and Random Forest
**Key Libraries:** `pandas`, `numpy`, `scikit-learn`, `xgboost`, `lightgbm`, `matplotlib`, `seaborn`
 
---

### 🚢 Titanic
**Competition:** [Titanic - Machine Learning from Disaster](https://www.kaggle.com/competitions/titanic)
 
The classic entry point to Kaggle. Predict survival on the Titanic using passenger data. Deceptively simple — the depth comes from thoughtful feature engineering and model tuning.
 
**Highlights:**
- Comprehensive EDA exploring survival rates by gender, class, age, and embarkation
- Feature engineering: title extraction from names, family size, fare binning
- Pipeline construction with imputation, encoding, and scaling
- Model comparison: Logistic Regression, Decision Tree, Random Forest, Gradient Boosting
**Key Libraries:** `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`
 
---

## 📊 Results
 
| Competition | Best Score | Metric |
|---|---|---|
| Spaceship Titanic | 0.80430 | Accuracy |
| Titanic | 0.66507 | Accuracy |
 
*Scores will be updated as notebooks are refined.*
 
---

## 👩‍💻 About
 
These notebooks are part of my machine learning portfolio, built while developing practical skills in data preprocessing, feature engineering, model selection, and evaluation. Each competition presented a unique problem structure that required a tailored approach rather than a one-size-fits-all solution.
 
If you find any of these useful or have suggestions, feel free to open an issue or reach out.
 
---


