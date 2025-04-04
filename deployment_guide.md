# Deployment Guide for SocialEase Backend

## GitHub Repository Setup

1. Create a new repository on GitHub:
   - Go to [GitHub](https://github.com/) and log in
   - Click the "+" button in the top right and select "New repository"
   - Name your repository (e.g., "socialease-backend")
   - Add a description (optional)
   - Choose repository visibility (public or private)
   - Click "Create repository"

2. Initialize your local repository and push to GitHub:
   ```bash
   # Navigate to your project directory
   cd c:\Users\kabishan\Downloads\backendkabi-main

   # Initialize git repository if not already done
   git init

   # Add all files to git
   git add .

   # Commit your changes
   git commit -m "Initial commit"

   # Add the remote GitHub repository
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

   # Push to GitHub
   git push -u origin main
   ```

## Render Deployment

1. Sign up or log in to [Render](https://render.com/)

2. Click on "New +" and select "Web Service"

3. Connect to your GitHub repository:
   - Select your GitHub account
   - Find and select your repository

4. Configure the web service:
   - Give your service a name (e.g., "socialease-backend")
   - Set the environment to "Python"
   - Set the build command: `pip install -r socialease_backend/requirements.txt`
   - Set the start command: `cd socialease_backend && uvicorn main:app --host 0.0.0.0 --port $PORT`
   - Select an appropriate instance type (Free tier is good for testing)

5. Add environment variables:
   - Click on "Environment" tab
   - Add the key: `MONGODB_URI`
   - Add the value: Your MongoDB connection string
     (Example: `mongodb+srv://username:password@cluster.mongodb.net/socialease?retryWrites=true&w=majority`)

6. Click "Create Web Service"

Your application will now be built and deployed. Render will provide you with a unique URL to access your API once deployment is complete.

## Testing the Deployment

Once deployed, you can test your API endpoints using the Render-provided URL:
- Swagger UI: `https://your-render-url.onrender.com/docs`
- API endpoints: `https://your-render-url.onrender.com/api/...`

Remember to update your frontend application to use these new production API endpoints.