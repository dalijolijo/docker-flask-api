from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

#class HelloWorld(Resource):
#    def get(self):
#        return {'about':'Hello World!'}
#
#    def post(self):
#        some_json = request.get_json()
#        return {'you sent': some_json}, 201

#class Multi(Resource):
#    def get(self, num):
#        return {'result': num * 10}

class limxtec(Resource):
    def get(self):
        return {'imageUrl':'https://bitcore.cc/wp-content/uploads/2019/12/advxwallet00.jpg',"link": "https://limxtec.org"}

class btx(Resource):
    def get(self):
        return {'imageUrl':'https://bitcore.cc/wp-content/uploads/2019/12/advxwallet00.jpg',"link": "https://bitcore.cc"}

class bsd(Resource):
    def get(self):
        return {'imageUrl':'https://bitcore.cc/wp-content/uploads/2019/12/advxwallet00.jpg',"link": "https://bitsend.info"}

class btdx(Resource):
    def get(self):
        return {'imageUrl':'https://bitcore.cc/wp-content/uploads/2019/12/advxwallet00.jpg',"link": "https://bit-cloud.info"}

class mec(Resource):
    def get(self):
        return {'imageUrl':'https://bitcore.cc/wp-content/uploads/2019/12/advxwallet00.jpg',"link": "https://megacoin.eu"}

#api.add_resource(HelloWorld, '/')
#api.add_resource(Multi, '/multi/<int:num>')
api.add_resource(limxtec,'/limxtec')
api.add_resource(btx,'/btx')
api.add_resource(bsd,'/bsd')
api.add_resource(btdx,'/btdx')
api.add_resource(mec,'/mec')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
