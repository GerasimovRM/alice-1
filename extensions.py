class SessionStorage:
    def __init__(self):
        self._sessionStorage = {}

    def get_session(self):
        return self._sessionStorage