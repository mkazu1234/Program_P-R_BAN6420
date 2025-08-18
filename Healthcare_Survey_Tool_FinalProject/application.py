from flask import Flask, render_template, request
from pymongo import MongoClient
import os

application = Flask(__name__)

# Get MongoDB URI from environment variables
mongo_uri = os.environ.get('MONGO_URI', 'mongodb+srv://Chimzor1234:Chimzor1234@datastar.tyfeg.mongodb.net/survey_db?retryWrites=true&w=majority&appName=DataStar')
# Debugging print to confirm what URI is being used
print("MongoDB URI in use:", mongo_uri)
client = MongoClient(mongo_uri)
db = client['survey_db']
collection = db['users']

@application.route('/')
def survey():
    return render_template('survey.html')

@application.route('/submit', methods=['POST'])
def submit():
    print(request.form)  # Debugging line to see the form data
    
    try:
        # Retrieve form data
        age = request.form.get('age', type=int)
        gender = request.form.get('gender')
        total_income = request.form.get('total_income', type=float)

        # Collect expenses with default values if not provided
        expenses = {}
        expenses['utilities'] = convert_to_float(request.form.get('utilities'))
        expenses['entertainment'] = convert_to_float(request.form.get('entertainment'))
        expenses['school_fees'] = convert_to_float(request.form.get('school_fees'))
        expenses['shopping'] = convert_to_float(request.form.get('shopping'))
        expenses['healthcare'] = convert_to_float(request.form.get('healthcare'))

        # Check if checkbox is selected, otherwise do not include the category
        if not request.form.get('include_utilities'):
            expenses.pop('utilities', None)
        if not request.form.get('include_entertainment'):
            expenses.pop('entertainment', None)
        if not request.form.get('include_school_fees'):
            expenses.pop('school_fees', None)
        if not request.form.get('include_shopping'):
            expenses.pop('shopping', None)
        if not request.form.get('include_healthcare'):
            expenses.pop('healthcare', None)

        # Store data in MongoDB
        user_data = {
            "age": age,
            "gender": gender,
            "total_income": total_income,
            "expenses": expenses
        }
        collection.insert_one(user_data)
        
        return "Data submitted successfully!"
    
    except Exception as e:
        print(f"Error: {e}")
        return f"An error occurred: {e}", 500

def convert_to_float(value):
    """Convert the input to a float, defaulting to 0.0 if conversion fails."""
    try:
        return float(value) if value else 0.0
    except ValueError:
        return 0.0





