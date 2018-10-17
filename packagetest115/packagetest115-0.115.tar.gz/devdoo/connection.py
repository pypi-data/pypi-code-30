#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from data_response import DataResponse

# --------------------------------
# Connection
# --------------------------------
'''
A classe Connection realiza conexão com servidor de serviço API
'''


class Connection:
    # --------------------------------
    # __init__
    # --------------------------------
    def __init__(self, status):
        self.status = status

    # --------------------------------
    # load_config
    # --------------------------------
    '''
    Conecta o servidor de serviços API e recupera documentos
    '''

    def load_config(self, service_id):
        # url = 'http://10.1.0.90:9500/console/config'
        #url = 'http://localhost:9500/console/config'
        url = 'http://mdb-master.soocializer.com.br:9500/console/config'
        params = dict(
            service=service_id
        )
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
            'devdoo-api-key': '286c42a2b9dabb536c87b1a88a6842117bfb37ab',
            'devdoo-app-id': '507f191e810c19729de860ea',
            'devdoo-credentials': 'NTA3ZjE5MWU4MTBjMTk3MjlkZTg2MGVhOjhmNGY5ZjJkY2JhZjliZDhlZTllNGQxYTJjYjk3MWEwNDA4NDE1N2I='
        }
        data_response = requests.get(url, params=params, headers=headers)

        if type(data_response) == requests.models.Response:
            return DataResponse(data_response.json(), self.status)
        else:
            self.status.error("ERROR_CONNECTION", None, ["Falha na conexao com servidor de servicos API", service_id])
