from flask import Flask, render_template, request
from recommender import generate_playlist

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    playlist = []
    if request.method == "POST":
        city = request.form["city"]
        mood = request.form["mood"]
        playlist = generate_playlist(city, mood)
    return render_template("index.html", playlist=playlist)

if __name__ == "__main__":
    app.run(debug=True)
