import boto3
from botocore.exceptions import ClientError

AMI_ID = "ami-0ec10929233384c7f"  # Ubuntu 22.04 LTS
INSTANCE_TYPE = "t2.micro"
KEY_NAME = "vockey"

def crear_instancia_super_limpia():
    session = boto3.Session()
    ec2 = session.resource('ec2', region_name='us-east-1')
    
    print("--- Intentando bypass de política de volumen ---")

    try:
        nueva_instancia = ec2.create_instances(
            ImageId=AMI_ID,
            MinCount=1,
            MaxCount=1,
            InstanceType=INSTANCE_TYPE,
            KeyName=KEY_NAME,
            # ESTE BLOQUE ES LA CLAVE PARA EL ERROR DE VOLUME/*
            BlockDeviceMappings=[
                {
                    'DeviceName': '/dev/sda1', # Nombre estándar para el root de Ubuntu
                    'Ebs': {
                        'VolumeSize': 8,
                        'VolumeType': 'gp2',      # Obligatorio gp2 en muchos labs
                        'Encrypted': False,       # El 'Explicit Deny' suele ser por esto
                        'DeleteOnTermination': True
                    },
                },
            ]
        )

        instancia = nueva_instancia[0]
        print(f"¡LOGRADO! ID de instancia: {instancia.id}")

    except ClientError as e:
        print(f"Error persistente: {e}")
    except Exception as e:
        print(f"Otro error: {e}")

if __name__ == "__main__":
    crear_instancia_super_limpia()
