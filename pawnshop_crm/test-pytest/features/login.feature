Feature: Login as admin
  A sample test
  
Scenario: Login as admin
    Given Login page

#    Then Taking out superuser from db
#    Then Create superuser

    Then I logging as admin

    Then I should see admin page
#    Then Click on user model
