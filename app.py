from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <h1>DevSecOps Application</h1>
    <p>Running on Amazon EKS</p>
    <p>Pod: {socket.gethostname()}</p>
    """

@app.route("/health")
def health():
    return "healthy", 200

app.run(host="0.0.0.0", port=5000)