# echo-websocket-server

This is a basic WebSocket server implemented using FastAPI. The server listens for WebSocket connections and, upon receiving any message, prints the connection details and returns them to the client in a JSON format.

## Features

- Accepts WebSocket connections
- Prints connection details (host, port, headers)
- Returns the connection details and received message back to the client as JSON
- Handles client disconnections gracefully

## Requirements

- Python 3.7+
- FastAPI
- `uvicorn` for running the server

## Installation

1. Clone the repository or copy the server script.
2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Running
```bash
python3 app/main.py
```