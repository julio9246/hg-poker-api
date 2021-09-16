from flask import g
from source.exceptions.unauthorized import UnauthorizedException
from source.helpers.cognito import CognitoHelper
import source.commons.environment as environment
from flask import request
import requests
from source.utils import utils

class Authorization:

    def __init__(self):
        self.cognito_helper = CognitoHelper()
        self.authorization_token = utils.get_authorization_code()
