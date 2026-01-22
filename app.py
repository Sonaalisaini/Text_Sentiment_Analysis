from flask import Flask, render_template, request, jsonify
from textblob import TextBlob

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze_sentiment():
    data = request.get_json()
    text = data["text"]

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive 😊"
    elif polarity < 0:
        sentiment = "Negative 😞"
    else:
        sentiment = "Neutral 😐"

    return jsonify({
        "sentiment": sentiment,
        "polarity": round(polarity, 2)
    })

if __name__ == "__main__":
    app.run(debug=True)
