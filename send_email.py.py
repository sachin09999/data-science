import smtplib
try:
    server = smtplib.SMTP(host='SMTP.gmail.com',port=587)
    server.starttls()
    receiver_email=input("enter your email")
    sender_email="sachinrajput1362@gmail.com"
    password='qywr swkf xtzs istg'
    server.login(sender_email,password=password)
    subject=input("what is your problem")
    body=input("Tell me details")
    message=f"subject:{subject}\n\n{body}"
    server.sendmail(sender_email,receiver_email,message)
    print("Sent &%")
    server.quit()
except Exception as e:
    print(e)
