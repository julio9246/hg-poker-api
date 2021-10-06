from flask import Blueprint, current_app, jsonify, request
from source.business.player_game import PlayerGameBusiness
from source.schemas.player_game import PlayerGameSchema
from source.utils.response import Response
from source.schemas.validation import Validation
from source.exceptions.bad_request import BadRequestException
from source.commons import message

player_game_api = Blueprint('player-game', __name__)
player_game_business = PlayerGameBusiness()


@player_game_api.route('/', methods=['GET'], strict_slashes=False)
def find_all():
    current_app.logger.info('Get All.')
    response = player_game_business.find_all()
    current_app.logger.info('Get All completed successfully.')
    return jsonify(Response(200).success(response)), 200


@player_game_api.route('/<int:field_id>', methods=['GET'], strict_slashes=False)
def find_by_id(field_id):
    current_app.logger.info('Get By Id.')
    response = player_game_business.find_by_id(field_id)
    current_app.logger.info('Get By Id completed successfully.')
    return jsonify(Response(200).success(response)), 200


@player_game_api.route('/report', methods=['POST'], strict_slashes=False)
def get_player_game_report():
    data = request.get_json()
    response = player_game_business.get_player_game_report(data)
    return jsonify(Response(200).success(response)), 200


@player_game_api.route('/<int:field_id>', methods=['PUT'], strict_slashes=False)
def update(field_id):
    current_app.logger.info('Update.')
    data = request.get_json()
    if not data:
        raise BadRequestException(None, message.BAD_REQUEST_VALIDATION)
    Validation.validate(data, PlayerGameSchema().update())
    response = player_game_business.update(field_id, data)
    current_app.logger.info('Update completed successfully.')
    return jsonify(Response(201).success(response)), 201


@player_game_api.route('/', methods=['POST'], strict_slashes=False)
def save():
    current_app.logger.info('Save.')
    data = request.get_json()
    if not data:
        raise BadRequestException(None, message.BAD_REQUEST_VALIDATION)
    Validation.validate(data, PlayerGameSchema().save())
    response = player_game_business.save(data)
    current_app.logger.info('Save completed successfully.')
    return jsonify(Response(201).success(response)), 201


@player_game_api.route('/<int:field_id>', methods=['DELETE'], strict_slashes=False)
def delete(field_id):
    current_app.logger.info('Delete.')
    response = player_game_business.delete(field_id)
    current_app.logger.info('Delete completed successfully.')
    return jsonify(Response(200).success(response)), 200
