Feature: starting the web server

    Scenario: visit the welcome page
        When we visit / in port 5000
        Then we should get Strif in the title

    Scenario: submit request
        When we visit / in port 5000
        And we set start date to 2015-12-20
        And we set end date to 2015-12-29
        And we add place Athens
        And we add place London
        And we add place Belgium
        And we submit the form
        Then we should get Strif in the title

