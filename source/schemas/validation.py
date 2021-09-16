from cerberus import Validator
from source.exceptions.unprocessable_entity import UnprocessableEntityException

import source.commons.message as message


class Validation:

    @staticmethod
    def validate(data, schema):
        validator = Validator()
        validator.validate(data, schema)
        if validator.errors:
            raise UnprocessableEntityException(validator.errors, message.VALIDATION_ERROR)
