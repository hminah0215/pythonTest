from flask import Flask, render_template
#import flask하면 매번 flask. ~~~ 이런식으로 써야하는게 번거로워서 
import myUtil.hanbit as hanbit

app = Flask(__name__)

@app.route("/newBook")
def newBook():
    list = hanbit.getNewBook()
    return  render_template("newbook.html", list=list)

@app.route("/")
def index():
        return "<h1>hello</h1>"
if __name__ == "__main__":
    app.run(host="192.168.0.24",debug=True)