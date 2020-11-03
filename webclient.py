import os
import urllib3
import logging
import json

country_server_url = os.environ.get('COUNTRY_SERVER_URL')
country_server_token = os.environ.get('COUNTRY_SERVER_TOKEN')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

http = urllib3.PoolManager()


def get_country_from_ip(ip):
    headers = {'charset': "UTF-8"}
    url = '{}/{}?access_key={}&format=1'

    country = "Unknown Country"
    try:
        response = http.request('GET',
                                url.format(country_server_url, ip, country_server_token),
                                headers=headers,
                                timeout=15,
                                retries=False)

        result = json.loads(response.data.decode('utf-8'))

        country = result['country_name'].upper()

    except Exception as inst:
        print(inst)
        logger.error(inst.args)

    return country
