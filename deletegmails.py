#Script to erase all unread email messages from gmail
#
#before testing this script you have to turn ON the access for less secure apps for which a direct link is followed
#https://www.google.com/settings/security/lesssecureapps

import imaplib
box = imaplib.IMAP4_SSL('imap.gmail.com', 993)
#Replace with your gmail username and password
box.login("username@gmail.com","password")
box.select('Inbox')
typ, data = box.search(None, 'UNSEEN')
for num in data[0].split():
   box.store(num, '+FLAGS', '\\Deleted')
box.expunge()
box.close()
box.logout()
