from random import randint

from .models import Post
from faker import Faker


def create_posts(n=10):
    fake = Faker()
    for _ in range(n):
        created = fake.date_time()
        post = Post(
            author=fake.text(randint(10, 30)),
            title=fake.text(randint(10, 30)),
            published=fake.boolean(),
            content=fake.text(randint(100, 300)),
            created=created,
            modified=created + fake.time_delta(10),
            sponsored=fake.boolean()
        )
        post.save()
