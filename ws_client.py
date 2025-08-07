import websocket
import json

def send_landmarks(data):
    ws = websocket.WebSocket()
    ws.connect("ws://<YOUR-PC-IP>:8000")
    ws.send(json.dumps(data))
    ws.close()
