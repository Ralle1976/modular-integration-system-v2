class IntegrationErrorHandler:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self._setup_logging()
...