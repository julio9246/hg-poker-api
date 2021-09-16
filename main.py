from source.application import create_application
from source.commons import environment

application = create_application(environment.FLASK_ENV)

if __name__ == '__main__':
    application.run(
        debug=environment.APPLICATION_DEBUG,
        host=environment.APPLICATION_HOST,
        port=environment.APPLICATION_PORT,
    )
