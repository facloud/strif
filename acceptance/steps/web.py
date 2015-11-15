from behave import then
import sure  # TODO(gl): disable W0611 for sure
import requests


@then('we should get the welcome page in port {port:d}')
def step_impl(context, port):
    r = requests.get('http://0.0.0.0:{}/'.format(port))
    r.status_code.should.be.equal(requests.codes.ok)
    r.text.should.contain('strif')
