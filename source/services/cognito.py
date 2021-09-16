from source.exceptions.bad_request import BadRequestException
from source.exceptions.conflict import ConflictException
from source.exceptions.not_found import NotFoundException
from source.exceptions.unauthorized import UnauthorizedException

import boto3
import source.commons.message as message


class CognitoBusiness:

    def __init__(self):
        self.client = boto3.client('cognito-idp')

    def get_user(self, data):
        try:
            response = self.client.get_user(
                AccessToken=str(data['access_token'])
            )
            return {
                'email': response['UserAttributes'][6]['Value']
            }
        except self.client.exceptions.NotAuthorizedException:
            raise UnauthorizedException('Token expirado')
        except self.client.exceptions.UserNotFoundException:
            raise NotFoundException(None, message.USER_NOT_FOUND)
        except self.client.exceptions.UserNotConfirmedException:
            raise UnauthorizedException(message.USER_NOT_CONFIRMED)
