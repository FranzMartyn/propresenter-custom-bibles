import flask
import server_utils

app = flask.Flask(__name__, template_folder="static", static_folder="static")


@app.route("/")
def root():
    return flask.render_template("index.html")


@app.route("/download", methods=["GET", "POST"])
def download():
    if flask.request.method == "GET":
        return flask.render_template("download.html")
    return "POST request response from /download"


@app.route("/delete", methods=["GET", "POST"])
def delete():
    if flask.request.method == "GET":
        return flask.render_template("delete.html")
    return "POST request response from /delete"


if __name__ == "__main__":
    app.run(host="localhost", port=1189)

