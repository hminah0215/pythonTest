import flask
import myutil.kma as kma

app = flask.Flask(__name__)

@app.route("/kma")
def listkma():
    list = kma.pro()
    return flask.render_template("kma.html", list=list)


@app.route("/insert")
def insert():
    name = "이순신"
    return flask.render_template("insert.html", name=name )

@app.route("/list")
def list():
    return "<h2>게시물 목록</h2>"

@app.route("/")
def index():
    return "<h1>Hello Flask!!</h1>"

if __name__ == "__main__":
    app.run(host='192.168.0.13', debug=True)