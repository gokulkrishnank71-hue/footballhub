from flask import Flask, render_template
import requests

app = Flask(__name__)

NEWS_API_KEY = "54a9bcd2b0e44c35abc8dc3b7dc5fe6c"  # Replace with your NewsAPI key

@app.route("/")
def home():
    # Get latest football news
    url = f"https://newsapi.org/v2/everything?q=football&language=en&sortBy=publishedAt&apiKey={NEWS_API_KEY}"
    response = requests.get(url).json()
    articles = response.get("articles", [])[:10]  # limit to 10 articles

    return render_template("index.html", articles=articles)

if __name__ == "__main__":
    app.run(debug=True)
