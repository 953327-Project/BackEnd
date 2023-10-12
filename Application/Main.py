# Import necessary libraries
from flask import Flask, jsonify, make_response
import pandas as pd

# Create a Flask app instance
app = Flask(__name__)

csv_data = "../Material/api_lib_metrics.csv"
df = pd.read_csv(csv_data)

# Endpoint to get sorted data for a specific topic
@app.route('/sorted/<topic>', methods=['GET'])
def get_sorted_data(topic):
    if topic not in df.columns:
        return jsonify({"error": "Invalid topic"}), 400

    sorted_data = df[['project_name', topic]].sort_values(by=topic, ascending=False).to_dict('records')
    return jsonify(sorted_data)



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
