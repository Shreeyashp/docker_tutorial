from flask import Flask
import numpy as np
import pandas as pd

app=Flask(__name__)

app.route('/',methods=['GET'])
def home():
    return 'Hello everyone from shreeyash'


if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000) # 0.0.0.0 whichever system its run it will run as local host