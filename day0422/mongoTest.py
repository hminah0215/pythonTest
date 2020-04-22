from pymongo import MongoClient

client = MongoClient("localhost",27017)
db = client['bit']
goods = db['goods'] #goods가 컬렉션이름이 된다.


#   모든 상품목록을 출력
list = goods.find({},{"_id":0})
#print(type(list))
arr = []
for g in list:
    arr.append(g)
    # print(g)
    # print(type(g))
print(arr)

# g = {"no":1,"item":"나이키공","qty":10,"price":25000,"fname":"ball1.jpg","detail":"좋은 공입니다."}

# _id = goods.insert_one(g).inserted_id
# print(_id)

# list = [
#     {"no":2, "item":"나이키 유니폼","qty":10,"price":65000,"fname":"cloth1.jpg", "detail":"좋은 유니폼입니다."},
#     {"no":3, "item":"나이키 축구화","qty":10,"price":85000,"fname":"shoe1.jpg", "detail":"좋은 축구화입니다."},
#     {"no":4, "item":"나이키 스타킹","qty":10,"price":8000,"fname":"stock1.jpg", "detail":"좋은 스타킹입니다."}]

# _ids = goods.insert_many(list).inserted_ids
# print(_ids)