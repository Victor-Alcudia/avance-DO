VERDE='\033[0;32m'
NC='\033[0m'

echo -e "${VERDE}>>> Actualizando sistema e instalando Python y Cron...${NC}"
sudo apt-get update -y
sudo apt-get install python3 python3-pip cron -y

echo -e "${VERDE}>>> Instalando Boto3...${NC}"
sudo apt install python3-boto3

echo -e "${VERDE}>>> Configurando y verificando el servicio Cron...${NC}"
sudo systemctl enable cron
sudo systemctl start cron

echo -e "${VERDE}>>> Resumen de instalación:${NC}"
python3 --version
pip3 --show boto3 | grep -E "Name|Version"
systemctl is-active cron

echo -e "${VERDE}>>> ¡Entorno listo para automatización con AWS y tareas programadas!${NC}"
