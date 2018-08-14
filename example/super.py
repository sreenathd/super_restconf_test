import requests
import os

class RestCalls():

    def __init__(self, ip_address, port=80, username=None, password=None):
        self.BasePath = '/restconf/data/running/openconfig-'
        self.Accept = [
            'application/yang.data+{fmt}',
            'application/yang.errors+{fmt}',
        ]
        self.ContentType = 'application/yang.data+{fmt}'
        session = requests.Session()
        self.Format = 'json'
        if username is not None and password is not None:
            session.auth = (username, password)
        session.verify = False
        session.headers.update({
            'Accept': ','.join([
                accept.format(fmt=self.Format) for accept in self.Accept
            ]),
            'Content-Type': self.ContentType.format(fmt=self.Format),
        })
        self._session = session
        self._host = '{scheme}://{ip}:{port}{basePath}/'.format(
            scheme='http',
            ip=ip_address,
            port=port,
            basePath=self.BasePath
        )

    def put(self, data, endpoint):
        url = self._host + endpoint
        res = self._session.put(url, data=data)
        return res

    def post(self, data, endpoint):
        url = self._host + endpoint
        res = self._session.post(url, data=data)
        return res

    def patch(self, data, endpoint):
        url = self._host + endpoint
        res = self._session.patch(url, data=data)
        return res

    def get(self, endpoint='', **kwargs):
        url = self._host + endpoint
        print(url)
        if 'content' not in kwargs:
            kwargs = {'content': 'config'}
        print(url)
        res = self._session.get(url, params=kwargs)
        return res

    def delete(self, endpoint):
        url = self._host + endpoint
        res = self._session.delete(url)
        return res
        
 class SuperMicro():
     def __init__(self, ip_address, port=80, username=None, password=None):
         self.switch =  RestCalls()
     def get_hostname():
          self.switch.get('system:sytem/config')
