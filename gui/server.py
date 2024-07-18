import flask

app = flask.Flask(__name__, template_folder="html")

@app.route("/")
def root():
    return flask.render_template("index.html")

@app.route("/download", methods=["GET", "POST"])
def download():
    if flask.request.method == "GET":
        return flask.render_template("download.html", bibles=)

@app.route("/delete")
def delete()
"

if __name__ == "__main__":
    app.run(host="localhost", port=1189)

