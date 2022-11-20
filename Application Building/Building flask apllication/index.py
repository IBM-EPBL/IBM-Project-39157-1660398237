# importing the required libraries 

from flask import Flask,render_template,request
import cv2
import numpy as np
from keras.models import load_model

app = Flask(__name__, static_url_path='/static')



@app.route('/',methods=['POST','GET'])
