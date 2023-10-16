# Churn-Prediction Web Application


This project focuses on customer churn prediction, a critical task for businesses aiming to retain existing customers and boost profitability. Using a real-world telecom customer dataset, we develop a robust churn prediction model. Our goal is to identify customers who are likely to churn, enabling proactive retention strategies.


## Project Overview

The project encompasses several key stages:

1. Importing Libraries:
In this initial step, we import essential Python libraries and modules required for data analysis, visualization, machine learning, and model evaluation. We also handle any potential warnings that might arise during code execution.

2. Loading Data:
We load the dataset, which contains information about telecom customers, into a Pandas DataFrame. This dataset forms the basis for building our churn prediction model.

3. Exploratory Data Analysis and Visualization:
Prior to preprocessing the data, we conduct exploratory data analysis (EDA) to gain insights into its characteristics. We examine for missing values and address any issues related to the "TotalCharges" column. Additionally, we create histograms to visualize the distribution of tenures and monthly charges for both churned and non-churned customers.

4. Data Preprocessing:
Data preprocessing is a pivotal step in preparing the data for machine learning. We define custom functions to handle categorical variables with binary values ("Yes" and "No"). Further, we establish pipelines for preprocessing different types of features, such as binary (yes/no), ordinal (gender), categorical (contract, payment method, internet service), and numeric (tenure, monthly charges, total charges) features. These pipelines are consolidated into a unified preprocessor pipeline.

5. Model Selection and Grid Search:
We implement a function to perform a grid search across a variety of machine learning models, aiming to discover the best hyperparameters. The models under consideration encompass Logistic Regression, Random Forest, XGBoost, CatBoost, and LightGBM. Multiple scoring metrics, such as recall, F1 score, and ROC AUC, are employed to assess model performance.

6. Evaluation and Comparison:
Model performance is evaluated on both training and test datasets, with metrics like accuracy, precision, recall, F1 score, and ROC AUC computed. We present a comparative analysis of these metrics across different models and scorers using visualizations.

7. Model Selection and Interpretation:
Following an in-depth evaluation, we opt for the CatBoostClassifier with optimized hyperparameters for ROC AUC as the final model. We provide insights into the rationale behind this selection.

8. Saving the Final Model:
The chosen CatBoostClassifier model is saved to a file, ensuring it can be readily employed for future use.


## Files in the Repository

1 - CatBoost_model.cbm: This is the trained churn classification model saved from the notebook, which is used in the web application.

2- app.py and utils.py: These two files contain the code for our simple web application.

3- preprocessor.pkl: This is the preprocessor used for training, which should also be used in our web application for data preprocessing.

4- requirements.txt: This file lists the libraries used in our virtual environment.

5- churn-prediction.ipynb the main code file.

6- Full_grid_result.pkl: This is the result of the grid search saved in a dictionary.

7- IT_customer_churn.csv: The dataset used in this project.



## To see this web application in action, please visit below web page:
https://churn-prediction-sgzsbmfsjduq4fdjwjcxdr.streamlit.app/
