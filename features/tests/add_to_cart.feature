
Feature: Target’s product into the cart


  Scenario: adding product into cart
    Given Open target main page
    When Search for tea
    Then Add product to the cart
    Then Product name on sidebar
    Then confirm with continue button
    When Verify cart has 1 item







