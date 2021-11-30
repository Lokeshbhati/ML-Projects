import pickle
import json
import numpy as np

_data_columns = None
_model = None

def load_artifacts():
    global _data_columns
    global _model
    
    print('loading artifacts....')

    with open('./columns.json','r') as f:
        _data_columns = json.load(f)['features']

    with open('./used_bike_price.pickle','rb') as f:
        _model = pickle.load(f)

    print('Artifacts loaded suceessfully')
        
        
        
def predict_bike_price(kms,age,power,cityName,ownerName,brandName,modelName):
    
    input = np.zeros(len(_data_columns))
    
    input[0] = kms
    input[1] = age
    input[2] = power
    
    city = _data_columns.index(cityName.lower())
    owner = _data_columns.index(ownerName.lower())
    brand = _data_columns.index(brandName.lower())
    model = _data_columns.index(modelName.lower())
    input[city] = 1
    input[owner] = 1
    input[brand] = 1
    input[model] = 1
   
    return _model.predict([input])[0]
        
    
    
def get_feature_names():
    print(_data_columns)
    
load_artifacts()
# get_features_names()
print(predict_bike_price(25000,4,120.0,'Ahmedabad','second owner or more','tvs','avenger street 220'))
    
    