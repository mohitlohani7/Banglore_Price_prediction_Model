

# 🏡 Bangalore Housing Price Prediction  
> 📍 **Executed Entirely in Jupyter Notebook**

---

## 🎯 Objective
To develop a **machine learning model** using supervised learning that **predicts housing prices in Bangalore** based on features like:
- Location  
- Square Footage  
- BHK (Bedrooms)  
- Bathrooms  
- Area Type (e.g., Built-up)  
- Availability  

---

## 📒 Execution in Jupyter Notebook

### ✅ 1. **Data Preprocessing**
- Imported and cleaned dataset (13,000+ rows) from Kaggle.
- Handled missing values, removed outliers, and fixed inconsistent entries.
- Transformed categorical features using **LabelEncoder**.
- Engineered features like `price_per_sqft` for better model performance.

---

### 📊 2. **Exploratory Data Analysis (EDA)**
- Used **matplotlib** and **seaborn** for:
  - Location-based price visualization
  - Distribution of BHKs and bathrooms
  - Correlation heatmaps to detect key patterns

---

### 🤖 3. **Model Building and Evaluation**
Used `GridSearchCV` in Jupyter to test and tune the following models:
- ✅ **XGBoost Regressor** (Best Accuracy: **91.3%**)
- Linear Regression  
- Lasso Regression  
- Ridge Regression  
- Random Forest  

All models were evaluated using:
- Cross-validation (`ShuffleSplit`)
- Accuracy and best parameter reporting

---

### 💾 4. **Saving the Model**
- Final trained XGBoost model saved using `pickle`
- Exported label encodings for interface use in `.json` format

---

## 🌐 Deployment (Outside Jupyter)
- After model testing in Jupyter, integrated the model into a web app using **Streamlit**
- Deployed to the cloud at:  
  👉 [Live Demo](https://banglorepricepredictionmodel-6ywekmwevqmyk2yxdtr3ek.streamlit.app/)

---

## 📦 Tools & Tech Used
| Category       | Tools/Packages                 |
|----------------|--------------------------------|
| Notebook       | **Jupyter Notebook**           |
| ML Libraries   | scikit-learn, XGBoost, pandas  |
| Visualization  | matplotlib, seaborn            |
| Deployment     | Streamlit                      |
| Environment    | Conda (managed via `.yml` file)|
| Saving Model   | pickle, json                   |

---

## 🧪 Conda Environment Setup

```bash
conda create --name bhp_env python=3.9
conda activate bhp_env
pip install -r requirements.txt
```

Useful Conda commands used:
- `conda info --envs`
- `conda env export > environment.yml`
- `conda env remove -n bhp_env`

---

## 🧠 Final Summary

> 💻 **Core ML logic, training, and tuning were executed in Jupyter Notebook**.  
> 🌐 Streamlit used for building an interactive and professional UI.  
> 📈 XGBoost selected for final deployment with **91.3% model accuracy**.

