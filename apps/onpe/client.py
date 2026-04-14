from core.settings import settings
import requests
from .schemas import ConsultaElectoral
from typing import Literal

headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9,es-ES;q=0.8,es;q=0.7",
    "content-type": "application/json",
    "referer": "https://resultadoelectoral.onpe.gob.pe/main/presidenciales",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Mobile Safari/537.36 Edg/146.0.0.0"
}

cookies = {
    "_ga_1QXM7GD789": "GS2.1.s1776032415$o2$g0$t1776032415$j60$l0$h130753776",
    "_clck": "wqc9cp^2^g56^0^2294",
    "_ga_S91LMCFR6G": "GS2.1.s1776039339$o1$g1$t1776039434$j60$l0$h129318824",
    "_gid": "GA1.3.1037688574.1776052372",
    "cf_clearance": "2QnTADQiWe4j2Q6EA1o6uRWy_p23mRbmZNii.brb7pA-1776052372-1.2.1.1-...",
    "_clsk": "11onvql^1776052373644^1^1^q.clarity.ms/collect",
    "_ga_7GJZHZKMC1": "GS2.1.s1776052372$o1$g0$t1776052377$j55$l0$h0",
    "_ga": "GA1.1.608236232.1776018014",
    "_ga_7X9XC2V582": "GS2.1.s1776103015$o6$g1$t1776103218$j60$l0$h391511575"
}

def get_resultados_onpe(consulta_electoral: ConsultaElectoral, mode: Literal['resumen', 'detalle']):
    params = consulta_electoral.get_params(mode)
    response = requests.get(
        consulta_electoral.get_resultados_url() if mode == 'detalle' else consulta_electoral.get_resumen_url(),
        params=params,
        headers=headers,
        cookies=cookies,
    )
    return response.json()