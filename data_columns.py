# columns.py
import json

def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in: {file_path}")
        return None

file_path = './data/columns.json'
data = read_json_file(file_path)

def childhood():
    return data['childhood_columns']

def demographic():
    return data ['demographic_columns']

def diagnosis():
    return data['diagnosis_columns']

def all():
    return childhood() + demographic() + diagnosis()

def numeric_col():
    return data['demographic_numerical_col'] + data['childhood_numerical_col']