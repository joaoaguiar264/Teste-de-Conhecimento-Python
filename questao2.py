movies = [
{"titulo": "O Senhor dos Anéis", "ano": 2001, "avaliacao": 8.8},
{"titulo": "Matrix", "ano": 1999, "avaliacao": 9.3},
{"titulo": "Interestelar", "ano": 2014, "avaliacao": 8.6}
]

average_rating = 0
biggest_rating = 0
smallest_rating = float('inf')

for movie in movies:
    if(movie["avaliacao"] > biggest_rating):
        biggest_rating = movie["avaliacao"]
        biggest_rating_movie = movie["titulo"]
    if(movie["avaliacao"] < smallest_rating):
        smallest_rating = movie["avaliacao"]
        smallest_rating_year = movie["ano"]
    average_rating += movie["avaliacao"]

average_rating /= len(movies)
print("Média das avaliações: " + average_rating.__str__())
print("Filme de maior avaliação: " + biggest_rating_movie)
print("Ano de lançamento do filme de menor avaliação: " + smallest_rating_year.__str__())
