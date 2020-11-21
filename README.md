# Disaster-Response-ML-Pipeline

# Table of Contents<a name="Table of Contents"></a>

1. [Introduction](#introduction)
2. [File Descriptions](#files)
3. [Installation](#installation)
4. [Screenshots](#pictures)


# Introduction<a name="introduction"></a>
This Project is in collaboration with Figure Eight. The data contains pre-labelled tweet and messages from real-life disaster. The aim of the project is to build a Natural Language Processing tool that categorise messages.

# File Description<a name="files"></a>
The project contains the following parts:  
1. ETL Pipeline: process_data.py: reads in the data, cleans and stores it in a SQL database. The script merges the messages and categories datasets, splits the categories column into separate, clearly named columns, converts values to binary, and drops duplicates.
2. Dataset: disaster_categories.csv and disaster_messages.csv 
3. DisasterResponse.db: created database from transformed and cleaned data.
4. ML Model: train_classifier.py: includes the code necessary to load data, transform it using natural language processing, run a machine learning model using GridSearchCV, RandomForest and train it. 
5. Web App: run.py: Flask app and the user interface used to predict results and display them.


# Installation<a name="installation"></a>
Dependencies
* Python 3.5+ (I used Python 3.7)
* Machine Learning Libraries: NumPy, SciPy, Pandas, Sciki-Learn
* Natural Language Process Libraries: NLTK
* SQLlite Database Libraqries: SQLalchemy
* Web App and Data Visualization: Flask, Plotly

Installing
Clone this GIT repository:
git clone https://github.com/isakkabir/Disaster-Response-ML-Pipeline.git


Executing Program:
1. Run the following commands in the project's root directory to set up your database and model.
    * To run ETL pipeline that cleans data and stores in database python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db
    * To run ML pipeline that trains classifier and saves python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl
2. Run the following command in the app's directory to run your web app. python run.py 
3. Go to http://0.0.0.0:3001/ 


# Screenshots<a name="pictures"></a>
Below are a few screenshots of the web app.

After clicking **Classify Message**, you can see the categories which the message belongs to highlighted in green

![Sample Output](pictures/disaster-response-project1.png)

![Main Page](pictures/disaster-response-project2.png)

