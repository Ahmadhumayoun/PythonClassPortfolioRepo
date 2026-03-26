from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import csv
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

DATA_FILE = 'form_submissions.csv'

def init_csv():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['id', 'name', 'email', 'subject', 'message', 'timestamp'])

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/rock_paper_scissors.html')
def game():
    return send_from_directory('.', 'rock_paper_scissors.html')

@app.route('/chess.html')
def chess():
    return send_from_directory('.', 'chess.html')

@app.route('/vendor_data.html')
def vendor_data():
    return send_from_directory('.', 'vendor_data.html')

@app.route('/FinalItems.csv')
def csv_file():
    return send_from_directory('.', 'FinalItems.csv')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = request.get_json()
        
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        subject = data.get('subject', '').strip()
        message = data.get('message', '').strip()
        
        if not all([name, email, subject, message]):
            return jsonify({'success': False, 'message': 'All fields are required'}), 400
        
        row_id = 1
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as f:
                row_id = sum(1 for _ in f)
        
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        with open(DATA_FILE, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([row_id, name, email, subject, message, timestamp])
        
        return jsonify({'success': True, 'message': 'Message saved successfully!'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500

if __name__ == '__main__':
    init_csv()
    print(f"Server running at http://localhost:5000")
    print(f"Form submissions will be saved to: {os.path.abspath(DATA_FILE)}")
    app.run(debug=True, port=5000)
