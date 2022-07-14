import smtplib

s = smtplib.SMTP("smtp.gmail.com",587) # need to initialize google standard port
s.starttls() #Transport layer security to encrypt the SMTP commands
s.login("apmdcsilica02@gmail.com","silicanlr2") # need to login with sender credentials
message = "Hi, I sent this mail by coding python" # message to be delivered
s.sendmail("apmdcsilica02@gmail.com","deppblack@gmail.com",message) # sender & receiver details with message
s.quit() # quit the session