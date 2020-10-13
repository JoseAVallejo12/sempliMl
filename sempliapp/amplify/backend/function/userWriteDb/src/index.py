import json
import boto3
import uuid



def handler(event, context):
    """ Lambda main funtion """

    codeStatus = 200
    message = ""
    if event.get("pathParameters") is not None:
        userData = event.get("pathParameters").get("user")
        if userData.get("userNew") is not None:
            post_user(userData)
            codeStatus = 200
            message = "Data save done"
        else:
            codeStatus = 404
            message = "Not parameter given to function"
    else:
        codeStatus = 404
        message = "Not parameter given to function"

    return {
                "statusCode": codeStatus,
                "body": json.dumps({
                    "userData": message
                })
            }

def post_user(userDataSet):

    dynamodb = boto3.resource('dynamodb')
    uid = uuid.uuid1()

    keys = ['recency', 'state', 'arrears_days', 'total_paid', 'monto_acum', 'uso_recursos',
            'plazo', 'sector', 'ingresos', 'ubicacion', 'estrato_min', 'procesos_jud', 'alertas',
            'score_bureau', 'huellas', 'website', 'instagram', 'linkedin_empresa',
            'linkedin_empresarios', 'edad_empr', 'activador', 'numero_acc', 'impacto',
            'acceso_banca', 'empleados', 'mujeres_empr', 'mujeres_cargos']
    new_dict = dict(zip(keys, userDataSet.get('userNew')))
    new_dict.update({'id': str(uid)})
    table = dynamodb.Table('customer02-dev')
    print(new_dict)
    table.put_item(
        Item = new_dict
    )
