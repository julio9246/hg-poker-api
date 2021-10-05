from flask import Blueprint, current_app, jsonify, request
from source.business.player_tournament import PlayerTournamentBusiness
from source.schemas.player_tournament import PlayerTournamentSchema
from source.utils.response import Response
from source.schemas.validation import Validation
from source.exceptions.bad_request import BadRequestException
from source.commons import message

player_tournament_api = Blueprint('player-tournament', __name__)
player_tournament_business = PlayerTournamentBusiness()


@player_tournament_api.route('/', methods=['GET'], strict_slashes=False)
def find_all():
    current_app.logger.info('Get All.')
    response = player_tournament_business.find_all()
    current_app.logger.info('Get All completed successfully.')
    return jsonify(Response(200).success(response)), 200


@player_tournament_api.route('/<int:field_id>', methods=['GET'], strict_slashes=False)
def find_by_id(field_id):
    current_app.logger.info('Get By Id.')
    response = player_tournament_business.find_by_id(field_id)
    current_app.logger.info('Get By Id completed successfully.')
    return jsonify(Response(200).success(response)), 200


@player_tournament_api.route('/ranking/<int:tournament_id>', methods=['GET'], strict_slashes=False)
def get_ranking(tournament_id):
    current_app.logger.info('Get Player Game By GameId.')
    response = player_tournament_business.get_ranking(tournament_id)
    current_app.logger.info('Get Players Game By GameId completed successfully.')
    return jsonify(Response(200).success(response)), 200


@player_tournament_api.route('/player-information/', methods=['POST'], strict_slashes=False)
def get_player_tournament():
    data = request.get_json()
    response = player_tournament_business.get_player_tournament(data)
    return jsonify(Response(200).success(response)), 200


@player_tournament_api.route('/<int:field_id>', methods=['PUT'], strict_slashes=False)
def update(field_id):
    current_app.logger.info('Update.')
    data = request.get_json()
    if not data:
        raise BadRequestException(None, message.BAD_REQUEST_VALIDATION)
    Validation.validate(data, PlayerTournamentSchema().update())
    response = player_tournament_business.update(field_id, data)
    current_app.logger.info('Update completed successfully.')
    return jsonify(Response(201).success(response)), 201


@player_tournament_api.route('/', methods=['POST'], strict_slashes=False)
def save():
    current_app.logger.info('Save.')
    data = request.get_json()
    if not data:
        raise BadRequestException(None, message.BAD_REQUEST_VALIDATION)
    Validation.validate(data, PlayerTournamentSchema().save())
    response = player_tournament_business.save(data)
    current_app.logger.info('Save completed successfully.')
    return jsonify(Response(201).success(response)), 201


@player_tournament_api.route('/<int:field_id>', methods=['DELETE'], strict_slashes=False)
def delete(field_id):
    current_app.logger.info('Delete.')
    response = player_tournament_business.delete(field_id)
    current_app.logger.info('Delete completed successfully.')
    return jsonify(Response(200).success(response)), 200
