from flask import Flask, render_template
import random

app = Flask(__name__)

images = [
  "http://media.giphy.com/media/qoxM1gi6i0V9e/giphy.gif",
  "http://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif",
  "http://media.giphy.com/media/tT0wtdSJvE0Rq/giphy.gif"
]

@app.route('/')
def index():
  caturl = random.choice(images)
  return render_template("index.html", url=caturl)

if __name__ == "__main__":
  app.run(host="0.0.0.0")
