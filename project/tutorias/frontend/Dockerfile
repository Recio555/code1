# Etapa 1: Build de la app React
FROM node:22 AS build
WORKDIR /app
COPY . .
RUN npm install && npm run build

# Etapa 2: Servir archivos estáticos con nginx
FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html
COPY ./nginx/nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
