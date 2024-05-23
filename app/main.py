from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import JSONResponse
from typing import Dict

app = FastAPI()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    client_id = f"{websocket.client.host}:{websocket.client.port}"

    print(f"New connection from: {client_id}")

    try:
        while True:
            data = await websocket.receive_text()
            connection_details = {
                "client_id": client_id,
                "host": websocket.client.host,
                "port": websocket.client.port,
                "headers": dict(websocket.headers),
                "message": data,
            }
            print("-" * 20)
            print(f"Connection details: {connection_details}")
            print("-" * 20)

            # Send the connection details back to the client as a JSON response
            await websocket.send_json(connection_details)
    except WebSocketDisconnect:
        print("-" * 20)
        print(f"Connection closed by client: {client_id}")
        print("-" * 20)
    except Exception as e:
        print(f"Error: {e}")


@app.get("/health")
async def health_check():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
