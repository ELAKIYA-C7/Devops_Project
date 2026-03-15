from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/health")
def health():
    return {"status": "pipeline running"}

if __name__ == "__main__":
    # Run on all interfaces so it can be accessed outside container
    app.run(host="0.0.0.0", port=5000)