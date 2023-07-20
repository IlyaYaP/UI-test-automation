from faker import Faker



class RegistrationData():
    sing_up_successful_message = 'Sign up successful.'

    fake = Faker()
    username = fake.user_name()
    password = fake.password()

    # def fake_user_data():
    #     fake = Faker()
    #     user_data = []
    #     fake_user_data = [fake.user_name(), fake.password()]
    #     user_data.extend(fake_user_data)
    #     return user_data