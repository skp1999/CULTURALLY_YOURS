## Culturally Yours Backend

Backend service to capture Cultural Spans from URL.



### Prerequisites

- Python 3.7+
- MongoDB (for production)
- Azure OpenAI API access key


## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/gateway` | POST | Main analysis endpoint for text processing |
| `/chrome-api` | POST | Dedicated endpoint for Chrome extension |
| `/login` | POST | User authentication |
| `/register` | POST | New user registration |
| `/live` | GET | Health check endpoint |




- **Development**: Quick setup with minimal configuration
- **Production**: Full features with MongoDB logging and data persistence


