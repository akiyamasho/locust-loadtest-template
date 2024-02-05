#!/bin/bash

# check if env exists
if [ ! -d "env" ]; then
    echo "Virtual env does not exist. Creating virtual environment..."
    python -m venv env
    source env/bin/activate
    pip install -r requirements.txt
    echo "Virtual environment created and activated."
else
    echo "Virtual env exists. Activating virtual environment..."
    source env/bin/activate
    echo "Virtual environment activated."
fi

locust -f src/main.py