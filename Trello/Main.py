import json

import requests
class TrelloApi:
    def CreateBoard(self):
        url = "https://api.trello.com/1/boards/?name=chetan&prefs_background=green&token=ATTA17876d1dab4a6f27d85d809a9480dbf3e5c811d0f958bf5b25019b39b41e4c6707070D08&key=137bb24ec38c7eeed650fc03dcf6026f"
        # payload = ""
        # headers = {
        #     'Cookie': 'preAuthProps=s%3A654486c910c3091a69f92bf4%3AisEnterpriseAdmin%3Dfalse.CAf4RzdaA2BZfKegRiPI5X9oW7A%2F69c%2FcJ5kWkIx0EY'
        # }

        response = requests.post(url)
        res = json.loads(response.text)
        print(res)
s=TrelloApi()
s.CreateBoard()
