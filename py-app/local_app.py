import logging.config

logging.config.fileConfig('config/logging.config')
logger = logging.getLogger(__name__)

import chatbackend_app.app as backend
import chatui_app.app as ui

import logging.config

from cltl.combot.infra.event.memory import SynchronousEventBus

logging.config.fileConfig('config/logging.config')

from cltl.combot.infra.config.local import load_configuration, LocalConfigurationManager
from cltl.combot.infra.resource.threaded import ThreadedResourceManager


if __name__ == '__main__':
    configs=["../../cltl-chat-ui/config/default.config", "../../cltl-chat-backend/config/default.config"]
    config = load_configuration(None, configs)

    infra = [SynchronousEventBus(), ThreadedResourceManager(), LocalConfigurationManager(config)]

    logger.info("Initialized Application with local event bus")
    backend.Application(backend.ApplicationContainer(*infra)).run()
    ui.Application(ui.ApplicationContainer(*infra)).run()