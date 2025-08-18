import csv
from pymongo import MongoClient

class User:
    def __init__(self):
        # Connect to MongoDB
        self.client = MongoClient("mongodb+srv://Chimzor1234:Chimzor1234@datastar.tyfeg.mongodb.net/survey_db?retryWrites=true&w=majority&appName=DataStar")
        self.db = self.client['survey_db']
        self.collection = self.db['users']

    def export_to_csv(self, csv_file):
        users = self.collection.find()
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Age', 'Gender', 'Total Income', 'Utilities', 'Entertainment', 'School Fees', 'Shopping', 'Healthcare'])
            for user in users:
                # Extract each expense category, defaulting to '' if not present
                expenses = user.get('expenses', {})
                writer.writerow([
                    user.get('age', ''),
                    user.get('gender', ''),
                    user.get('total_income', ''),
                    expenses.get('utilities', ''),
                    expenses.get('entertainment', ''),
                    expenses.get('school_fees', ''),
                    expenses.get('shopping', ''),
                    expenses.get('healthcare', '')
                ])

# Usage
user_processor = User()
user_processor.export_to_csv('user_data.csv')


