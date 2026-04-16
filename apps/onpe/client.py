from core.settings import settings
import requests
from .schemas import ConsultaElectoral
from typing import Literal

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,es-ES;q=0.8,es;q=0.7',
    'content-type': 'application/json',
    'priority': 'u=1, i',
    'referer': 'https://resultadoelectoral.onpe.gob.pe/main/presidenciales',
    'sec-ch-ua': '"Microsoft Edge";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0',
}

# Configuración de Cookies
cookies = {
    '_ga': 'GA1.1.2072113352.1776111711',
    '_ga_7X9XC2V582': 'GS2.1.s1776234829$o14$g1$t1776235396$j52$l0$h2033550776',
}

def get_resultados_onpe(consulta_electoral: ConsultaElectoral, mode: Literal['resumen', 'detalle', 'participacion']):
    params = consulta_electoral.get_params(mode)
    response = requests.get(
        consulta_electoral.get_resultados_url() if mode == 'detalle' else consulta_electoral.get_resumen_url() if mode == 'resumen' else consulta_electoral.get_participacion_url(),
        params=params,
        headers=headers,
        cookies=cookies,
    )
    return response.json()