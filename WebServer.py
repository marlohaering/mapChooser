from flask import Flask, render_template, request

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/<float:longitude>/<float:latitude>')
def points(longitude, latitude):
    print(f'{longitude} | {latitude}')
    return render_template("mapchoose.html", latitude=latitude, longitude=longitude)


if __name__ == "__main__":
    app.run()