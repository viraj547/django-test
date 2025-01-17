from .models import Product
from faker import Faker
import random

def create_dynamic_product(size):
    fake = Faker()

    for i in range(0,size):
        Product.objects.create(
            category_id = 1,
            title=fake.name(),
            description =fake.text(),
            price =random.randint(1,100)
        )
