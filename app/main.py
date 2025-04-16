from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)
app.json.sort_keys = False

@app.route('/')
def time_servce():
    return jsonify({
        "timestamp": datetime.now(),
        "ip": request.remote_addr
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)