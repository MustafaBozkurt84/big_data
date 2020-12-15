from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
import glob
import pandas as pd
import numpy as np
import joblib

app = Flask(__name__)

api = Api(app=app)
model = joblib.load("/app/saved_models/01.knn_with_iris_dataset.pkl")
labelencoder_y = joblib.load("/app/saved_models/01.knn_with_iris_label_encoder.pkl")


class Classify(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('SepalLengthCm',
                        type=float,
                        required=True,
                        help="This field cannot left blank!")
    parser.add_argument('SepalWidthCm',
                        type=float,
                        required=True,
                        help="This field cannot left blank!")
    parser.add_argument('PetalLengthCm',
                        type=float,
                        required=True,
                        help="This field cannot left blank!")
    parser.add_argument('PetalWidthCm',
                        type=float,
                        required=True,
                        help="This field cannot left blank!")

    def return_prediction(self):
        data = Classify.parser.parse_args()

        SepalLengthCm = data['SepalLengthCm']
        SepalWidthCm = data['SepalWidthCm']
        PetalLengthCm = data['PetalLengthCm']
        PetalWidthCm = data['PetalWidthCm']

        input_data = np.array([SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm]).reshape(1, 4)

        x = model.predict(input_data)
        out_label = labelencoder_y.inverse_transform(x)
        df_pred_result = pd.DataFrame()
        df_pred_result['label'] = list(out_label)
        # df_pred_result['score'] = list(x[1])
        # df_pred_result_with_topic_id = pd.merge(left=df_label_topic_id_map, right=df_pred_result, on='label')
        out = df_pred_result.to_json(orient='records', force_ascii=False)
        return out

    def get(self):
        out = self.return_prediction()
        return jsonify({'result': out})


api.add_resource(Classify, '/iris')  # http://127.0.0.1:8082/iris

app.run(host="0.0.0.0", port=8082)