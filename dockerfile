# Use Node.js as the base image
FROM node:16

# Set the working directory
WORKDIR /app

# Install pnpm globally
RUN npm install -g pnpm

# Copy package.json and package-lock.json (or pnpm-lock.yaml if using pnpm)
COPY pnpm-lock.yaml

# Install dependencies using pnpm
RUN pnpm install

# Copy the rest of the application files
COPY . .

# Build the application (optional, for React projects)
RUN pnpm run build

# Set the command to start the application
CMD ["pnpm", "start"]

# Expose the default port (optional for React)
EXPOSE 3000
