#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Set environment variables
export FLASK_APP=app:create_app         # or routes.py if that's your entry point
export FLASK_ENV=development    # enables debug + auto-reload

# Run Flask with external access enabled for WSL
flask run --host=0.0.0.0
