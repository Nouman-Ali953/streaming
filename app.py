# from flask import Flask, Response
# from flask_cors import CORS
# import time

# app = Flask(__name__)
# CORS(app)  # Enable Cross-Origin Resource Sharing

# def generate_data():
#     """Generator that yields data in chunks."""
#     for i in range(1, 101):  # Simulate a series of data points
#         yield f"data:{i}\n\n"
#         time.sleep(0.1)  # Simulate delay between chunks

# @app.route('/api/stream')
# def stream():
#     """Endpoint that streams data chunk by chunk."""
#     return Response(generate_data(), content_type='text/event-stream')

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, Response
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

def generate_data():
    """Generator that yields a predefined paragraph word by word."""
    paragraph = (
        "Flask is a lightweight WSGI web application framework in Python. "
        "It is designed with simplicity and flexibility in mind, allowing "
        "developers to build small to medium-sized applications quickly. "
        "Flask is especially popular for its modularity and ease of use, "
        "making it a great choice for microservices and REST APIs."
    )
    
    words = paragraph.split()  # Split paragraph into words
    for word in words:
        yield f"data:{word}\n\n"  # Stream each word
        time.sleep(0.1)  # Simulate delay between words

@app.route('/api/stream')
def stream():
    """Endpoint that streams data word by word."""
    return Response(generate_data(), content_type='text/event-stream')

if __name__ == "__main__":
    app.run(debug=True)
