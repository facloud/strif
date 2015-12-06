from behave import given, when, then
import sure  # TODO(gl): disable W0611 for sure
from selenium import webdriver


@when('we visit {path} in port {port:d}')
def step_impl(context, path, port):
    context.browser.get("http://0.0.0.0:{}/{}".format(port, path))


@when('we set start date to {startDate}')
def step_impl(context, startDate):
    inputElement = context.browser.find_element_by_name("startDate")
    inputElement.send_keys(startDate)


@when('we set end date to {endDate}')
def step_impl(context, endDate):
    inputElement = context.browser.find_element_by_name("endDate")
    inputElement.send_keys(endDate)


@when('we add place {place}')
def step_impl(context, place):
    inputElement = context.browser.find_element_by_name("placesList")
    inputElement.send_keys(place + '\n')


@when('we submit the form')
def step_impl(context):
    inputElement = context.browser.find_element_by_name("placesList")
    inputElement.submit()


@then('we should get Strif in the title')
def step_impl(context):
    context.browser.title.should.be.equal("Strif")
