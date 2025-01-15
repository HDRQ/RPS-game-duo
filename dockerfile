# Use Node.js as the base image
FROM node:19

# Set the working directory
WORKDIR /app

# Install pnpm globally
RUN npm install -g pnpm

# Copy package.json and pnpm-lock.yaml to the working directory
COPY package.json pnpm-lock.yaml ./

# Install dependencies using pnpm
RUN pnpm install

# Copy the rest of the application files to the working directory
COPY . .

# Build the application (optional, for React or similar)
RUN pnpm run build

# Set the default command to start the application
CMD ["pnpm", "start"]

# Expose the port (optional, for React or any app exposing a port)
EXPOSE 3000
