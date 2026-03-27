#!/bin/bash

# Start Ollama in the background
ollama serve &

# Wait for Ollama to be ready
echo "Waiting for Ollama to start..."
until curl -s http://localhost:11434 > /dev/null; do
    sleep 1
done
echo "Ollama is ready."

# Pull the tinyllama model
echo "Pulling tinyllama model..."
ollama pull tinyllama
echo "Model ready."

# Start the Flask app
echo "Starting Flask..."
python app.py
