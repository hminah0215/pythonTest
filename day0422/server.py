from flask import Flask, render_template, request
import myutil.hanb as hanb
# import myutil.webtoon as wt
import myutil.goods as goods
import os
import numpy

app = Flask(__name__)

@app.route("/goodsUpdateOk",methods=['POST'])
def goodsUpdateOk():
    no = int(request.form['no'])
    item = request.form['item']
    qty = int(request.form['qty'])
    price = int(request.form['price'])
    detail = request.form['detail']

    oldFname = request.form['oldFname']
    #파일을 반환하는 request.files
    f = request.files['fname']
    fname = oldFname

    if f.filename != "":
        f.save("day0422/img/"+f.filename)
        fname = f.filename

    q = {"no":no}
    doc = {"item":item,"qty":qty,"price":price,"fname":fname,"detail":detail}
    re = goods.updateGoods(q,doc)
    if re > 0 and f.filename != "":
        os.remove("day0422/img/"+oldFname)
    return "ok"

@app.route("/goodsUpdate/<no>")
def goodsUpdate(no):
    #print("수정할 상품번호",no)
    g = goods.getGoods(int(no))
    return render_template("goodsUpdate.html", g = g)

@app.route("/goodsDelete/<no>")
def goodsDelete(no):
    g = goods.getGoods(int(no))
    fname= g['fname']
    re =goods.deleteGoods(int(no))
    if re > 0:
        os.remove("day0422/img/"+fname)
    return  "ok"

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

