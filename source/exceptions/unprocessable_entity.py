class UnprocessableEntityException(Exception):

    def __init__(self, errors, message):
        Exception.__init__(self)
        self._code = 422
        self._errors = errors
        self._message = message

    @property
    def code(self):
        return self._code

    @property
    def errors(self):
        return self._errors

    @property
    def message(self):
        return self._message
