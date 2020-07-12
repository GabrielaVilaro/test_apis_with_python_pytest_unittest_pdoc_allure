
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

Escenario = {}


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
