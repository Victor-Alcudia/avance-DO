LOG_DIR="/var/log/soluciones_futuro"

mkdir -p $LOG_DIR

echo "--- Iniciando limpieza de logs en $LOG_DIR ---"

find $LOG_DIR -type f -name "*.log" -mtime +7 -delete

echo "Limpieza completada el: $(date)" >> /var/log/clean_history.log
