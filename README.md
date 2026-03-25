# 📊 Marketing Sales Revenue Prediction System (KNN)

## 🚀 Project Overview
This project is an end-to-end Machine Learning system that predicts **Sales Revenue** using key business factors such as marketing spend, pricing strategies, and customer behavior.

It demonstrates a complete ML workflow — from **data preprocessing → model building → deployment** using Streamlit.

---

## 🎯 Objective
To build a predictive model that helps businesses understand how marketing efforts influence revenue generation and make better data-driven decisions.

---

## 🔧 Tech Stack
- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Streamlit  

---

## 📁 Dataset Description

### 📌 Train Dataset
Contains all input features along with the target variable:
- **sales_revenue (Target)**

### 📌 Test Dataset
Contains only input features (used for prediction)

### 🔑 Key Features
- region  
- channel  
- product_category  
- customer_segment  
- ad_spend  
- price  
- discount_rate  
- market_reach  
- impressions  
- click_through_rate  
- competition_index  
- seasonality_index  
- campaign_duration_days  
- customer_lifetime_value  

---

## ⚙️ Machine Learning Pipeline

### 1️⃣ Data Preprocessing
- Handled missing values  
- Converted date into **year, month, day**  
- Applied **One-Hot Encoding** for categorical variables  

### 2️⃣ Feature Scaling
- Used **StandardScaler** to normalize numerical data  
- Important for KNN (distance-based algorithm)

### 3️⃣ Model Building
- Implemented **K-Nearest Neighbors (KNN) Regression**
- Captures similarity between data points for prediction

### 4️⃣ Model Evaluation
- Mean Absolute Error (MAE)  
- Root Mean Squared Error (RMSE)  
- R² Score  

---

## 🧠 Intelligent Input Handling (Real-World Constraint)

### ❗ Problem
Many ML applications allow **any random input values**, which leads to:
- Unrealistic predictions  
- Poor model reliability  
- Misleading business insights  

---

### ✅ Solution Implemented
This system uses **data-driven input validation**, ensuring that user inputs stay within **realistic ranges derived from the training dataset**.

---

### 🔍 Example Constraints
- Ad Spend → Limited to dataset range  
- Price → Realistic pricing boundaries  
- Impressions → Cannot be zero or extremely low  
- CTR → Restricted within valid percentage range  
- Customer Lifetime Value → Based on business logic  

---

### 💡 Benefits
✔ Prevents unrealistic predictions  
✔ Improves model reliability  
✔ Ensures business relevance  
✔ Builds trust in ML outputs  

---

## ⚙️ Input Validation in Streamlit App

Before prediction, the system ensures:
- No critical values are zero  
- All inputs are within realistic dataset ranges  
- Proper categorical selections are made  

If invalid input is detected:
→ The app shows a warning instead of generating incorrect predictions  

---

## 🚀 Deployment

The model is deployed using **Streamlit**, providing an interactive interface where users can input marketing parameters and get real-time predictions.

🔗 **Live App**  
https://marketing-revenue-prediction-system-knn-5cfqxvvo9kvh2pwlfbdasl.streamlit.app/

---

## ⚠️ Challenges Faced

### 🔧 Dependency Conflict
- Faced issue: `Altair vs Streamlit version mismatch`  
- Result: Runtime errors during deployment  

### ✅ Solution
- Resolved by installing compatible package versions  
- Learned importance of environment management  

---

## 📈 Key Learnings

- Importance of **feature scaling in KNN**
- Handling categorical data using **One-Hot Encoding**
- Building complete ML pipelines  
- Real-world debugging and dependency resolution  
- Importance of **realistic input constraints in ML systems**
- Understanding **garbage-in → garbage-out problem**

---

## 🧠 Limitations

- KNN is sensitive to:
  - Irrelevant features  
  - Scaling issues  
- Performance may degrade with large datasets  

---

## 🚀 Future Improvements

- Replace KNN with advanced models:
  - Random Forest  
  - XGBoost  
- Add feature importance visualization  
- Improve prediction accuracy  
- Add dashboard analytics (Power BI / Streamlit)  
- Store predictions for analysis  

---

## 📂 Project Structure

Marketing-Revenue-Prediction-System-KNN/
│
│ ├── train.csv
│ ├── test.csv
│
│ ├── model.pkl
│ ├── scaler.pkl
│ ├── columns.pkl
│
│ ├── data_preprocessing.py
│ ├── model.py
│
├── app.py
├── requirements.txt
└── README.md
