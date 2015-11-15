import unittest
from unittest.mock import MagicMock
from web import controllers
import flask
import sure


class TestWelcomeController(unittest.TestCase):
    def setUp(self):
        self.app = MagicMock()
        self.controller = controllers.WelcomeController(self.app)

    def test_handle_welcome(self):
        originalHtml = '<html><body>I am a banana!</body></html>'
        flask.render_template = MagicMock(return_value=originalHtml)

        html = self.controller.handle_welcome()
        flask.render_template.assert_called_once_with('welcome.html')

        html.should.be.equal(originalHtml)
