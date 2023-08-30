# Use the official Nginx base image
FROM nginx:alpine

# Copy your custom nginx.conf file to the container
COPY nginx.conf /etc/nginx/nginx.conf

# Expose port 80
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
