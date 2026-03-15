"""
main.py — LittleVision entry point
Run: python main.py
"""
from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "Littlevision aI"

from app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
