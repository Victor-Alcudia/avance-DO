# ETAPA 1: Construcción (Build)
FROM node:18-alpine AS build-stage
WORKDIR /app
# Copiamos archivos de dependencias
COPY package*.json ./
RUN npm install
# Copiamos el resto del código y construimos
COPY . .
RUN npm run build

# ETAPA 2: Producción (Imagen final ligera)
FROM nginx:stable-alpine
# Copiamos solo los archivos construidos desde la etapa anterior
# Esto reduce el tamaño de la imagen drásticamente
COPY --from=build-stage /app/dist /usr/share/nginx/html
# Copiamos una configuración personalizada de nginx si fuera necesaria
# COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
