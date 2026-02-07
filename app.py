# medium-1-team-switcher/app.py
from flask import Flask, request, session, jsonify
from flask_session import Session
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = "team"
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

FLAG = os.environ.get("FLAG","CTF{dev}")

USERS = {
    "alice": ["team1"],
    "bob": ["team2"]
}

@app.route("/health")
def health():
    return "ok"

@app.route("/login", methods=["POST"])
def login():
    u = request.json.get("user")
    if u not in USERS:
        return jsonify({"err":"bad user"}),403
    session["user"] = u
    session["active_team"] = USERS[u][0]
    return jsonify({"ok":True})

@app.route("/api/team/<team>/settings")
def settings(team):
    # BUG: trusts session team instead of request ownership
    if team == "team2":
        return jsonify({"team":team,"flag":FLAG})
    return jsonify({"team":team})

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
