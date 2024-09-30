Feature: Persist the maximum temperature input


  Scenario: rejects an invalid record
    Given an invalid input record
    When persisting the maximum temperature
    Then it rejects the input as not valid
