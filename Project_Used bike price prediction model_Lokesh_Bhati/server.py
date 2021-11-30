from flask import Flask,request,jsonify
import util

app = Flask(__name__)

@app.route('/get_column_names')
def get_column_names():
    response = {'Features' : util.get_feature_names()}
    return response


@app.route('/predict_price',methods=['POST'])
def predict_price():
    kms = float(request.form['kms'])
    year = float(request.form['year'])
    power = float(request.form['power'])

    city = request.form['cityName']
    own = request.form['ownerName']
    brand = request.form['brandName']
    model = request.form['modelName']

    age = 2021 - year
    #print(age)
    price = util.predict_bike_price(kms,age,power,city,own,brand,model)
    def roundup(x):
        return x if x % 100 == 0 else x + 100 - x % 100
    price = roundup(price)
    
    response = jsonify({'Estimated_Price':price})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


app.run()