from __future__ import print_function

import pickle

import flask

import os

import sys

from flask import request,jsonify,make_response,Response

from stroke_segmentation import strokeSeg

#from rq import Queue

#from worker import conn

#from utils import count_words_at_url


# from werkzeug import secure_filename

app = flask.Flask(__name__)

APP_ROUTE=os.path.dirname(os.path.abspath(__file__))

# print('aa',APP_ROUTE)

#loading my model

# model = pickle.load(open("model.pkl","rb"),encoding="latin1")

# model = pickle.load(open("model.pkl","rb"))

# feature_array1=[float(i) for i in '7.4,0.66,0,1.8,0.075,13,40,0.9978,3.51,0.56,9.4'.split(",")]

# print(len(feature_array1),'\n',feature_array1)

# response1={}

# response1['predictions'] = model.predict([feature_array1]).tolist()

# print('ddffsdaad',response1['predictions'])

#defining a route for only post requests

@app.route('/', methods=['GET'])

def index():

    #getting an array of features from the post request's body

    # feature_array = request.get_json()['feature_array']

    # feature_array=[float(i) for i in '7.4,0.66,0,1.8,0.075,13,40,0.9978,3.51,0.56,9.4'.split(",")]

    #creating a response object

    #storing the model's prediction in the object

    # response = {}

    # response['predictions'] = model.predict([feature_array]).tolist()

    #returning the response object as json

    return flask.jsonify("hello")



@app.route('/<name>')

def hello_name(name):

    response={}

    response['name']=name

    return _corsify_actual_response(jsonify(response))

@app.route('/<int:id>')

def print_int(id):

    response={}

    response['idnumber']=id

    return _corsify_actual_response(jsonify(response))

@app.route('/search',methods=['GET','POST','OPTIONS'])

 def generate():
    
   if request.method == "OPTIONS": # CORS preflight

       return _build_cors_prelight_response()
    #getting an array of features from the post request's body

    # feature_array = request.get_json()['feature_array']

    # #creating a response object

    # #storing the model's prediction in the object

    # response = {}

    # response['predictions'] = model.predict([feature_array]).tolist()

    # print(response['predictions'])

    # #returning the response object as json

   elif request.method=="POST" :
   

     target=os.path.join(APP_ROUTE,'files/')

        # print('target',target,file=sys.stderr)

     if not os.path.isdir(target):

        os.mkdir(target)

     f = request.get_json(['COORDINATES'])

     coor = f['COORDINATES']

     final_coor = []
     for item in coor:
        final_coor.append(item['coordinates'])
     #result = [1,2]
     #response['result'] = result
     #yield _corsify_actual_response(jsonify(response)
        
     result = strokeSeg(final_coor)
   

     response={}

     response['result']=result

     return _corsify_actual_response(jsonify(response))
       
   
        

        # print('request',request,file=sys.stderr)

        # print('file',f,file=sys.stderr)

        # destination="/".join([target,f.filename])

        # print('destination',destination,file=sys.stderr)

        # f.save(secure_filename(target))

        # f.save(destination)

       


'''@app.route('/back',methods=['GET','POST','OPTIONS']))

def background():
     if request.method == "OPTIONS": # CORS preflight

        return _build_cors_prelight_response()
    
     elif request.method=="POST" :
          q = Queue(connection=conn)
        
          result = q.enqueue(count_words_at_url, 'https://damp-plains-82912.herokuapp.com/search')
            
          response={}

          response['result']=result

          return _corsify_actual_response(jsonify(response))'''


def _build_cors_prelight_response():

    response = make_response()

    response.headers.add("Access-Control-Allow-Origin", "*")

    response.headers.add('Access-Control-Allow-Headers', "*")

    response.headers.add('Access-Control-Allow-Methods', "*")

    return response



def _corsify_actual_response(response):

    response.headers.add("Access-Control-Allow-Origin", "*")

    return response
#hello
