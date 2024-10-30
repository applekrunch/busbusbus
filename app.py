from flask import Flask, jsonify, request
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
EXTERNAL_API_URL = "https://datamall2.mytransport.sg/ltaodataservice/v3/BusArrival"

payload = {}
headers = {
  'AccountKey': API_KEY
}



# Replace with your actual external API URL
# EXTERNAL_API_URL = 'https://jsonplaceholder.typicode.com/posts'

@app.route('/api/posts', methods=['GET'])
def get_posts():
    response = requests.request("GET", EXTERNAL_API_URL, headers=headers, data=payload)
    print(response.text)
    
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({"error": "Failed to fetch posts from external API"}), response.status_code

@app.route('/api/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    # response = requests.get(f'{EXTERNAL_API_URL}?BusStopCode={post_id}')
    response = requests.request("GET", f'{EXTERNAL_API_URL}?BusStopCode={post_id}', headers=headers, data=payload)
    print(response.text)
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({"error": "Post not found"}), 404

@app.route('/api/posts', methods=['POST'])
def create_post():
    new_post_data = request.get_json()
    response = requests.post(EXTERNAL_API_URL, json=new_post_data)

    if response.status_code == 201:
        return jsonify(response.json()), 201
    else:
        return jsonify({"error": "Failed to create post"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
