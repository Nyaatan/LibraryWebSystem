from pprint import pprint

from models import *
from settings import *

subscriptions = [
    Subscription('None', 2, 0),
    Subscription('Basic', 5, 10),
    Subscription('Bookworm', 15, 20),
    Subscription('No-life', 45, 30)
]

data = {'subscriptions': subscriptions}

def generate():
    data['authors'] = [Author.random() for _ in range(author_count)]
    data['categories'] = [Category.random(name=name) for name in genres]
    data['publishers'] = [Publisher.random() for _ in range(publisher_count)]
    data['books'] = [Book.random(author=author,
                                 subauthors=random.choices(data['authors'], k=uniform(1, multi_author_count))
                                 if uniform(1, multi_author_chance) == 1
                                 else None, cateory=random.choices(data['categories'])[0]
                                 ) for author in data['authors']
                     for _ in range(books_of_author())]
    data['editions'] = [Edition.random(book=book, publisher=random.choices(data['publishers'])[0]) for book in data['books']]
    data['cards'] = [Card.random() for _ in range(card_count)]
    data['users'] = [User.random(subscription=random.choices(data['subscriptions'])[0], card=card) for card in data['cards']]
    data['payments'] = [Payment.random(user=user) for user in data["users"]]
    data['borrowings'] = [Borrowing.random(user=user, edition=random.choices(data['editions'])[0]) for user in data['users']
                          for _ in range(user.subscription.count-user.borrowings_remaining-1)]


    for key, val in data.items():
        for i, item in enumerate(val):
            item.id = i


    query_script = ""
    for key, val in data.items():
        for item in val:
            query_script += item.query()
            query_script += "\n"
    return query_script
