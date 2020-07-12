@Integration
Feature: Test WebApi

  @WebApi
  Scenario: GET pet data
    Given I connect with endpoint pet/Escenario:pet
    When I do a Get
    Then I print out the results of the response