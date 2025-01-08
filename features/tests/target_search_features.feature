
Feature: Tests for search

  Scenario: User can search for a product
    Given Open target main page
    When Search for tea
    Then Verify search results shown tea


  Scenario: User can search for a coffee
    Given Open target main page
    When Search for coffee
    Then Verify search results shown coffee

Scenario: User can search for a mug
    Given Open target main page
    When Search for mug
    Then Verify search results shown mug


Scenario: Sign In form opened
  Given Open target main page
  Then Click sign in button
  When Nav bar sign button
  Then Verify Sign In form opened

#  Scenario Outline: User can search for a product
#    Given Open target main page
#    When Search for <product>
#    Then Verify search results shown  <product>
#    Examples:
#    |product    |
#    |coffee     |
#    |tea        |
#    |mug        |



  Scenario: “Your cart is empty” message is shown
  Given Open target main page
  When Click on Cart Icon
  Then Verify “Your cart is empty” message is shown




  Scenario:  Select colors
    Given Open target page A-54551690
    Then Verify that color selected by user





  Scenario:  Create a test case
    Given  Open target main page
    Then   Search for product iphone
    Then   Verify product name and image


