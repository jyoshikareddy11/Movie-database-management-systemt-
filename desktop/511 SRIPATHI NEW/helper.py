import random
from faker import Faker

fake = Faker()

adjectives = [
    "Amazing", "Bewitched", "Charming", "Dazzling", "Enigmatic",
    "Fantastic", "Glorious", "Harmonious", "Incredible", "Jubilant",
    "Magical", "Radiant", "Spectacular", "Thrilling", "Wonderous"
]

nouns = [
    "Adventure", "Dream", "Escape", "Fantasy", "Journey",
    "Mystery", "Odyssey", "Quest", "Voyage", "Legend",
    "Miracle", "Enchantment", "Whisper", "Wonder", "Treasure"
]

def generate_movie_title():
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    random_number = random.randint(1000, 9999)
    return f"{adjective} {noun} {random_number}"

def generate_random_genre():
    genres = ["Action", "Drama", "Comedy", "Sci-Fi", "Romance"]
    return random.choice(genres)

def generate_random_director():
    return fake.name(), fake.date_of_birth(minimum_age=30, maximum_age=70)

def generate_random_actor():
    return fake.name(), fake.date_of_birth(minimum_age=20, maximum_age=80)


