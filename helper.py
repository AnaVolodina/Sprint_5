from faker import Faker

# Генерируем случайный логин(email)
fake = Faker()

def generate_fake_email():
    return fake.email()
