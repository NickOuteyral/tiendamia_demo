Feature: Test covid and register popups in homepage
  We want to check that the covid and register popups shows in the homepage
  These are supposed to show up when the user opens the site

  Scenario: Homepage covid message pops up
    Given I am on the homepage
    Then Covid message pops up

  Scenario: Homepage register message pops up
    Given I am on the homepage
    And Covid message pops up
    And I click on Continuar button
    And Covid popup is invisible
    When Register message pops up
    Then I click on Ya estoy registrado button
    And Register popup is invisible

