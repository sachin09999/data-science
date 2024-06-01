#port limit 0-6.5.5.3
#192.168.180.225
#port 8888
import socket
try:
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # r=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    ip_address1="192.168.180.72" #receiver ip address
    ip_address2="192.168.180.35"
    PORT=8080
    Target1=(ip_address1,PORT)
    Target2=(ip_address2,PORT)
    message=input("what meassage do you want to send ")
    message.encode('ascii')
    encrypt_message=message.encode('ascii')
    s.sendto(encrypt_message,Target1)
    s.sendto(encrypt_message,Target2)

except Exception as e:
    print("Failed")    

else:
    print("meassage sent 😊😊😊")        