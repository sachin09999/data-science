import socket, cv2, pickle, struct
import pyaudio

# Socket Create
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# host_name = socket.gethostname()
# host_ip = socket.gethostbyname(host_name)
port = 9999
socket_address = ('192.168.254.225', port)

# Socket Bind
server_socket.bind(socket_address)

# Socket Listen
server_socket.listen(5)
print("LISTENING AT:", socket_address)

conn, addr = server_socket.accept()
CHUNK = 1024
audio_stream = pyaudio.PyAudio().open(format=pyaudio.paInt16, channels=1, rate=44100, output=True)

# Socket Accept
while True:
    data = conn.recv(CHUNK)
    audio_stream.write(data)
    client_socket, addr = server_socket.accept()
    print('GOT CONNECTION FROM:', addr)
    if client_socket:
        vid = cv2.VideoCapture(0)

        while (vid.isOpened()):
            img, frame = vid.read()
            a = pickle.dumps(frame)
            message = struct.pack("Q", len(a)) + a
            client_socket.sendall(message)

            cv2.imshow('TRANSMITTING VIDEO', frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                client_socket.close()
