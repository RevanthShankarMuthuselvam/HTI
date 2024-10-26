from flask import Flask, jsonify, request
import pandas as pd
import json

# Open and read the JSON file
with open('config.json', 'r') as file:
    config = json.load(file)

app = Flask(__name__)   


# Route 1: GET method to retrieve the message
@app.route('/message', methods=['GET'])
def get_message():# Create a DataFrame from the input data
    df = pd.read_csv(config['path'])

    # Convert the Timestamp to datetime
    df['Timestamp'] = pd.to_datetime(df['timestamp'], format='%d.%m.%YT%H:%MZ')

    # Extract date and hour from the timestamp
    df['Date'] = df['Timestamp'].dt.date
    df['Hour'] = df['Timestamp'].dt.hour

    # Group by Car, Date, and Hour, and calculate the average speed
    hourly_avg = df.groupby(['id', 'Date', 'Hour'])['speed'].mean().reset_index()

    # Transform the DataFrame into a nested dictionary for JSON format
    result = {}
    for _, row in hourly_avg.iterrows():
        car = row['id']
        date = str(row['Date'])
        hour = row['Hour']
        avg_speed = row['speed']
        
        if car not in result:
            result[car] = {}
        if date not in result[car]:
            result[car][date] = {}
        result[car][date][hour] = avg_speed
        
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
