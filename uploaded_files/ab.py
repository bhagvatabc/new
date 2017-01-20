import smtplib
TO= 'dsaini07@gmail.com'  #'bhagvatsr@gmail.com'
Subject="hello"
message="wselcome"
gmail_sender='d2rlabs.contree@gmail.com'
gmail_password='mwjolkeglvnvlwry' #'ppbtpzlzwioxdyvx' #'letscontree123' ppbtpzlzwioxdyvx
server=smtplib.SMTP("smtp.gmail.com:587")
server.ehlo()
server.starttls()
server.login(gmail_sender,gmail_password)
BODY = '\r\n'.join([
       'TO: %s' % TO,
       'From: %s'% gmail_sender,
       'Subject: %s' % Subject,
       ' ',
       'TEXT: %s'% message
      ])
try:
 server.sendmail(gmail_sender,[TO] ,BODY)
 print 'email sent'
except:
 print 'error sending mail....'
server.quit()
