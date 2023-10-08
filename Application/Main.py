# Import necessary libraries
from flask import Flask, jsonify, make_response
import pandas as pd

# Create a Flask app instance
app = Flask(__name__)

# Sample CSV data (you can replace this with your own CSV file)
csv_data = "../Material/api_lib_metrics.csv"

# Define a route to return CSV data as a DataFrame in JSON
@app.route('/get_csv_as_df', methods=['GET'])
def get_csv_as_df():
    # Convert CSV data to a DataFram
    df = pd.read_csv(csv_data)
    # Convert the DataFrame to JSON format
    json_data = df.to_json(orient='records')
    response = make_response(json_data)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    print(json_data)

    return response

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
