# GitHub Webhooks에서 git push 될 때 보내는 post 메시지를 수신하는 서버
# 클라우드 서버에서 실행될 것
from flask import Flask, json
from flask_restful import Resource, Api

import os

buildBranch = 'main'
buildPath = '/home/thtjdgus65/lab-socket-programming'

buildCommand = 'cd ' + buildPath + ' && git stash && git pull origin ' + buildBranch

app = Flask(__name__)
api = Api(app)

class setDeploy(Resource):
    def post(self):
        os.system(buildCommand)
        return {'status' : 'success'}
    
api.add_resource(setDeploy, '/deploy')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
