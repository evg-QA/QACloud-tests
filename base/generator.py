from faker import Faker
from random import randint


class PostGenerator:
    def __init__(self):
        self.faker = Faker('en_US')
        self.userId = None
        self.title = None
        self.body = None

    def generate_random_user_id(self):
        self.userId = randint(1, 10)
        return self.userId

    def generate_random_title(self):
        self.title = self.faker.sentence()
        return self.title

    def generate_random_body(self):
        self.body = self.faker.paragraph()
        return self.body

