#!/bin/bash

# Configuration variables
PROJECT_ID="python-transformer"
SERVICE_NAME="aiapi"
REGION="europe-west1"
IMAGE_NAME="myfastapiapp"

# Build the Docker image
docker build -t gcr.io/$PROJECT_ID/$IMAGE_NAME .

# Authenticate with GCP
gcloud auth configure-docker

# Push the Docker image to Google Container Registry
docker push gcr.io/$PROJECT_ID/$IMAGE_NAME

# Deploy to Google Cloud Run
gcloud run deploy $SERVICE_NAME \
    --image gcr.io/$PROJECT_ID/$IMAGE_NAME \
    --platform managed \
    --region $REGION \
    --allow-unauthenticated

