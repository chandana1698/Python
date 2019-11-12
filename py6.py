import smtplib

fromaddr = "vaibhava2426@gmail.com"
toaddr = "ashikaramesh98@gmail.com"

msg = "Hello this is an an automted script, please ignore"

server = smtplib.SMTP("smtp.gmail.com:587")
server.starttls()
server.login(fromaddr, "vaibhava1703")
server.sendmail(fromaddr, toaddr, msg)
