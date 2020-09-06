Feature: Test all search options
  We want to check that each store returns results when prompted

  Background:
    Given I am on the homepage
    And Covid message pops up
    And I click on Continuar button
    And Covid popup is invisible
    When Register message pops up
    Then I click on Ya estoy registrado button
    And Register popup is invisible

  Scenario: Search with Amazon
    Given I perform a search using "Amazon"
    Then I get only "Amazon" results

  Scenario: Search with eBay
    Given I perform a search using "eBay"
    Then I get only "eBay" results

  Scenario: Search with Walmart
    Given I perform a search using "Walmart"
    Then I get only "Walmart" results