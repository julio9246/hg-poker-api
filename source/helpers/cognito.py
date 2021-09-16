from source.exceptions.bad_request import BadRequestException
from source.exceptions.conflict import ConflictException
from source.exceptions.not_found import NotFoundException
from source.exceptions.unauthorized import UnauthorizedException

import boto3
import source.commons.environment as environment
import source.commons.message as message


class CognitoHelper:

    def __init__(self):
        self.client = boto3.client('cognito-idp')

    def change_password(self, access_token, previous_password, proposed_password):
        try:
            self.client.change_password(
                AccessToken=access_token,
                PreviousPassword=previous_password,
                ProposedPassword=proposed_password
            )
        except self.client.exceptions.InvalidParameterException:
            raise BadRequestException(None, message.USER_INVALID_PREVIOUS_PASSWORD)
        except self.client.exceptions.InvalidPasswordException:
            raise BadRequestException(None, message.USER_INVALID_PASSWORD)
        except self.client.exceptions.LimitExceededException:
            raise BadRequestException(None, message.USER_LIMIT_EXCEEDED)
        except self.client.exceptions.NotAuthorizedException:
            raise BadRequestException(None, message.USER_NOT_AUTHORIZED)
        except self.client.exceptions.UserNotConfirmedException:
            raise NotFoundException(None, message.USER_NOT_CONFIRMED)
        except self.client.exceptions.UserNotFoundException:
            raise NotFoundException(None, message.USER_NOT_FOUND)

    def forgot_password(self, username):
        try:
            self.client.forgot_password(
                ClientId=environment.AWS_COGNITO_CLIENT_ID,
                Username=username
            )
        except self.client.exceptions.InvalidParameterException:
            raise BadRequestException(None, message.USER_NOT_CONFIRMED)
        except self.client.exceptions.NotAuthorizedException:
            raise BadRequestException(None, message.USER_ALREADY_CONFIRMED)
        except self.client.exceptions.UserNotFoundException:
            raise NotFoundException(None, message.USER_NOT_FOUND)

    def get_user(self, access_token):
        try:
            response = self.client.get_user(
                AccessToken=access_token
            )
            return response
        except self.client.exceptions.UserNotFoundException as e:
            print('-=-=-=-=-=-=-=-=--=-=-=-==-=-=-=')
            print('Não encontrado', e)
            print('-=-=-=-=-=-=-=-=--=-=-=-==-=-=-=')
            raise NotFoundException(None, message.USER_NOT_FOUND)
        except self.client.exceptions.UserNotConfirmedException as e:
            print('-=-=-=-=-=-=-=-=--=-=-=-==-=-=-=')
            print('Não confirmado', e)
            print('-=-=-=-=-=-=-=-=--=-=-=-==-=-=-=')
            raise UnauthorizedException(None, message.USER_NOT_CONFIRMED)
        except self.client.exceptions.NotAuthorizedException as e:
            print('-=-=-=-=-=-=-=-=--=-=-=-==-=-=-=')
            print('Não autorizado', e)
            print('-=-=-=-=-=-=-=-=--=-=-=-==-=-=-=')
            raise UnauthorizedException(None, message.USER_NOT_AUTHORIZED)
        except Exception as e:
            print('-=-=-=-=-=-=-=-=--=-=-=-==-=-=-=')
            print('Error', e)
            print('-=-=-=-=-=-=-=-=--=-=-=-==-=-=-=')
            raise UnauthorizedException(None, message.USER_NOT_AUTHORIZED)

    def sign_in(self, email, password):
        try:
            response = self.client.admin_initiate_auth(
                AuthParameters={
                    'PASSWORD': password,
                    'USERNAME': email
                },
                AuthFlow=environment.AWS_COGNITO_AUTH_FLOW,
                ClientId=environment.AWS_COGNITO_CLIENT_ID,
                UserPoolId=environment.AWS_COGNITO_USER_POOL_ID
            )
            return {
                'access_token': response['AuthenticationResult']['AccessToken'],
                'expires_in': response['AuthenticationResult']['ExpiresIn'],
                'id_token': response['AuthenticationResult']['IdToken'],
                'refresh_token': response['AuthenticationResult']['RefreshToken'],
                'token_type': response['AuthenticationResult']['TokenType']
            }
        except self.client.exceptions.NotAuthorizedException:
            raise UnauthorizedException(None, message.USER_NOT_AUTHORIZED)
        except self.client.exceptions.UserNotConfirmedException:
            raise UnauthorizedException(None, message.USER_NOT_CONFIRMED)

    def sign_up(self, family_name, name, password, phone_number, username):
        try:
            self.client.sign_up(
                ClientId=environment.AWS_COGNITO_CLIENT_ID,
                Password=password,
                UserAttributes=[
                    {
                        'Name': 'name',
                        'Value': name
                    },
                    {
                        'Name': 'family_name',
                        'Value': family_name
                    },
                    {
                        'Name': 'phone_number',
                        'Value': phone_number
                    }
                ],
                Username=username,
                ValidationData=[
                    {
                        'Name': 'email',
                        'Value': username
                    }
                ]
            )
        except self.client.exceptions.InvalidParameterException:
            raise BadRequestException(None, message.USER_INVALID_PHONE)
        except self.client.exceptions.InvalidPasswordException:
            raise BadRequestException(None, message.USER_INVALID_PASSWORD)
        except self.client.exceptions.UsernameExistsException:
            raise ConflictException(None, message.USER_ALREADY_EXISTS)
