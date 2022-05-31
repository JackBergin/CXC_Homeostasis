
# import python poplib module
import poplib
# input email address, password and pop3 server domain or ip address
email = input('Email: ')
password = input('Password: ')
pop3_server = input('POP3 server: ')
# connect to pop3 server:
server = poplib.POP3(pop3_server)
# open debug switch to print debug information between client and pop3 server.
server.set_debuglevel(1)
# get pop3 server welcome message.
pop3_server_welcome_msg = server.getwelcome().decode('utf-8')
# print out the pop3 server welcome message.
print(server.getwelcome().decode('utf-8'))
# user account authentication
server.user(email)
server.pass_(password)
# stat() function return email count and occupied disk size
print('Messages: %s. Size: %s' % server.stat())
# list() function return all email list
resp, mails, octets = server.list()
print(mails)
# retrieve the newest email index number
index = len(mails)
# server.retr function can get the contents of the email with index variable value index number.
resp, lines, octets = server.retr(index)
# lines stores each line of the original text of the message
# so that you can get the original text of the entire message use the join function and lines variable. 
msg_content = b'\r\n'.join(lines).decode('utf-8')
# now parse out the email object.
msg = Parser().parsestr(msg_content)
# get email from, to, subject attribute value.
email_from = msg.get('From')
email_to = msg.get('To')
email_subject = msg.get('Subject')
print('From ' + email_from)
print('To ' + email_to)
print('Subject ' + email_subject)
# delete the email from pop3 server directly by email index.
# server.dele(index)
# close pop3 server connection.
server.quit()