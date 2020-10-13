import json
import random

def handler(event, context):
    """Generate client automatic"""
    # variables numéricas.
    recency = random.randint(26, 318)
    arrears_days = random.randint(0, 258)
    total_paid = random.randint(0, 215213613)
    monto_acum = random.randint(30000000, 1299370581)
    estrato_min = random.randint(2, 6)
    score_bureau = random.randint(0, 982)
    huellas = random.randint(0, 44)
    edad_empr = random.randint(22, 74)
    numero_acc = random.randint(1, 69)
    empleados = random.randint(1, 500)
    mujeres_cargos = random.randint(0, 25)
    # variables alfanuméricas.
    state = ran(['PAID', 'LATE'])
    uso_recursos = ran(['CR', 'KT - CO', 'KT - EX', 'SP'])
    plazo = ran(['Menos de 12 meses', '13 a 24 meses',
                 '25 a 36 meses', 'Más de 37 meses'])
    sector = ran(['Comercio', 'Industria', 'Servicios'])
    ingresos = ran(['Growth', 'Scale Up', 'Seed', 'Venture'])
    ubicacion = ran(['Armenia', 'Barranquilla', 'Bello', 'Bogotá D.C.',
                     'Bucaramanga', 'Cali', 'Cartagena de indias', 'Copacabana',
                     'Envigado', 'Itagüí', 'La Ceja', 'La Estrella', 'Manizales',
                     'Marinilla', 'Medellín', 'Neiva', 'Pereira',
                     'Rionegro', 'Sabaneta', 'Santa Marta'])
    procesos_jud = ran(['Si', 'No'])
    alertas = ran(['Si', 'No'])
    website = ran(['Si', 'No'])
    instagram = ran(['Si', 'No'])
    linkedin_empresa = ran(['Si', 'No'])
    linkedin_empresarios = ran(['Si', 'No'])
    activador = ran(['CommunicationMedia', 'CreditProfessionalContact',
                     'Email', 'Fenalco', 'FriendOrColleague', 'Internet',
                     'Newspapers', 'Other', 'Referrer', 'RutaN', 'SocialNetworks'])
    impacto = ran(['Si', 'No'])
    acceso_banca = ran(['Si', 'No'])
    mujeres_empr = ran(['Si', 'No'])

    customer = [recency, state, arrears_days, total_paid, monto_acum, uso_recursos,
            plazo, sector, ingresos, ubicacion, estrato_min, procesos_jud, alertas,
            score_bureau, huellas, website, instagram, linkedin_empresa,
            linkedin_empresarios, edad_empr, activador, numero_acc, impacto,
            acceso_banca, empleados, mujeres_empr, mujeres_cargos]

    return {
        "statusCode": 200,
        "body": json.dumps({
            "userNew": customer,
            # "location": ip.text.replace("\n", "")
        }),
    }

def ran(list):
    """Return a ramdom value from list givend"""
    return(list[random.randint(0, len(list) - 1)])