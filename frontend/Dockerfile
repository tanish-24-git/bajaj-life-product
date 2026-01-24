FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

# Build for production? For MVP dev, we might just run dev server
# But prompt asked for Docker Compose deployment.
# We will use 'npm run dev' exposed on host for simplicity in MVP 
# or 'npm run preview' after build. Let's stick to dev for hot reload potential if needed, 
# or preview for stability.

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host"]
