import socket

try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ip_address = "192.168.180.225"  # Server's IP address
        PORT = 8080

        # Connect to the server
        s.connect((ip_address, PORT))

        # Receive message string from server (assuming it's the text file content)
        received_content = "b"
        while True:
            chunk = s.recv(1024)
            if not chunk:
                break
            received_content += chunk

        # Write the received content to a new text file
        with open("hello.txt", "w") as file:
            file.write(received_content.decode("utf-8"))

except Exception as e:
        print("Failed:", e)

else:
        print("Text file received successfully! 😊")

