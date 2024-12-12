FROM node:14

# Set working directory
WORKDIR /app

# Install dependencies
COPY package.json /app
RUN npm install

# Copy application code
COPY . /app

# Expose port for the web server
EXPOSE 3000

# Start the web application
CMD ["npm", "start"]