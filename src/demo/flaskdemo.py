#! /usr/bin/env python
#coding=utf-8

from flask import Flask
from flask_restful import Resource, Api
import base64

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        #return {'hello': str(base64.b64encode(b'world'))}
        #return {'hello': "world"}
        return {'hello': base64.b64encode(b'world').decode("utf-8")}

api.add_resource(HelloWorld, '/hello')


if __name__ == '__main__':
    app.run(debug=True)
