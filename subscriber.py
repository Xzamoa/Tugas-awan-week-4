import zmq
import sys

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")

topic = sys.argv[1]  # input topic (NIM)
socket.setsockopt_string(zmq.SUBSCRIBE, topic)

print(f"Subscribed to topic: {topic}")

while True:
    message = socket.recv_string()
    print("Received:", message)
