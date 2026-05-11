import json
import random

m = ["este es un mensaje aleatorio en formato JSON"]

def l_hand(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps(random.choice(m))
    }
