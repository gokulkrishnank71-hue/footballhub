from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    team_name = request.form.get("team")
    return redirect(url_for("team_page", team_name=team_name))

@app.route("/team/<team_name>")
def team_page(team_name):
    # Mock data for now – later connect to API or DB
    recent_matches = [
        {"opponent": "Arsenal", "result": "W"},
        {"opponent": "Chelsea", "result": "D"},
        {"opponent": "Liverpool", "result": "L"},
        {"opponent": "Tottenham", "result": "W"},
        {"opponent": "Man City", "result": "L"},
    ]
    return render_template("team.html", team_name=team_name, recent_matches=recent_matches)

if __name__ == "__main__":
    app.run(debug=True)
