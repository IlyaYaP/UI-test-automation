from faker import Faker


fake = Faker()

class RegistrationData():
    # username = fake.user_name()
    # password = fake.password()
    username = 'ui_test_user'
    password = 'ui_test_password'
    sing_up_successful_message = 'Sign up successful.'
