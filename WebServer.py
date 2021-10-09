from flask import Flask, render_template, request

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/<float:latitude>/<float:longitude>')
def points(latitude, longitude):
    return render_template("mapchoose.html", latitude=latitude, longitude=longitude)


if __name__ == "__main__":
    app.run()