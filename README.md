# 🩺 Heart Disease Predictor

## Overview

This project is a comprehensive Machine Learning solution designed to predict the likelihood of heart disease in patients based on various clinical parameters. The solution encompasses the entire ML lifecycle, from initial data preprocessing and exploratory data analysis (EDA) to model training and final deployment as an interactive web application using **Streamlit**.

The prediction is performed using multiple classification algorithms, with the best-performing model being integrated into the Streamlit application for real-time inference.



---

## Features

* **Data Preprocessing:** Cleaning, handling missing values, encoding categorical features, and scaling numerical data, as seen in `Data Preprocessing Heart Dataset.ipynb`.
* **Exploratory Data Analysis (EDA):** Visualizing key relationships and distributions within the dataset (`Heart Data Visualization.ipynb`).
* **Model Training:** Training and evaluating multiple classification models, including Logistic Regression, Decision Tree, and Support Vector Machine (SVM) (`Model Training and pickleing.ipynb`).
* **Model Persistency:** Saving the trained models (`.pkl` files) for quick loading and deployment.
* **Web Deployment:** An easy-to-use **Streamlit** application (`app.py`) that allows users to input clinical features and receive an instant heart disease prediction.

---

## Technologies Used

The project is built entirely in Python and utilizes the following major libraries:

| Category | Library | Purpose |
| :--- | :--- | :--- |
| **Data Handling** | `Pandas`, `NumPy` | Data manipulation and numerical operations. |
| **Visualization** | `Matplotlib`, `Seaborn` | Data visualization and EDA. |
| **Machine Learning** | `Scikit-learn` | Model building, training, and evaluation. |
| **Deployment** | `Streamlit` | Creating the interactive web application. |
| **Model Saving** | `pickle` | Saving and loading the trained models. |

---

## Repository Structure

The key files and directories are organized as follows, reflecting the full project lifecycle:
├── Data Preprocessing Heart Dataset.ipynb # Initial data cleaning and preparation notebook. 
├── Heart Data Visualization.ipynb # Exploratory Data Analysis (EDA) notebook. 
├── Model Training and pickleing.ipynb # Notebook for training ML models and saving them. 
├── app.py # The main Streamlit web application script for deployment. 
├── cleaned.csv # The cleaned dataset used for model training. 
├── PredictionsData.csv # Data used for final prediction testing. 
├── DecisonTree1.pkl # Trained Decision Tree Classifier model. 
├── LogisticRegresion.pkl # Trained Logistic Regression model. 
├── SVm.pkl # Trained Support Vector Machine (SVM) model. 
├── README.md # The documentation file (this file). 
-------------------------------------------------------------------------------------------
## Application Screenshots / Dashboard

This section showcases the application's interface and the key visualizations used during the Exploratory Data Analysis (EDA).

### Streamlit Application Interface
(Paste the image files for your Streamlit app here. For example, if you place your screenshots in an `assets` folder, use this format:)

`![Streamlit Prediction Interface](assets/app_screenshot.png)`

### Key Data Visualizations
(Showcasing graphs from your `Heart Data Visualization.ipynb` notebook)

`![Age vs HeartDisease](assets/Age.png)`
`![Chest Pain Type vs Heart Disease](assets/chest_pain_plot.png)`
DatasetUsed:https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction
