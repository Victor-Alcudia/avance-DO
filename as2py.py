import boto3
from botocore.exceptions import ClientError

# Configuración de constantes
AMI_ID = "ami-0e2c8ca47bde19891"  # Amazon Linux 2023 en us-east-1
INSTANCE_TYPE = "t2.micro"
KEY_NAME = "vockey" # Llave por defecto en Vocareum

#Función para crear la instancia
def crear_instancia_controlada():
    # Se inicializa el cliente de EC2
    ec2 = boto3.resource('ec2', region_name='us-east-1')
    
    print("--- Iniciando aprovisionamiento controlado ---")

    try:
        # Se verifica el número de instancias activas para no exceder límites
        instances = ec2.instances.filter(
            Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
        )
        count = sum(1 for _ in instances)
        
        if count >= 4:
            print(f"Límite alcanzado. Ya tienes {count} instancias activas.")
            return

        # Se crea la instancia
        print(f"Creando instancia {INSTANCE_TYPE}...")
        nueva_instancia = ec2.create_instances(
            ImageId=AMI_ID,
            MinCount=1,
            MaxCount=1,
            InstanceType=INSTANCE_TYPE,
            KeyName=KEY_NAME,
            TagSpecifications=[{
                'ResourceType': 'instance',
                'Tags': [
                    {'Key': 'Name', 'Value': 'Servidor-Financiero-DevOps'},
                    {'Key': 'Proyecto', 'Value': 'SolucionesFuturo'}
                ]
            }]
        )

        print(f"INSTANCIA CREADA CON ÉXITO. ID de la instancia: {nueva_instancia[0].id}")

    except ClientError as e:
        print(f"Error de permisos: {e}")
    except Exception as e:
        print("Algo salió mal, pero no sabemos qué es :(")

#Se ejecuta la función definida anteriormente
if __name__ == "__main__":
    crear_instancia_controlada()
