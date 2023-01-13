import requests, json

class getNada:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US;q=0.7,en;q=0.3"
        }
        self.getDomains()


    def getDomains(self):
        r = requests.get('https://getnada.com/api/v1/domains',headers=self.headers)
        response_json = json.loads(r.text)
        self.domains = []
        for dom in response_json:
            self.domains.append(dom['name'])
        return self.domains

    def checkInbox(self,email,delete=True):
        email_name, domain_name = email.split('@')
        assert domain_name in self.domains, f'Error entered domain {domain_name} not in available {self.domains}'
        r = requests.get(f'https://getnada.com/api/v1/inboxes/{email}',headers=self.headers)
        print(r.text)
        json_data = json.loads(r.text)
        print(json_data['msgs'])
        if json_data['msgs'] == []:
            return []
        else:
            msgs = []
            for m in json_data['msgs']:
                # get content of email.
                uid = m['uid']
                r2 = requests.get(f'https://getnada.com/api/v1/messages/html/{uid}',headers=self.headers)
                message_status_code = r2.status_code
                message_bytes = r2.content
                msgs.append(
                    {
                        'uid' : uid,
                        'from' : m['f'],
                        'subject' : m['s'],
                        'from_email' : m['fe'],
                        'receive_time_epoch' : m['r'],
                        'message_data' : {
                            'status_code' : message_status_code,
                            'message_contents': message_bytes
                        }
                    }
                )
                if delete:
                    r = requests.delete(f'https://getnada.com/api/v1/messages/{uid}',headers=self.headers)
        return msgs

if __name__ == "__main__":
    gn = getNada()
    # get acceptable domains:
    domains = gn.domains
    email_name = 'whateveryouwant'
    domain = 'getnada.com'
    print(gn.checkInbox(email=f'{email_name}@{domain}',delete=True))