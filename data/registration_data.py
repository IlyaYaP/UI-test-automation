from faker import Faker

fake = Faker()

class RegistrationData():
    username = fake.user_name()
    password = fake.password()
