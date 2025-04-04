# SocialEase Backend

This is the backend API for the SocialEase application, providing endpoints for progress tracking, notifications, and user settings.

## Features

- User progress tracking
- Notification management
- User settings

## Deployment

This application is configured for deployment on Render. See the [deployment_guide.md](deployment_guide.md) for detailed instructions.

## Running Locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up environment variables:
   Create a `.env` file with:
   ```
   MONGODB_URI=your_mongodb_connection_string
   PORT=8000
   ```

3. Run the application:
   ```bash
   cd backendkabi-main/socialease_backend
   uvicorn main:app --reload
   ```

4. Open [http://localhost:8000/docs](http://localhost:8000/docs) to view the API documentation.