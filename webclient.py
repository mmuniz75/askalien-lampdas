import os
import urllib3
import logging
import json

wa_server_url = os.environ.get('WA_SERVER_URL')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

http = urllib3.PoolManager()


def get_country_from_ip(ip):
    return "casa"


def get_country_from_ip2(ip):
    headers = {'phone': "teste"}
    url = wa_server_url + '/{}/members'

    result = []
    try:
        response = http.request('GET',
                                url.format("group"),
                                headers=headers,
                                timeout=15,
                                retries=False)

        result = json.loads(response.data.decode('utf-8'))

    except Exception as inst:
        print(inst)
        logger.error(inst.args)

    return result
