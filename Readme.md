# 📩 SMS Delivery Failure Prediction System

## 🚀 1. Project Overview

This project aims to predict the probability of SMS delivery success using machine learning. SMS platforms often face delivery failures due to multiple factors such as operator filtering, spam detection, routing issues, and user preferences (e.g., DND).
This is one of the binary classification problem of machine learning, where we need to classify the data into 0 or 1, delivered or failed 
The goal of this system is to:

* Predict whether an SMS will be **delivered or failed**
* Provide **probability of success**
* Help optimize SMS campaigns and routing strategies

An interactive **Streamlit application** is also built to allow real-time predictions.

---

## ⚙️ 2. How to Run the Project

### 🔹 Step 1: Clone the Repository


git clone https://github.com/ChirayuSolanki/SMS-classification.git

cd SMS-classification


### 🔹 Step 2: Install Dependencies

create virtual env - python -m venv venv

Initiate it - venv/Scripts/activate

install - pip install -r requirements.txt


### 🔹 Step 3: Run the Streamlit App


streamlit run app.py


### 🔹 Step 4: Use the App

* Enter SMS message OR select message length
* Fill other parameters (country, operator, etc.)
* Click **Predict** to get delivery probability

---

## 🧠 3. Approach

### 🏗️ Data Preparation
* Since we do not have any data, we would required some data to traing the model for this we generated synthetic dataset (1000 rows) based on realistic SMS delivery patterns
* Applied:

  * One-hot encoding for categorical variables
  * Train-test split with stratification

---

### 📊 Data Understanding
* Before building the model it is very important to understand the data we are building model on for this we have various techniques some of them are: 
* Explored feature impact using:

  * GroupBy analysis
  * Binning for numerical features
* After which we need to find which feature are in correlation with the target feature for this we Identified key influencing features like:

  * `historical_delivery_rate`
  * `previous_failures`
  * `campaign_type`

---



### Data Pre-processing
    * Checked for null and duplicates value. Since the data is synthetic data we dont have any null or duplicates value.

### 🤖 Model Selection

Here we have Tested multiple models on our data to find out which model is performing best on our data:

* Logistic Regression (baseline)
* Random Forest (best performer)
* XGBoost (boosting model)

👉 Final model selected: **Random Forest**

* Accuracy: ~72%
* Balanced precision and recall

---

### 📈 Evaluation Metrics

* Precision
* Recall
* F1-score
* Accuracy

---

### 🖥️ Deployment

* Model saved using `joblib`
* using **Streamlit** to build UI
* Supports:

  * Text-based message input
  * Manual feature selection
  * Real-time prediction

---

## ⚠️ 4. Exceptions & Limitations

* Dataset is **synthetically generated**, not real production data
* Feature relationships may not fully represent real telecom systems
* Model performance depends heavily on data quality
* Long or unrealistic message inputs may not reflect real SMS behavior
* (imp) The performace of model will not be good because of the data as well as hardware requirenments and time constrainsts.
---


## 🔥 Future Improvements

* Use real-world SMS logs for better accuracy
* Do multiple things on feature engineering part.
* Deploy as API using FastAPI, making it scalable, also we can build CI/CD pipelines
* Enhance UI with analytics dashboard

---

## 🧑‍💻 Author

**Chirayu Solanki**
AI/ML Engineer

---

## 📌 Conclusion

This project demonstrates an end-to-end ML pipeline:

* Data analysis → Feature engineering → Model building → Deployment

It showcases practical understanding of:

* Machine learning concepts
* Model evaluation
* Real-world system design

---
