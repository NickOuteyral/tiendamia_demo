Feature: Test covid and register popup in homepage
  We want to check that the covid and register popup shows in the homepage
  These are supposed to show up when the user opens the site

  Scenario: Homepage covid message pops up
    Given I am on the homepage
    When I wait for popup with id "lightbox_covid"
    Then Message with id "lightbox_covid" pops up

  Scenario: Homepage register message pops up
    Given I am on the homepage
    Given I wait for popup with id "lightbox_covid"
    Given Message with id "lightbox_covid" pops up
    Given I click on element with text "Continuar"
    When I wait for popup with id "registration-home-popup3"
    Then Message with id "registration-home-popup3" pops up
    Then I click on element with text "Ya estoy registrado"

