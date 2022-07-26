from connectors.core.connector import Connector, get_logger, ConnectorError
from .operations import *

logger = get_logger('discord-webhook')


class DiscordWebhook(Connector):
    def execute(self, config, operation, params, **kwargs):
        logger.info('In execute() Operation: {}'.format(operation))
        try:
            operation = operations.get(operation)
            return operation(config, params)
        except Exception as err:
            logger.error('{}'.format(err))
            raise ConnectorError('{}'.format(err))