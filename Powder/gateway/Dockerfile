# Use official NGINX image
FROM nginx:latest

# Remove the default nginx.conf
RUN rm /etc/nginx/nginx.conf

# Copy the custom nginx.conf into the container
COPY config/nginx.conf /etc/nginx/nginx.conf

# Define volumes for nginx.conf
VOLUME ["/config:/etc/nginx/"]

# Expose port 80
EXPOSE 80