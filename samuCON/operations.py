import json, requests
from connectors.core.connector import get_logger, ConnectorError

logger = get_logger('discord-webhook')

def send_message(config, params):
    url1 = config.get('webhook')
    data = {
      "content": params.get('content'),
      "username": "FortiSOAR"
    }
    result = requests.post(url1, json = data)
    return {'status': 'success','code': result.status_code}
  
operations = {
  'send_message': send_message
}