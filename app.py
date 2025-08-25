from flask import Flask, render_template, request

app = Flask(__name__)

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Team search route
@app.route("/team")
def team():
    team_name = request.args.get("team")
    return render_template("team.html", team=team_name)

# Predictions route (placeholder)
@app.route("/predict")
def predict():
    return "<h1>🔮 Match Prediction feature coming soon!</h1>"

# Live scores route (placeholder)
@app.route("/scores")
def scores():
    return "<h1>📊 Live Scores feature coming soon!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
