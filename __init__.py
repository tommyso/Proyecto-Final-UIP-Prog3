from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
@app.route("/<name>")
def index(name=None):
    return render_template('Review.html', name=name)

@app.route("/end")
def end():
    return render_template('return.html')

if __name__ == "__main__":
    app.run()