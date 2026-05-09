## 📩 NLP Spam Message Detector

### 📌 Project Overview

This project is based on Machine Learning and Natural Language Processing (NLP) to detect whether an SMS message is Spam or Normal Message.
The model analyzes SMS text using various NLP techniques like text preprocessing, tokenization, stopword removal, stemming, and CountVectorizer to accurately classify messages.

This project is beginner-friendly and demonstrates the complete workflow of a real-world NLP classification project using Python and Scikit-learn.


### 🚀 Features

-✅ SMS Spam Detection

-✅ NLP-based Text Preprocessing

-✅ CountVectorizer Implementation

-✅ Machine Learning Model Training

-✅ Real-time Message Prediction

-✅ Model Saving using Pickle

-✅ Clean and Simple Project Structure


### 🛠️ Tech Stack

Python

Pandas

NumPy

NLTK

Scikit-learn

Pickle

Jupyter Notebook

NLP (Natural Language Processing)


### 📊 Dataset

Dataset File: spam.csv

Contains SMS messages classified as:

Spam Message

Normal Message

Columns:

result

message


### ⚙️ NLP & Machine Learning Workflow

1️⃣ Data Loading

Dataset loaded using Pandas

2️⃣ Text Preprocessing

Performed NLP preprocessing techniques:

Lowercase Conversion

Tokenization

Removing Special Characters

Removing Stopwords

Stemming

3️⃣ Text Vectorization

Converted text into numerical format using:

CountVectorizer

4️⃣ Machine Learning Model

Model trained using Scikit-learn classification algorithms.

5️⃣ Model Saving

Saved:

Trained Model (spam_ham_project.pkl)

Count Vectorized File (vectorized.pkl)

using Pickle.

6️⃣ Prediction

Predicts whether a new SMS message is:

📩 Normal Message

🚨 Spam Message


### 📸 Screenshots

📊 Dataset Preview

![Dataset Preview](Screenshots/dataset.jpeg)

⚙️ NLP Preprocessing

![NLP Preprocessing](Screenshots/preprocessing.jpeg)

📈 Model Prediction

![Model Prediction](Screenshots/normal_msg.jpeg)

![Model Prediction](Screenshots/spam_msg.jpeg)


### ▶️How to Run

1️⃣ Clone the Repository

git clone https://github.com/kirtiisahu15/NLP-Spam-Message-Detector.git

2️⃣ Open Project Folder

cd NLP-Spam-Message-Detector

3️⃣ Install Dependencies

pip install pandas numpy nltk scikit-learn

4️⃣ Run the Notebook

jupyter notebook

Open:

spam_ham_project.ipynb


### 💡 Real World Use Case

This project can help:

Email & SMS Filtering Systems

Social Media Platforms

Cybersecurity Applications

Fraud & Scam Detection Systems

to automatically detect unwanted spam messages.


### ⚠️ Important Notes

Install all required libraries before running

Keep dataset file in the same folder

Download NLTK resources if required

Avoid uploading very large files to GitHub



### 🌟 Future Improvements

Deploy using Flask or Streamlit

Add Deep Learning Models

Improve Prediction Accuracy

Multi-language Spam Detection

Real-time Web Application


### 👩‍💻 Author

Kirti Sahu
