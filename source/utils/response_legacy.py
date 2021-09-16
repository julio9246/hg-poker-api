class Response:

    @staticmethod
    def error(message='', data=None):
        return {
            'success': False,
            'message': message,
            'records': data
        }

    @staticmethod
    def success(message='', data=None):
        return {
            'success': True,
            'message': message,
            'records': data
        }
