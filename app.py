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

@app.route("/")
def index():
    return """
<h2>Team Configuration Service</h2>
<p>Internal platform for managing team scoped settings.</p>
<ul>
<li>POST /login</li>
<li>GET /api/team/&lt;team&gt;/settings</li>
<li>GET /health</li>
</ul>
<p>Active team is derived from the user session.</p>
"""

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
    if team == "team2":
        return jsonify({"team":team,"flag":FLAG})
    return jsonify({"team":team})

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
