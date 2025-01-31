import smtplib

email = "ommdevgoswami01@gmail.com"
password = "xozz sqdf dpvy lxqs"

with smtplib.SMTP("smtp.gmail.com", port=587) as testingMail:
    testingMail.starttls()
    testingMail.login(email, password)
    testingMail.sendmail(from_addr = email, 
                        to_addrs="ommdevgoswami@yahoo.com", 
                        msg="Subject:Yo Yo testing Mail is here\n\nHello, this is a test email!"
                        )