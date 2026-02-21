# pishing_detection
This project implements a machine learning pipeline to classify emails as Phishing or Safe. It includes text preprocessing, feature extraction using TF-IDF, model training and evaluation, and a serialized model for inference. The goal is to demonstrate a reproducible end-to-end ML workflow, from data preparation to deployment-ready model artifacts.

# Phishing Email Detection using Machine Learning

## 📌 Project Overview

This project implements a machine learning pipeline to classify emails as **Phishing** or **Safe** using natural language processing techniques and supervised learning models.

The objective is to demonstrate a reproducible end-to-end ML workflow, including:

- Text preprocessing  
- Feature extraction with TF-IDF  
- Model training and evaluation  
- Model serialization for inference  

---

## 🧠 Problem Statement

Phishing emails represent a major cybersecurity threat. The goal of this project is to build a binary classification model capable of identifying whether an email is malicious (phishing) or legitimate (safe) based on its textual content.

---

## ⚙️ Methodology

### 1️⃣ Data Preprocessing

- Text cleaning (HTML removal, regex filtering)
- Tokenization
- Lemmatization / Stemming
- Stopword removal

### 2️⃣ Feature Engineering

- TF-IDF vectorization (`TfidfVectorizer`)
- N-gram representation (if applicable)

### 3️⃣ Models Evaluated

- Logistic Regression  
- Random Forest  
- MultinomialNB  

### 4️⃣ Model Selection

Models were evaluated using:

- Accuracy  
- Precision  
- Recall  
- F1-score  
- ROC-AUC  

The best-performing model was selected and saved as a serialized pipeline (`.pkl` file).

---

## 📊 Model Performance

> Replace with your real results.

| Metric    | Score |
|-----------|--------|
| Accuracy  | 0.96   |
| Precision | 0.95   |
| Recall    | 0.94   |
| F1 Score  | 0.95   |
| ROC-AUC   | 0.97   |

---

## 📂 Project Structure

phishing-detection/
│
├── notebooks/
│ └── training.ipynb
│
├── model/
│ └── phishing_model.pkl
│
├── src/
│ └── inference.py
│
├── requirements.txt
├── README.md
└── .gitignore
