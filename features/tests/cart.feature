Feature: Tests for cart functionality

  Scenario: “Your cart is empty” message is shown
  Given Open target main page
  When Click on Cart Icon
  Then Verify “Your cart is empty” message is shown