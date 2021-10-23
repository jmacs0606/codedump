import smtplib
print("hi")
sender_email = "donotreply.mimifur@gmail.com"
rec_email = "jmacs0606@gmail.com"
password=input("Please enter your email password: ")
message="Test 123 Test"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
print("logged in :)")
server.sendmail(sender_email, rec_email, message)
print(str(message) + "... has been sent to " + str(rec_email))
