from flask import Flask, Response, jsonify, request, g
from flask_cors import CORS

from .configuration import configuration
from .utils.authorization import Authorization

from source.commons import constant
from source.exceptions.conflict import ConflictException
from source.exceptions.forbidden import ForbiddenException
from source.exceptions.internal_server_error import InternalServerErrorException
from source.exceptions.no_content import NoContentException
from source.exceptions.not_found import NotFoundException
from source.exceptions.unauthorized import UnauthorizedException
from source.exceptions.unprocessable_entity import UnprocessableEntityException

from source.resources.player import player_api
from source.resources.tournament import tournament_api
from source.resources.player_tournament import player_tournament_api
from source.resources.game import game_api
from source.resources.player_game import player_game_api
from source.resources.rebuy_game import rebuy_game_api

from source.utils.response import Response
from source.utils.version import version

def create_application(environment):

    application = Flask(__name__)
    application.config.from_object(configuration[environment])

    CORS(
        application,
        allow_headers=[
            'Accept',
            'Accept-Type',
            'Authorization',
            'Content-Type',
            'Origin',
            'X-CSRF-Token',
            'X-Requested-With'
        ],
        origins='*'
    )

    application.register_blueprint(player_api, url_prefix='/api/v1/player')
    application.register_blueprint(tournament_api, url_prefix='/api/v1/tournament')
    application.register_blueprint(player_tournament_api, url_prefix='/api/v1/player-tournament')
    application.register_blueprint(game_api, url_prefix='/api/v1/game')
    application.register_blueprint(player_game_api, url_prefix='/api/v1/player-game')
    application.register_blueprint(rebuy_game_api, url_prefix='/api/v1/rebuy-game')

    @application.before_request
    def before_request():
        Authorization().authorize(request.headers.get('Authorization'))

    @application.after_request
    def enable_cors(Response):
        Response.headers[
            'Access-Control-Allow-Headers'] = 'Accept, Accept-Type, Authorization, Content-Type, Origin, X-CSRF-Token, X-Requested-With'
        Response.headers['Access-Control-Allow-Methods'] = 'DELETE, GET, OPTIONS, POST, PUT'
        Response.headers['Access-Control-Allow-Origin'] = '*'
        Response.headers['Access-Control-Max-Age'] = 3600
        return Response

    @application.errorhandler(ConflictException)
    def conflict(error):
        return jsonify(Response(error.code).fail(None, error.message)), error.code

    @application.errorhandler(ForbiddenException)
    def forbidden(error):
        return jsonify(Response(error.code).fail(None, error.message)), error.code

    @application.errorhandler(InternalServerErrorException)
    def internal_server_error(error):
        return jsonify(Response(error.code).fail(None, error.message)), error.code

    @application.errorhandler(NoContentException)
    def no_content(error):
        return jsonify(Response(error.code).fail(None, error.message)), error.code

    @application.errorhandler(NotFoundException)
    def not_found(error):
        return jsonify(Response(error.code).fail(None, error.message)), error.code

    @application.errorhandler(UnauthorizedException)
    def unauthorized(error):
        return jsonify(Response(error.code).fail(None, error.message)), error.code

    @application.errorhandler(UnprocessableEntityException)
    def unprocessable_entity(error):
        return jsonify(Response(error.code).fail(error.errors, error.message)), error.code

    @application.route('/', methods=['GET'])
    def health_check():
        data = {
            'name': constant.APPLICATION_NAME,
            'version': version.__str__()
        }
        return jsonify(Response(200).success(data)), 200


    return application