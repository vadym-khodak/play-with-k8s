FROM node:14.17.1-alpine AS builder
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
ENV NODE_ENV production
COPY package.json ./
COPY package-lock.json ./
RUN npm ci --silent
COPY . ./
RUN npm run build

FROM nginx:stable-alpine as production
ENV NODE_ENV production
COPY --from=build /app/build /usr/share/nginx/html
COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
