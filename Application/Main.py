# Import necessary libraries
from flask import Flask, jsonify
import pandas as pd

# Create a Flask app instance
app = Flask(__name__)

# Sample CSV data (you can replace this with your own CSV file)
csv_data = "/Users/fallingrain/Workfouryear/project metric/BackEnd/Material/api_lib_metrics.csv"

# Define a route to return CSV data as a DataFrame in JSON
@app.route('/get_csv_as_df')
def get_csv_as_df():
    # Convert CSV data to a DataFram
    df = pd.read_csv(csv_data)

    # Convert the DataFrame to JSON format
    json_data = df.to_json(orient='records')

    print(json_data)

    return jsonify(json_data)

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
