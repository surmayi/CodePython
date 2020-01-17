#from bottle import response, request
from flask import Flask,jsonify, request
from flask_restful import Resource, Api
from blazePay import simBp
from axis import simAxis
from olaMoney import olaMoneySim
from HPYIndusIndPg import HPYIndusIndPgSim
import json
import logging


app = Flask(__name__)                  # the set of names
api = Api(app)

logging.basicConfig(filename="RefundSim.log", 
                    format='%(asctime)s %(message)s', 
                    filemode='a')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class BlazePay(Resource):
    def post(self):
        data = request.json
        logger.info('Request Received For BlazePay Refund as below - ')
        logger.info(data)
        data = simBp(data)
        logger.info('Sending Response For BlazePay as below - ')
        logger.info(data)
        return data

class AxisSim(Resource):
    def post(self):
        logger.info('Request Received For Axis Refund as below - ')
        data = request.get_data()
        logger.info(data)
        data = simAxis(data)
        logger.info('Sending Response For Axis Refund as below - ')
        logger.info(data)
        return data

class OlaMoneySim(Resource):
    def post(self):
        data = request.json
        logger.info('Request Received For Ola Money as below - ')
        logger.info(data)
        data = olaMoneySim(data)
        logger.info('Sending Response For Ola Money Refund as below - ')
        logger.info(data)
        return data

class HPYIndusIndPg(Resource):
    def post(self):
        data = request.json
        logger.info('Request Received For HYPIndusIndPg Refund as below - ')
        logger.info(data)
        data = HPYIndusIndPgSim(data)
        logger.info('Sending Response For HYPIndusIndPg Refund as below - ')
        logger.info(data)
        return data

api.add_resource(BlazePay,'/bpSim')
api.add_resource(AxisSim,'/axisSim')
api.add_resource(OlaMoneySim,'/olaMoneySim')
api.add_resource(HPYIndusIndPg,'/HPYIndusIndPgSim')

app.run(port=2000)