# Simple Recommendation System for Movies, Books, and Products

items = [
    # Movies
    {"name": "Inception", "type": "movie", "tags": ["sci-fi", "thriller"]},
    {"name": "The Matrix", "type": "movie", "tags": ["sci-fi", "action"]},
    {"name": "Interstellar", "type": "movie", "tags": ["sci-fi", "adventure"]},
    {"name": "Pride and Prejudice (Movie)", "type": "movie", "tags": ["romance", "classic"]},
    # Books
    {"name": "The Alchemist", "type": "book", "tags": ["fiction", "philosophy"]},
    {"name": "Clean Code", "type": "book", "tags": ["programming", "tech"]},
    {"name": "Pride and Prejudice", "type": "book", "tags": ["romance", "classic"]},
    {"name": "Data Structures in Java", "type": "book", "tags": ["programming", "tech", "java"]},
    # Products
    {"name": "Wireless Mouse", "type": "product", "tags": ["electronics", "tech"]},
    {"name": "Java Headphones", "type": "product", "tags": ["electronics", "music", "tech"]},
    {"name": "Kindle E-reader", "type": "product", "tags": ["electronics", "book", "reading"]},
    {"name": "Movie Poster Set", "type": "product", "tags": ["decor", "movie", "classic"]},
]

def recommend(preferences, items):
    recs = []
    pref_set = set(preferences)
    for item in items:
        if pref_set.intersection(item["tags"]):
            recs.append(item)
    return recs

user_input = input("Enter your interests separated by commas (e.g., sci-fi, tech, romance, java, electronic): ")
user_preferences = [x.strip().lower() for x in user_input.split(",")]

rec_results = recommend(user_preferences, items)

print("\nRecommended for you:")
types = {"movie": "Movies", "book": "Books", "product": "Products"}
found = {"movie": False, "book": False, "product": False}
for t in types:
    filtered = [i["name"] for i in rec_results if i["type"] == t]
    if filtered:
        print(f"\n{types[t]}:")
        for name in filtered:
            print(f" - {name}")
        found[t] = True
if not any(found.values()):
    print("Sorry, no recommendations found for your interests.")
