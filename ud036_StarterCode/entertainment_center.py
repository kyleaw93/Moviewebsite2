import fresh_tomatoes
import media

# list of movies and there respective attributes
pulp_fiction = media.Movie(
    "Pulp Fiction",
    "The lives of two mob hitmen, a boxer, a gangster's
    "wife, and a pair of diner bandits intertwine in four
    "tales of violence and redemption.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTkxMTA5OTAzMl5BMl5BanBnXkFtZTgwNjA5MDc3NjE@._V1_SY1000_CR0,0,673,1000_AL_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=ewlwcEBTvcg")

scarface = media.Movie(
    "Scarface",
    "He loved the American dream, with a vengance",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BNjdjNGQ4NDEtNTEwYS00MTgxLTliYzQtYzE2ZDRiZjFhZmNlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,666,1000_AL_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=7pQQHnqBa2E")

goodfellas = media.Movie(
    "Goodfellas",
    "Dont mess with the wise guys",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BNThjMzczMjctZmIwOC00NTQ4LWJhZWItZDdhNTk5ZTdiMWFlXkEyXkFqcGdeQXVyNDYyMDk5MTU@._V1_SY1000_CR0,0,669,1000_AL_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=qo5jJpHtI1Y")

human_centipede = media.Movie(
    "Human Centipede",
    "Their flesh is his fantasy",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTY4Nzk3NzYxOF5BMl5BanBnXkFtZTcwODQwNjQzMw@@._V1_SY1000_SX679_AL_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=glfBurdSUS8")

Bad_Santa = media.Movie(
    "Bad Santa",
    "A miserable conman and his partner pose as Santa and his
    "Little Helper to rob department stores on Christmas Eve.
    "But they run into problems when the conman befriends a troubled kid.",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA4Njg1MDcwN15BMl5BanBnXkFtZTYwMzAxNjM3._V1_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=V6WO7q_80MI")

the_disaster_artist = media.Movie(
    "The Disaster Artist",
    "Have you seen the Room?",
    "https://images-na.ssl-images-amazon.com/images/M/MV5BOGNkMzliMGMtMDI5Ni00OTZkLTgyMTYtNzk5ZTY1NjVhYjVmXkEyXkFqcGdeQXVyNTAzMTY4MDA@._V1_SY1000_SX675_AL_.jpg",  # NOQA
    "https://www.youtube.com/watch?v=5Qa6Flvv11w")
# List of movies names to implement with fresh_tomatoes.py
movies = [pulp_fiction, scarface, goodfellas, human_centipede, Bad_Santa,
          the_disaster_artist]

fresh_tomatoes.open_movies_page(movies)
