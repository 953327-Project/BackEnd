# Import necessary libraries
from flask import Flask, jsonify, make_response
import pandas as pd
from flask_cors import CORS
# Create a Flask app instance
app = Flask(__name__)
CORS(app)
csv_metrics_data = "../Material/api_lib_metrics.csv"
csv_scores_data = "../Material/score_metrics.csv"
df_metrics = pd.read_csv(csv_metrics_data)
df_scores = pd.read_csv(csv_scores_data)

# Endpoint for Metrics data to get sorted data for a specific topic
@app.route('/sortedMetrics/<topic>', methods=['GET'])
def get_sorted_Metrics_data(topic):
    if topic not in df_metrics.columns:
        return jsonify({"error": "Invalid topic"}), 400

    sorted_data = df_metrics[['project_name', topic]].sort_values(by=topic, ascending=False).to_dict('records')
    return jsonify(sorted_data)

# Endpoint for Scores data to get sorted data for a specific topic
@app.route('/sortedScores/<topic>', methods=['GET'])
def get_sorted_Scores_data(topic):
    if topic not in df_scores.columns:
        return jsonify({"error": "Invalid topic"}), 400

    sorted_data = df_scores[['project_name', topic]].sort_values(by=topic, ascending=False).to_dict('records')
    return jsonify(sorted_data)


@app.route('/get_csv_as_df', methods=['GET'])
def get_csv_as_df():
    # Convert CSV data to a DataFram
    df = pd.read_csv(csv_metrics_data)
    # Convert the DataFrame to JSON format
    json_data = df.to_json(orient='records')
    response = make_response(json_data)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    print(json_data)

    return response
@app.route('/get_score_csv', methods=['GET'])
def get_score_csv():
    # Convert CSV data to a DataFram
    df = pd.read_csv(csv_scores_data)
    # Convert the DataFrame to JSON format
    json_data = df.to_json(orient='records')
    response = make_response(json_data)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    print(json_data)

    return response

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000, debug=True)
