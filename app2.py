from flask import Flask,jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

items =[]

class Items(Resource):
    def get(self,name):
        item = next(filter(lambda item : item['name']==name , items))
        return item, 400
    
    
    def post(self,name):
        if next(filter(lambda item: item['name']==name,items),None):
            return {'message':"An item with name '{}' already exists".format(name)},400
        data = request.get_json(force=True)
        item = {"name" : name , "price" : data['price']}
        items.append(item)
        return item ,201
        
    def delete(self,name):
        for item in items:
            if item['name']==name:
                items.remove(item)
        return item ,200

class ItemList(Resource):
    def get(self):
        return items

api.add_resource(Items,'/Items/<string:name>')

api.add_resource(ItemList,'/Items')


app.run(port=4001)