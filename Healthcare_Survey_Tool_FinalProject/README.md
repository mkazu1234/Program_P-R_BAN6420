# Healthcare Income Spending Survey Application/Tool

## Project Overview
This project is a web-based survey tool intended to collect data on participants' income and spending patterns ahead of the introduction of a healthcare product. Python is used for data processing, Jupyter Notebook is used for data visualization, Flask is used for web development, and MongoDB is used for data storage. Elastic Beanstalk is used to install the web application on Amazon Web Services (AWS).

## Features
- **Web Development**: A simple webpage with a variety of categories (such as entertainment, school fees, utilities, and so on) that gathers user data such as age, gender, income, and expenses is created using Flask.
- **Data Storage**: A MongoDB database is used to store user data for future retrieval and analysis.
- **Data Processing**: To prepare the data collected for additional analysis, a custom Python class is used for processing and exporting to a CSV file.
- **Data Visualization**: To visualize the distribution of income by age and the distribution of spending by gender, Jupyter Notebooks are used to create the visualizations.
- **Deployment**: For convenience, AWS Elastic Beanstalk hosts the complete web application.

## Installation Instructions

### 1. Requirements

- **Python 3.8+**
- **Flask** (`pip install Flask`)
- **MongoDB** (Download and install from [MongoDB](https://www.mongodb.com/))
- **Pandas** (`pip install pandas`)
- **Matplotlib** (`pip install matplotlib`)
- **Seaborn** (`pip install seaborn`)
- **Jupyter Notebook** (`pip install jupyter`)
- **AWS CLI and Elastic Beanstalk CLI** (`pip install awsebcli`)

Directory Structure
/Healthcare_Survey_Tool_FinalProject     
    /templates           # HTML templates
        - survey.html
    /static              # Static files like CSS or images
        /charts          # Generated charts for visualization
    /application.py      # Main Flask application (app.py renamed to application.py for AWS Elastic Beanstalk hosting)
    /user_processing.py  # Data processing class
    /requirements.txt    # Dependencies
    /flask_suverytool    # Virtual Environment for testing
    /.ebextensions       # Elastic Beanstalk environment configuration
        - pythonconfig
    /README.md           # Project instructions
    /data_analysis.ipynb  # Jupyter Notebook for data visualization
    /flask_survey_tool_app # Zip files for AWS deloyment

### 2. Project Setup

1. Install project dependencies
bash
pip install -r requirements.txt

2. Ensure MongoDB is running locally
bash
mongod --dbpath "C:\Program Files\MongoDB\Server\7.0\data"

 Or 
Set MongoDB Atlas (Remote)
python -m pip install "pymongo[srv]==3.6"

mongodb+srv://Chimzor1234:Chimzor1234@datastar.tyfeg.mongodb.net/survey_db?retryWrites=true&w=majority&appName=DataStar

3. Run the Flask app locally
bash
python application.py

4. Access the web application at http://192.168.0.164:8080/

5. Data Processing and Analysis
Collected data export to CSV file
bash
python user_processing.py

Opening Jupyter Notebook and Analyzing the data
bash
jupyter notebook data_analysis.ipynb

Export the visualizations for use in presentations
Python
plt.savefig('age_vs_income.png')
plt.savefig('gender_distribution.png')

6. Deployment to AWS
Initialize AWS Elastic Beanstalk for the project
bash
eb init

Create and deploy the application
bash
eb create aws_flask-survey-env
eb deploy
eb open
eb status
eb logs

Also it can be hosted by uploading the flask_survey_tool_app zip file to the AWS Elastic Beanstalk console and accessed via th link (http://Flasksurveytool-env.eba-k2wfqvip.us-east-1.elasticbeanstalk.com)

Usage
Access the web form through the browser and submit survey data.
View the stored data in MongoDB compass.
Use the Python scripts to process and analyze the data, and visualize spending and income trends.
Export charts for client presentations.

Submissions - The files (application.py, survey.html, requirements.txt, user_processing.py, data_analysis.ipynb, CSV files, images, README.md) are uploaded to the GitHub repository  in a zipped folder " Healthcare_Survey_Tool_FinalProject.zip" 

GitHub Repository link - https://github.com/Chimzor/Payment_system
