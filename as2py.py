import boto3
from botocore.exceptions import ClientError

# Configuración actualizada
AMI_ID = "ami-0ec10929233384c7f"  # Ubuntu en us-east-1
INSTANCE_TYPE = "t2.micro"
KEY_NAME = "vockey"

def crear_instancia_ubuntu():
    # Usamos la sesión activa para asegurar permisos
    session = boto3.Session()
    ec2 = session.resource('ec2', region_name='us-east-1')
    
    print(f"--- Iniciando creación de instancia Ubuntu ({AMI_ID}) ---")

    try:
        # Ejecución con los parámetros mínimos obligatorios
        # Nota: No incluimos BlockDeviceMappings ni TagSpecifications aquí
        # para evitar el 'Explicit Deny' del laboratorio.
        nueva_instancia = ec2.create_instances(
            ImageId=AMI_ID,
            MinCount=1,
            MaxCount=1,
            InstanceType=INSTANCE_TYPE,
            KeyName=KEY_NAME
        )

        instancia = nueva_instancia[0]
        print(f"ÉXITO. Instancia creada con ID: {instancia.id}")
        
        # Intentamos asignar el nombre por separado una vez creada
        print("Asignando nombre...")
        instancia.create_tags(Tags=[{'Key': 'Name', 'Value': 'Servidor-Ubuntu-Lab'}])
        print("Configuración finalizada.")

    except ClientError as e:
        # Esto nos dirá exactamente qué recurso está fallando ahora
        print(f"Error de AWS (ClientError): {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    crear_instancia_ubuntu()
