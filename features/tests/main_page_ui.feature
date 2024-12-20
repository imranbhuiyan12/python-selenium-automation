# Created by ibhui at 12/20/2024
Feature: test for main page UI


  Scenario: User can see header links
    Given Open target main page
    Then Verify header links are shown


  Scenario: user can see 6 header links
    Given Open target main page
    Then Verify 6 header links are shown
