# client.py
import socket
import pyaudio

def start_client():
    server_ip = '192.168.254.225'
    server_port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    CHUNK = 1024
    audio_stream = pyaudio.PyAudio().open(format=pyaudio.paInt16, channels=1, rate=44100, input=True)

    while True:
        data = audio_stream.read(CHUNK)
        client_socket.sendall(data)

    audio_stream.stop_stream()
    audio_stream.close()
    client_socket.close()

if __name__ == "__main__":
    start_client()
