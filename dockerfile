# Use a Node.js base image
FROM node:19

# Set the working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the app
COPY . .

# Build the app
RUN npm run build

# Serve the app
RUN npm install -g serve
CMD ["serve", "-s", "build"]

# Expose the port (default: 3000)
EXPOSE 3000
