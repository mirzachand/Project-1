
import smtplib
  
s = smtplib.SMTP('smtp.gmail.com', 587)
  
s.starttls()
  
s.login("mirzachand0307@gmail.com", "**password**")

subject = "sending email using python"
body= "This is Mirza here, I'm sending this email from python program"

message = "Subject:{}\n\n{}".format(subject,body)

ReceiverEmail = ["ironman@gmail.com", "superman@gmail.com"]

s.sendmail("mirzachand0307@gmail.com", ReceiverEmail, message)

s.quit()