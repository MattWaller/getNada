<h1> getnada.com API for managing inbox</h1>

<p>
This is an unoffical api utilizing API GET / DELETE CALLS FROM https://getnada.com

</p>

<h2>
Guide:
</h2>

<p>
git clone https://github.com/MattWaller/getNada.git
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
</p>

<p>

Example:
gn = getNada()
<!--get acceptable domains: -->
domains = gn.domains
email_name = 'whateveryouwant'
domain = 'getnada.com'
print(gn.checkInbox(email=f'{email_name}@{domain}',delete=True))
</p>

<p>
Response:

[{'uid': '8xST2y9lF2WoVV2cHbIZ5AEl1kTPrN', 'from': 'SAMPLE FROM', 'subject': 'SAMPLE', 'from_email': 'example@example.com', 'receive_time_epoch': 1673579903, 'message_data': {'status_code': 200, 'message_contents': b'<!doctype html> <html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office"> SAMPLE EMAIL.</body> </html> \n'}}]

</p>

<p>
Functions:
<ul>
<ol>
getDomains(): initates / calls getnada's api and retrives acceptable domains for throwaway. 
This function is automatically called in the class.
To get a list of the acceptable domains you can call {classVariable}.domains
</ol>
<ol>
checkInbox(email,delete)
email is type string: look to use an email such as "example@getnada.com"
delete is Boolean, and will delete the email in inbox, defaults to True.
So if you're testing set it to False, if you want to make sure you change it to False if you want to keep the email in inbox.
</ol>
</p>