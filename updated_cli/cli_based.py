import socket

# Try connecting to the target machine
try:
    # Create a TCP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Target IP address (verify it's reachable)
    ip_address = "192.168.180.225"

    # Port number (ensure a server listens on this port)
    PORT = 8080
    Target = (ip_address, PORT)

    # Read the content of the text file
    with open("hello.txt", "r") as file:
        file_content = file.read()

    # Send the content to the target machine
    s.connect(Target)
    s.sendall(file_content.encode("utf-8"))

except Exception as e:
    print("Failed to connect:", e)

else:
    print("Text file sent successfully! ")
    # Close the socket (important)
    s.close()
