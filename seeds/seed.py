import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, db
from models import Episode, Guest, Appearance

episodes = [
    Episode(date="2024-01-01", number=1),
    Episode(date="2024-01-08", number=2),
    Episode(date="2024-01-15", number=3),
]

guests = [
    Guest(name="John", occupation="Actor"),
    Guest(name="Jane", occupation="Musician"),
    Guest(name="Johnson", occupation="Comedian"),
]

appearances = [
    Appearance(rating=4, episode=episodes[0], guest=guests[0]),
    Appearance(rating=5, episode=episodes[0], guest=guests[1]),
    Appearance(rating=3, episode=episodes[1], guest=guests[2]),
    Appearance(rating=2, episode=episodes[2], guest=guests[0]),
]

def seed():
    db.drop_all()
    db.create_all()

    db.session.add_all(episodes)
    db.session.add_all(guests)
    db.session.add_all(appearances)
    
    db.session.commit()
    print("Database seeded!")

if __name__ == '__main__':
    with app.app_context():
        seed()
