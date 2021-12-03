from flask import g
from source.exceptions.unauthorized import UnauthorizedException
from source.helpers.cognito import CognitoHelper
import source.commons.environment as environment
from flask import request
import source.commons.message as message
import requests
from source.utils import utils

class Authorization:

    def __init__(self):
        self.cognito_helper = CognitoHelper()

    def authorize(self, access_token):
        if not access_token:
            raise UnauthorizedException(None, message.TOKEN_NOT_FOUND)
        if access_token != 'QUALQUERCOISA':
            raise UnauthorizedException(None, message.TOKEN_NOT_FOUND)

