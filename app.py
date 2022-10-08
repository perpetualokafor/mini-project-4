# import Flask and jsonify
from flask import Flask, jsonify, request
# import Resource, Api and reqparser
from flask_restful import Resource, Api, reqparse
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
import pickle
app = Flask(__name__)
api = Api(app)
df = pd.read_csv("/Users/perpetualokafor/Downloads/mini-project-4/data/data1.csv") 
model = pickle.load( open( "model.pkl", "rb" ))

#Now, we need to create an endpoint where we can communicate with our ML model. 
#This time, we are going to use POST request.

LE = LabelEncoder()
encode_cols = ['Gender','Married','Education','Self_Employed','Property_Area']
for col in encode_cols:
    df[col] = LE.fit_transform(df[col])

class Scoring(Resource):
    def post(self):
        json_data = request.get_json()
        df = pd.DataFrame(json_data.values(), index=json_data.keys()).transpose()
        # getting predictions from our model.
        # it is much simpler because we used pipelines during development
        res = model.predict_proba(df)
        # we cannot send numpt array as a result
        return res.tolist() 
# assign endpoint
api.add_resource(Scoring, '/scoring')
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
  