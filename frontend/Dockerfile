# Use the official Node.js image as the base image for building
FROM node:14 AS build

# Set the working directory in the container
WORKDIR /app

COPY package*.json ./

# Install dependencies
RUN npm install

# Copy all the source code to the container
COPY . .


# Build the Vue application
RUN npm run build

# Node.js server stage
FROM node:14 AS server
WORKDIR /app
COPY --from=build /app ./
COPY server.js ./
RUN npm install express
EXPOSE 3000
CMD ["node", "server.js"]