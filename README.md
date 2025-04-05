**Diamond Price Prediction Using Flask**
=> A Flask-based web application that predicts price of the diamond using various parameters like carat, cut, clarity, depth.
**Project Overview**
This project is an end-to-end machine learning application where:
This Project contains two Pipelines:
1. Training Pipeleine
2. Prediction Pipeline.
   In training pipeline there major
    4 **Steps**
   a. Data Ingestion: Reading the data from the specific source.
   b. Data Transformation: The EDA steps like cleaning the data, finding outliers, Normalizing the data, Feature extraction and Feature engineering.
   c. Model Trainer: This application is trained by using the Linear Regression machine learning algorithm.
   d. Model Evaluation: To evaluate the model we use Lasso, Elastic net and Ridge model.

In prediction Pipleline:
I have created the frontend page hosted on the Web API flask, which takes the data and fetch the information from the backend and predicts .

1. A trained model predicts diabetes likelihood.

2. A Flask API serves the model for real-time predictions.

3. The app is deployed on the AWS Beanstalk.

**Project Structure**

Diamond-Price-Prediction-Flask/
│
├── app/                # Folder for Flask app and web files
│   ├── __init__.py
│   ├── routes.py
│   └── templates/
│       └── index.html
│
├── notebooks/          # Jupyter Notebooks for exploratory analysis and model training
│   ├── EDA.ipynb
│   └── ModelTraining.ipynb
│
├── data/               # Folder for raw and processed data
│   ├── raw/
│   └── processed/
│
├── artifacts/          # Folder to save models and other outputs
│   ├── model.pkl
│   ├── preprocessor.pkl
│
├── requirements.txt    # Python dependencies
├── app.py              # Flask application entry point
└── README.md           # Documentation

**Install Dependencies**
pip install -r requirements.txt
**Technologies Used**
Python

Flask

Scikit-learn

HTML, CSS (for UI)
**Run the Flask application**
python app.py

**Libraries Used **
Sci-kit learn, Seaborn, flask, OneHotEncoding, pandas, numpy, matplolib.

**How It Works**
The user enters their details like carat, depth clarity x,y,z dimensions of the diamond.

The Flask app processes the input and passes it to the trained model.

The model predicts the price.

The result is displayed on the UI.












