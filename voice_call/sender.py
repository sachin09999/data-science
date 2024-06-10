# server.py
import socket
import pyaudio

def start_server():
    server_ip = '192.168.254.225'  # Listen on all available interfaces
    server_port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(1)

    print(f"Server listening on {server_ip}:{server_port}")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    CHUNK = 1024
    audio_stream = pyaudio.PyAudio().open(format=pyaudio.paInt16, channels=1, rate=44100, output=True)

    while True:
        data = conn.recv(CHUNK)
        if not data:
            break
        audio_stream.write(data)

    audio_stream.stop_stream()
    audio_stream.close()
    conn.close()

if __name__ == "__main__":
    start_server()
