
class RecepeBook(object):
    
    def __init__(self, app_name, logger):
        self._logger = logger
        self._app_name = app_name


    def get_app_name(self):
        return self._app_name

    def start(self):
        """
        Start the application
        """
        pass


    def stop(self):
        """
        Stop the application
        """
        pass