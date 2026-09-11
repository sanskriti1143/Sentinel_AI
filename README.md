# 🛡️ Sentinel AI — Predictive Maintenance System

An end-to-end machine learning system that predicts machine failure risk, detects unusual machine behavior, and provides interpretable risk factors through an interactive web dashboard.

🔗 **Live Demo:** "https://sentinelai-mqw3hobu3cmuhcvqtryqcu.streamlit.app/"

---

## 📌 Overview

Unexpected machine failures can cause production downtime, maintenance costs, and equipment damage.

**Sentinel AI** uses machine sensor data to identify potential failures before they occur.

The system combines:

* Supervised machine failure prediction
* Imbalanced classification techniques
* Probability threshold optimization
* Unsupervised anomaly detection
* Explainable AI
* Interactive Streamlit dashboard
* Cloud deployment

---

## 🚀 Features

### 1. Failure Prediction

A machine-learning classification model predicts the probability of machine failure based on:

* Air temperature
* Process temperature
* Rotational speed
* Torque
* Tool wear
* Machine type

The system uses a tuned **Random Forest classifier**.

### 2. Imbalanced Data Handling

Machine failure is relatively rare compared with normal operation.

Instead of relying only on accuracy, the project evaluates:

* Precision
* Recall
* F1-score
* ROC-AUC
* PR-AUC
* Confusion matrix

A custom probability threshold was selected to improve failure detection.

### 3. Anomaly Detection

The system also uses **Isolation Forest** to detect unusual sensor behavior.

The anomaly detector produces:

* Anomaly prediction
* Anomaly score

This allows the system to identify unusual machine conditions even when a failure is not directly predicted.

### 4. Explainable AI

The system provides the **top risk factors** contributing to the machine's risk assessment.

Example:

```text
1. RPM
2. Process Temperature
3. Temperature
```

This makes the predictions easier to understand.

---

## 🧠 System Architecture

```text
                 Machine Sensor Inputs
                         │
                         ↓
                 Streamlit Dashboard
                         │
                         ↓
                  Sentinel Engine
                   ↙           ↘
          Failure Prediction   Anomaly Detection
                 │                    │
                 ↓                    ↓
          Failure Probability    Anomaly Score
                   \              /
                    \            /
                     ↓          ↓
                    Explainability
                         │
                         ↓
                   Final Analysis
```

---

## 📊 Machine Learning Approach

### Supervised Learning

**Random Forest Classifier**

Used for predicting machine failure probability.

The model was evaluated using metrics suitable for imbalanced classification rather than relying only on accuracy.

### Unsupervised Learning

**Isolation Forest**

Used to identify unusual machine operating conditions.

---

## 📈 Model Results

### Failure Prediction

Final evaluation using a tuned decision threshold:

| Metric    | Score |
| --------- | ----: |
| Precision | 0.757 |
| Recall    | 0.779 |
| F1-Score  | 0.768 |
| PR-AUC    | 0.788 |

Confusion Matrix:

```text
[[1915   17]
 [  15   53]]
```

The threshold was adjusted from the default 0.5 to approximately **0.3** to improve the detection of rare failure cases.

### Anomaly Detection

The Isolation Forest model was trained to distinguish normal machine behavior from anomalous operating conditions.

---

## 🛠️ Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* SHAP
* Streamlit
* Git
* GitHub

---

## 📂 Project Structure

```text
Sentinel_AI/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── models/
│   ├── failure_prediction_model.pkl
│   ├── best_threshold.pkl
│   ├── anomaly_detection_model.pkl
│   └── anomaly_scaler.pkl
│
└── src/
    ├── prediction.py
    ├── anomaly.py
    ├── explainability.py
    └── sentinel_engine.py
```

---

## ⚙️ How It Works

1. User enters machine sensor parameters.
2. The input is passed to the Sentinel AI engine.
3. The failure prediction model calculates failure probability.
4. The optimized threshold determines the risk category.
5. Isolation Forest checks for anomalous behavior.
6. The explainability module identifies important risk factors.
7. Results are displayed through the Streamlit dashboard.

---

## 💻 Run Locally

Clone the repository:

```bash
git clone https://github.com/sanskriti1143/Sentinel_AI.git
cd Sentinel_AI
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🌐 Deployment

The application is deployed using **Streamlit Community Cloud**.

The deployed application provides a public web interface where users can enter machine parameters and receive real-time predictions.

---

## 🎯 Project Goals

The goal of Sentinel AI is to demonstrate how multiple machine learning techniques can be combined into an end-to-end predictive maintenance application.

Rather than using a single classification model, the system combines:

**Failure Prediction + Anomaly Detection + Explainability**

to provide a more useful machine-health assessment.

---

## 🔮 Future Improvements

Possible future improvements include:

* Real-time sensor streaming
* Historical machine-health monitoring
* Maintenance recommendations
* Model monitoring and drift detection
* Automated model retraining
* REST API integration
* Containerized deployment

---

## 👩‍💻 Author

**Sanskriti**

B.Tech Computer Science En
