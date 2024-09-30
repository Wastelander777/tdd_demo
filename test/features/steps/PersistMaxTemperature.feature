Feature: Persist the maximum temperature input


  Scenario: rejects an invalid record
    Given an invalid input record
    When persisting the maximum temperature
    Then it rejects the input as not valid
  Scenario: reject a duplicated record
    Given an duplicated record
    When inserting a temperature
    Then it rejects the input as duplicated    
