import json
import numpy as np
from joblib import dump, load

def handler(event, context):
    data = event.get('multiValueQueryStringParameters')
    if data is None or data.get('userNew') is None:
        return {
            "statusCode": 404,
            "body": json.dumps({
                "use" : "url + params={useNew : []}"
            })
        }
    dataList = event.get('multiValueQueryStringParameters').get('userNew')
    res = evaluar_cliente(dataList)
    return {
        "statusCode": 200,
        "body": json.dumps({
            #'userData': dataList,
            'userCluster': res
            }),
    }

def evaluar_cliente(dataList):
    # load the model from disk
    dato = np.array([dataList])
    clf = load('model.joblib') 
    categorical_columns = [1, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16,
                       17, 18, 20, 21, 22, 23, 25]
    try:
        if type(dato).__module__ == np.__name__:
            predecir = clf.predict(
                dato, categorical=categorical_columns)
            print(f'El cliente pertenece al cluster: {predecir.item(0)}')
            return predecir.item(0)
        else:
            print("No se puede procesar el dato")
            return "none"
    except:
        print("Revisar los datos. Están incompletos y/o orden incorrecto")
        return "none"