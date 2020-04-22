from flask import Flask, render_template
import myutil.hanb as hanb

app = Flask(__name__)

@app.route("/newBook")
def newBook():
    list = hanb.getNewBook()
    r = "pro("+str(list)+")"
    return r
    # return  render_template("newBook.html", list=list)

@app.route("/")
def index():
    return "<h1>Hello</h1>"

if __name__ == "__main__":
    app.run(host="192.168.0.24", debug=True)

