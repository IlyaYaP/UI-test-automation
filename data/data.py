from faker import Faker

fake = Faker()


class RegistrationData():
    sing_up_successful_message = 'Sign up successful.'
    username = fake.user_name()
    password = fake.password()


class ContactMessageData():
    contact_message = 'Thanks for the message!!'
    email = fake.ascii_free_email()
    name = fake.name()
    message = fake.company()


