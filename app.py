from flask import Flask, render_template, jsonify

app = Flask (
  __name__)

EXP = [
  {
    'id': 1,
    'title': 'C++',
    'projects': 'Robotic Arm',
    'description': 'A robotic arm that can move with a given set of commands',
  },
  {
    'id': 2,
    'title': 'Python',
    'projects': 'Card Reader',
    'description': 'A card reader that can read a card from video',
  },
  {
    'id': 3,
    'title': 'HTML',
    'projects': 'Tiger Webpage',
    'description': 'A webpage with information about how to save tigers from extinction',
  }
]

@app.route("/")
def home():
  return render_template("home.html", exps=EXP)

@app.route("/about")
def about():
  return render_template("about.html")
  
@app.route("/exp")
def list_jobs():
  return jsonify(EXP)
  
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)