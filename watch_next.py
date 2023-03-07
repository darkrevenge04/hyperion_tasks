import spacy
nlp = spacy.load('en_core_web_md')

# gets list of possible movie choices from .txt file
with open("movies.txt", "r+", encoding="utf-8") as file:
    movie_details = file.readlines()

# Movie choice and description that is compared against
movie_title = "Planet Hulk"
movie_description = nlp(str("Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth,"
                            "the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the "
                            "Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold "
                            "into slavery and trained as a gladiator"))

# Compares imported movies against movie_description
movies = {}
for i in range(len(movie_details)):
    title = movie_details[i]
    movies[str(title).split(':')[0]] = nlp(movie_details[i]).similarity(movie_description)

# sorts out the similarity dictionary then prints the most similar movie title
sorted_movies = sorted(movies.items(), key=lambda x: x[1], reverse=True)
print(f"{sorted_movies[0][0]} is the best choice for you")
