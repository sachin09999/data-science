import socket
try:
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    ip_address="192.168.180.225" #sender ip address
    port=8080
    target=(ip_address,port)
    s.bind(target)
    while True:
        message=s.recvfrom(120)
        data=message[0]
        print(data)
        #data="\n"
       #data.encode('ascii')
except Exception as e:
    print(e)  
else:
    print("message received")          