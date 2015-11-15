from flask import Flask
from web import controllers


def main():
    app = Flask('web-service')
    controllers.WelcomeController(app).setup_routes()
    app.run(host='0.0.0.0')

if __name__ == '__main__':
    main()
