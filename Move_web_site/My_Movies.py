import fresh_tomatoes
import media


the_Proposal = media.Movie("The Proposal",
	                       "A pushy boss forces her young assistant to marry her in order to keep her visa status in the U.S. and avoid deportation to Canada.",
	                       "http://www.filmgoo.com/uploads/film/2017/12/teklif-the-proposal-izle-2009-1080p-648.jpg",
	                       "https://www.youtube.com/watch?v=amtK00WLULY")


passengers = media.Movie("Passengers",
	                     "A spacecraft traveling to a distant colony planet and transporting thousands of people has a malfunction in its sleep chambers. As a result, two passengers are awakened 90 years early.",
	                     "http://www.sonypictures.com/movies/passengers/assets/images/onesheet.jpg",
	                     "https://www.youtube.com/watch?v=7BWWWQzTpNU")


the_mask = media.Movie("The mask",
	                   "Bank clerk Stanley Ipkiss is transformed into a manic superhero when he wears a mysterious mask.",
	                   "https://i.ytimg.com/vi/TgVb69WykQk/movieposter.jpg",
	                   "https://www.youtube.com/watch?v=hOqVRwGVUkA")


gladiator = media.Movie("Gladiator",
	                    "When a Roman General is betrayed, and his family murdered by an emperor's corrupt son, he comes to Rome as a gladiator to seek revenge.",
	                    "https://i.pinimg.com/originals/45/f4/86/45f48683847444c4264254ad601642f6.jpg",
	                    "https://www.youtube.com/watch?v=do9zep1n8cU")


midnight_in_paris = media.Movie("Midnight in Paris",
	                            "While on a trip to Paris with his fiancee's family a nostalgic screenwriter finds himself mysteriously going back to the 1920s everyday at midnight.",
	                            "http://is5.mzstatic.com/image/thumb/Video/v4/80/5c/8f/805c8f2a-5d93-0621-2f3d-2f23ba60f775/source/1200x630bb.jpg",
	                            "https://www.youtube.com/watch?v=FAfR8omt-CY")


toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://www.4usky.com/data/out/96/164871590-toy-story-wallpapers.jpg",
                        "https://www.youtube.com/watch?v=rNk1Wi8SvNc")


The_Wolf_of_Wall_Street = media.Movie("The Wolf of Wall Street",
	                                  "Based on the true story of Jordan Belfort, from his rise to a wealthy stock-broker living the high life to his fall involving crime, corruption and the federal government.",
	                                  "https://ia.media-imdb.com/images/M/MV5BMjIxMjgxNTk0MF5BMl5BanBnXkFtZTgwNjIyOTg2MDE@._V1_UX182_CR0,0,182,268_AL_.jpg",
	                                  "https://www.youtube.com/watch?v=iszwuX1AK6A")



movies = [the_Proposal, passengers, gladiator, midnight_in_paris, the_mask,toy_story]


# programe excution
fresh_tomatoes.open_movies_page(movies)

"""
# Test2
print("The name of the class")
print""
print(media.Movie.__name__)
print""
print("The name of the module")
print""
print(media.Movie.__module__)
print""


# Test3

#print(gladiator.poster_image_url)
#toy_story.show_trailer()
"""