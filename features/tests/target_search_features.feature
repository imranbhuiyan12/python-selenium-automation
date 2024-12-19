# Created by ibhuiyan at 12/19/2024
Feature: Tests for search

  Scenario: User can search for a product
    Given Open target main page
    When Search for tea
    Then Verify search results shown


Scenario: “Your cart is empty” message is shown
  Given Open target main page
  When Click on Cart Icon
  Then Verify “Your cart is empty” message is shown

Scenario: Sign In form opened
  Given Open target main page
  Then Click sign in button
  When Nav bar sign button
  Then Verify Sign In form opened

