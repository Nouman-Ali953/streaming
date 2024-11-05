from flask import Flask, Response
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

def generate_data():
    """Generator that yields data in chunks."""
    for i in range(1, 101):  # Simulate a series of data points
        yield f"data:{i}\n\n"
        time.sleep(0.1)  # Simulate delay between chunks

@app.route('/api/stream')
def stream():
    """Endpoint that streams data chunk by chunk."""
    return Response(generate_data(), content_type='text/event-stream')

if __name__ == "__main__":
    app.run(debug=True)
