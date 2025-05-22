# My First DevOps Project

This is a simple Flask web application with CI/CD pipeline using GitHub Actions and Docker.

## Project Structure

```
.
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── test_app.py        # Unit tests
├── Dockerfile         # Docker configuration
└── .github/workflows/
    └── python-ci-cd.yml  # GitHub Actions workflow
```

## Prerequisites

- Python 3.9+
- Docker
- GitHub account

## Local Development

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the application:
   ```
   python app.py
   ```
5. Open http://localhost:5000 in your browser

## Running Tests

```
python -m pytest -v test_app.py
```

## Building with Docker

1. Build the Docker image:
   ```
   docker build -t my-flask-app .
   ```
2. Run the container:
   ```
   docker run -d -p 5000:5000 my-flask-app
   ```
3. Open http://localhost:5000 in your browser

## CI/CD Pipeline

This project includes a GitHub Actions workflow that will:
1. Run tests on every push to the main branch
2. Build a Docker image
3. Test the container

## Next Steps

- Add more API endpoints
- Set up deployment to a cloud provider (AWS, GCP, Azure)
- Add monitoring and logging
- Implement blue-green or canary deployments
