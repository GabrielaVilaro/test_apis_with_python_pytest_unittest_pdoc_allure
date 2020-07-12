
import objectpath as objectpath
import pytest
from functions.Inicializar import Inicializar
import json
import requests
import re
import time
import datetime
import random
import string


class Functions(Inicializar):

    def ReplaceWithContextValues(self, text):
        PatronDeBusqueda = r"(?<=Escenario:)\w+"
        #r"(?<=Escenario:)\w+"
        variables = re.findall(str(PatronDeBusqueda), text, re.IGNORECASE)
        self.N = 0
        for variable in variables:
            if variable == 'today':
                dateToday = str(datetime.date.today().strftime("%Y-%m-%d"))
                text = re.sub('(Escenario:)'+ variable, dateToday, text, re.IGNORECASE)
                continue
            text = re.sub('(Escenario:)'+ variable, Inicializar.Scenary[variable], text, re.IGNORECASE)
        return text

    def get_full_host(self, _PartHost):
        _RegexPartHost = str(Functions.ReplaceWithContextValues(self, _PartHost))
        self._endpoint = Inicializar.API_hostAddressBase + _RegexPartHost
        print(self._endpoint)
        return self._endpoint

    def do_a_get(self):
        new_header = Inicializar.API_headers
        self._response = requests.get(self._endpoint, headers=new_header)
        return self._response

    def print_api_response(self):
        self.json_response = json.loads(self._response.text)
        print(json.dumps(self.json_response, indent=3))
