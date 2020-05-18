# Titanic Survival Prediction using Jupyter Notebooks

This repository contains a quite mature solution to predict survival on the titanic.
This is a challenge on Kaggle (https://www.kaggle.com/c/titanic) 
The solution contains code examples of custom plotly plots, scikit-learn pipelines, and model interpretation using shap.

## Technical Setup

This project can easily be reproduced in any Jupyter Notebook environment.

I extracted the conda environment I was working with for the project into the environment.yml file.
This file also contains some libraries that are not necessary to run this project.

For this project, the reelvant libraries are:
- scikit-learn=0.22.1
- numpy=1.18.1
- pandas=1.0.1
- seaborn=0.10.0
- matplotlib=3.1.3
- xgboost==1.0.2
- shap=0.35.0

## Contents

| File/folder | Description |
|-------------|-------------|
| `01_titanic_survival_prediction` | The Jupyter Notebook containing all the source code (including EDA, Model Training Pipelines, Model Explanation)
| `graph_utils.py` | Utility functions that include custom plotly plots
| `custom_transformer.py` | Examples to build custom scikit-learn estimators and transformers
| `environment.yml` | My extracted conda environment which I used to run the project
| `titanic.csv` | The dataset used to predict survival
| `proposal.docx` | This is the project proposal as this project was built within the scope of the Udacity Machine Learning Engineer Nanodegree
| `proposal.pdf` | The project proposal in pdf version
| `report.docx` | This is the project report as this project was built within the scope of the Udacity Machine Learning Engineer Nanodegree
| `report.pdf` | The project report in PDF Version
| `README.md` | This README file.