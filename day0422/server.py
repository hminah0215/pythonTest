from flask import Flask, render_template, request
import myutil.hanb as hanb
# import myutil.webtoon as wt
import myutil.goods as goods

app = Flask(__name__)

@app.route("/detailGoods/<no>")
def goodsDetail(no):
    doc = goods.getGoods(int(no))
    return render_template("detailGoods.html",doc = doc)

@app.route("/goodsInsert")
def goodsInsert():
    return render_template("goodsInsert.html")

@app.route("/goodsInsertOk",methods=['POST'])
def goodsInsertOk():
    no = int(request.form['no'])
    item = request.form['item']
    qty = int(request.form['qty'])
    price = int(request.form['price'])
   # fname = request.form['fname']
    detail = request.form['detail']
    #파일을 반환하는 request.files
    f = request.files['fname']
    f.save("day0422/img/"+f.filename)
    fname = f.filename

    
    doc = {"no":no,"item":item,"qty":qty,"price":price,"fname":fname,"detail":detail}
    _id = goods.insert(doc)
    print(_id)
    return "ok" 

@app.route("/goodsList")
def goodsList():
    list = goods.listAll();
    return render_template("goodsList.html", list=list)


# @app.route("/webtoon")
# def webtoon():
#     list = wt.getData()
#     r = "pro("+  str(list)   +")"
#     return r

@app.route("/webtoon")
def webtoon():
    list = wt.getData()
    r = "pro("+  str(list)   +")"
    return r
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

