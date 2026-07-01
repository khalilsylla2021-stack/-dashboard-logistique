from flask import Flask, jsonify

app = Flask(__name__)

AGENTS = [
    {"nom": "Khalil", "commandes": 120, "temps_moyen": 3.2, "presence": True},
    {"nom": "Amadou", "commandes": 95, "temps_moyen": 4.1, "presence": True},
    {"nom": "Fatou", "commandes": 110, "temps_moyen": 3.8, "presence": False}
]

@app.route("/")
def home():
    return "Dashboard Logistique OK 🚀"

@app.route("/api/data")
def data():
    return jsonify({"agents": AGENTS})

if __name__ == "__main__":
    app.run()