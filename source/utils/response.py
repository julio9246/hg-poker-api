class Response:

    def __init__(self, code):
        self._code = code

    @property
    def code(self):
        return self._code

    def fail(self, errors, message):
        return {
            'code': self.code,
            'errors': errors,
            'message': message
        }

    def success(self, data):
        return {
            'code': self.code,
            'data': data
        }

    def success_page(self, data, last, page, size):
        return {
            'code': self.code,
            'data': data,
            'last': last,
            'page': page,
            'size': size
        }
