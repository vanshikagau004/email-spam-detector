# 📧 Email Spam Detector using Machine Learning

## 📌 Project Overview

This project builds an **Email Spam Detection system** using **Machine Learning and Natural Language Processing (NLP)** techniques. The model analyzes email messages and classifies them into **Spam** or **Ham (Not Spam)**.

Spam emails often contain promotional content, scams, or unwanted advertisements. This project demonstrates how machine learning can automatically detect such messages by analyzing textual patterns.

The model uses **TF-IDF vectorization** to convert text into numerical features and applies the **Naive Bayes classification algorithm** to perform spam detection.

---

## 🎯 Objectives

* Detect spam messages automatically
* Apply Natural Language Processing techniques
* Train a machine learning model for text classification
* Evaluate model performance using multiple metrics
* Save the trained model for future predictions

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* NLTK
* Matplotlib
* Seaborn

---

## 📂 Project Structure

```
email_spam_detector/
│
├── dataset/
│   └── spam.csv
│
├── model/
│   ├── spam_model.pkl
│   └── vectorizer.pkl
│
├── notebook/
│   └── spam_detector.ipynb
│
└── README.md
```

---

## ⚙️ Project Workflow

### 1️⃣ Data Collection

The dataset contains labeled email messages categorized as:

* **Spam**
* **Ham (Not Spam)**

### 2️⃣ Data Cleaning

Unnecessary columns are removed and the dataset is structured with two main columns:

* `label`
* `message`

### 3️⃣ Text Preprocessing

The text data is processed using NLP techniques such as:

* Lowercase conversion
* Removing punctuation
* Removing stopwords
* Stemming words to their root form

### 4️⃣ Feature Extraction

Text data is converted into numerical form using **TF-IDF (Term Frequency – Inverse Document Frequency)** vectorization.

### 5️⃣ Train-Test Split

The dataset is divided into:

* **Training Data (80%)**
* **Testing Data (20%)**

### 6️⃣ Model Training

The model is trained using the **Multinomial Naive Bayes algorithm**, which is effective for text classification tasks.

### 7️⃣ Model Evaluation

The model is evaluated using:

* Accuracy Score
* Confusion Matrix
* Classification Report

### 8️⃣ Model Saving

The trained model and TF-IDF vectorizer are saved using **Pickle (.pkl)** files for future predictions.

---

## 📊 Model Performance

The model achieves high accuracy in detecting spam messages. Performance metrics include:

* Accuracy
* Precision
* Recall
* F1-Score

---

## 🧪 Example Prediction

Input Email:

```
Congratulations! You have won a free lottery ticket.
```

Model Output:

```
Spam Email
```

---

## 🚀 How to Run the Project

1. Clone the repository

```
git clone https://github.com/vanshikagau004/email-spam-detector.git
```

2. Navigate to the project folder

```
cd email-spam-detector
```

3. Install required libraries

```
pip install -r requirements.txt
```

4. Open the Jupyter Notebook

```
jupyter notebook
```

5. Run the notebook `spam_detector.ipynb`

---

## 📈 Future Improvements

The following improvements will be implemented in the next version of the project:

* Implement advanced **text preprocessing**

  * Lowercase conversion
  * Removing punctuation
  * Removing stopwords
  * Stemming or lemmatization
* Experiment with additional machine learning models
* Improve feature engineering
* Build a web interface for real-time spam detection
* Deploy the model as an interactive application


---

## 👩‍💻 Author

Vanshika Gautam

---

## ⭐ Acknowledgment

This project was created as part of a **Machine Learning and NLP learning project** to understand spam detection techniques.
