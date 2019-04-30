import requests 

class Tram():
    id = 0
    endpoint = ""
    def __init__(self, id, endpoint):
        self.id = id
        self.endpoint = endpoint
    def update_time(self, time):
        url = self.endpoint + "/tram/{}/set/time/{}".format(self.id, time)
        r = requests.get(url=url) 
        return r.text
    def update_seats(self, seats):
        url = self.endpoint + "/tram/{}/set/seats/{}".format(self.id, seats)
        r = requests.get(url=url) 
        return r.text
    
class Stop():
    id = 0
    endpoint=  ""
    def __init__(self, id, endpoint):
        self.id = id
        self.endpoint = endpoint
    def update_waiting(self, waiting):
        url = self.endpoint + "/stop/{}/set/waiting/{}".format(self.id, waiting)
        r = requests.get(url=url) 
        return r.text
    
class Line():
    id = 0
    endpoint=  ""
    def __init__(self, id, endpoint):
        self.id = id
        self.endpoint = endpoint
    def congestion(self, congestion):
        url = self.endpoint + "/line/{}/set/congestion/{}".format(self.id, int(congestion))
        r = requests.get(url=url) 
        return r.text

class Alert():
    endpoint=  ""
    def __init__(self, endpoint):
        self.endpoint = endpoint
    def show(self, alert):
        url = self.endpoint + "/alert/new/{}".format(alert)
        r = requests.get(url=url) 
        return r
    def hide(self):
        url = self.endpoint + "/alert/hide"
        r = requests.get(url=url) 
        return r