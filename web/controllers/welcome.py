import flask


class WelcomeController:
    def __init__(self, app):
        self.app = app

    def setup_routes(self):
        self.app.add_url_rule('/', view_func=self.handle_welcome)
        return self.app

    def handle_welcome(self):
        return flask.render_template('welcome.html')
