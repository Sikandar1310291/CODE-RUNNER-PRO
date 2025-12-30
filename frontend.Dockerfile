FROM nginx:alpine

# Remove default config
RUN rm /etc/nginx/conf.d/default.conf

# Copy custom config
COPY nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf

# Copy website files to the standard Nginx root
COPY . /usr/share/nginx/html/

# Ensure the container stays clean (optional: remove server folder if not needed in frontend)
RUN rm -rf /usr/share/nginx/html/server /usr/share/nginx/html/nginx

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
