from flask import Blueprint, current_app, jsonify, request
from source.business.game import GameBusiness
from source.schemas.game import GameSchema
from source.utils.response import Response
from source.schemas.validation import Validation
from source.exceptions.bad_request import BadRequestException
from source.commons import message

game_api = Blueprint('game', __name__)
game_business = GameBusiness()


@game_api.route('/', methods=['GET'], strict_slashes=False)
def find_all():
    current_app.logger.info('Get All.')
    response = game_business.find_all()
    current_app.logger.info('Get All completed successfully.')
    return jsonify(Response(200).success(response)), 200


@game_api.route('/<int:field_id>', methods=['GET'], strict_slashes=False)
def find_by_id(field_id):
    current_app.logger.info('Get By Id.')
    response = game_business.find_by_id(field_id)
    current_app.logger.info('Get By Id completed successfully.')
    return jsonify(Response(200).success(response)), 200


@game_api.route('/tournament/<int:tournament_id>', methods=['GET'], strict_slashes=False)
def find_game_by_tournament(tournament_id):
    current_app.logger.info('Get By tournament_id Id.')
    response = game_business.find_game_by_tournament(tournament_id)
    current_app.logger.info('Get By tournament_id Id completed successfully.')
    return jsonify(Response(200).success(response)), 200


@game_api.route('/<int:field_id>', methods=['PUT'], strict_slashes=False)
def update(field_id):
    current_app.logger.info('Update.')
    data = request.get_json()
    if not data:
        raise BadRequestException(None, message.BAD_REQUEST_VALIDATION)
    Validation.validate(data, GameSchema().update())
    response = game_business.update(field_id, data)
    current_app.logger.info('Update completed successfully.')
    return jsonify(Response(201).success(response)), 201


@game_api.route('/', methods=['POST'], strict_slashes=False)
def save():
    current_app.logger.info('Save.')
    data = request.get_json()
    if not data:
        raise BadRequestException(None, message.BAD_REQUEST_VALIDATION)
    Validation.validate(data, GameSchema().save())
    response = game_business.save(data)
    current_app.logger.info('Save completed successfully.')
    return jsonify(Response(201).success(response)), 201


@game_api.route('/<int:field_id>', methods=['DELETE'], strict_slashes=False)
def delete(field_id):
    current_app.logger.info('Delete.')
    response = game_business.delete(field_id)
    current_app.logger.info('Delete completed successfully.')
    return jsonify(Response(200).success(response)), 200
