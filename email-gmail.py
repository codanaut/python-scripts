import smtplib
 
def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
    return problems

name = "Shaggy"
phone = "555-555-5555"
issue = "All my shit is broken!"

sendemail(from_addr = 'your gmail email', 
          to_addr_list = ['who its to @ email.com'],
          cc_addr_list = [''], 
          subject = 'Contact Us - ' + name, 
          message = name + '\n' + phone + '\n' + issue, 
          login = 'your gmail account', 
          password = 'your password')