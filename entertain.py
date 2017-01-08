import movies
import fresh_tomatoes

toy_story = movies.Movie("Toy Story", "A story of a boy with it's toys", "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v8_ab.jpg", "https://youtu.be/KYz2wyBy3kc")
#print(toy_story.story_line)
#toy_story.show_trailor()
movies = [toy_story]
fresh_tomatoes.open_movies_page(movies)
