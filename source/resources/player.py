from flask import Blueprint, current_app, jsonify, request
from source.business.player import PlayerBusiness
from source.utils.response import Response
from source.schemas.player import PlayerSchema
from source.schemas.validation import Validation
from source.exceptions.bad_request import BadRequestException
from source.commons import message

player_api = Blueprint('player', __name__)
player_business = PlayerBusiness()


@player_api.route('/', methods=['GET'], strict_slashes=False)
def find_all():
    current_app.logger.info('Get All Player.')
    response = player_business.find_all()
    current_app.logger.info('Get Players completed successfully.')
    return jsonify(Response(200).success(response)), 200


@player_api.route('/login', methods=['POST'], strict_slashes=False)
def login():
    current_app.logger.info('Get Login.')
    data = request.get_json()
    response = player_business.login(data)
    current_app.logger.info('Get Login completed successfully.')
    return jsonify(Response(200).success(response)), 200


@player_api.route('/<int:player_id>', methods=['GET'], strict_slashes=False)
def find_by_id(player_id):
    current_app.logger.info('Get Player By Id.')
    response = player_business.find_by_id(player_id)
    current_app.logger.info('Get Players By Id completed successfully.')
    return jsonify(Response(200).success(response)), 200


@player_api.route('/find-by-email/<string:email>', methods=['GET'], strict_slashes=False)
def find_by_email(email):
    response = player_business.find_by_email(email)
    return jsonify(Response(200).success(response)), 200


@player_api.route('/find-by-nick_name/<string:nick_name>', methods=['GET'], strict_slashes=False)
def find_by_nick_name(nick_name):
    response = player_business.find_by_nick_name(nick_name)
    return jsonify(Response(200).success(response)), 200


@player_api.route('/<int:player_id>', methods=['PUT'], strict_slashes=False)
def update(player_id):
    current_app.logger.info('Update Player.')
    data = request.get_json()
    if not data:
        raise BadRequestException(None, message.BAD_REQUEST_VALIDATION)
    Validation.validate(data, PlayerSchema.update())
    response = player_business.update(player_id, data)
    current_app.logger.info('Update Player completed successfully.')
    return jsonify(Response(201).success(response)), 201


@player_api.route('/', methods=['POST'], strict_slashes=False)
def save():
    current_app.logger.info('Save Player.')
    data = request.get_json()
    if not data:
        raise BadRequestException(None, message.BAD_REQUEST_VALIDATION)
    Validation.validate(data, PlayerSchema.save())
    response = player_business.save(data)
    current_app.logger.info('Save Player completed successfully.')
    if response.get('error'):
        return jsonify(Response(204).success(response)), 204
    return jsonify(Response(201).success(response)), 201


@player_api.route('/<int:player_id>', methods=['DELETE'], strict_slashes=False)
def delete(player_id):
    current_app.logger.info('Delete Customer Type.')
    response = player_business.delete(player_id)
    current_app.logger.info('Delete Customer Type completed successfully.')
    return jsonify(Response(200).success(response)), 200
