import media
import fresh_tomatoes

toy_story=media.Movie("Toy story",
						"a story of a boy and his toys come to life",
	                    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
	                    "https://www.youtube.com/watch?v=rNk1Wi8SvNc")

#print (toy_story.storyline)

avatar=media.Movie("Avatar",
					"a marine on an alien palnet",
	               	"https://upload.wikimedia.org/wikipedia/en/9/9b/Avatar-_The_Last_Airbender_Book_1_DVD.jpg",
	               	"https://www.youtube.com/watch?v=meKMAfRqnB8")
#print (avatar.storyline)
#avatar.show_trailer()

Intouchables=media.Movie("Intouchables",
								"Brother Bear is a 2003 American animated comedy-drama film produced by Walt Disney Feature Animation and released by Walt Disney Pictures. It is the 44th Disney animated feature film. In the film, an Inuit boy named Kenai pursues a bear in revenge for a battle that he provoked in which his oldest brother Sitka is killed",
						        "https://upload.wikimedia.org/wikipedia/en/9/93/The_Intouchables.jpg",
						        "https://www.youtube.com/watch?v=34WIbmXkewU")


brother_bear=media.Movie("Brother bear",
							"It is the 44th revenge for a battle that he provoked in which his oldest brother Sitka is killed",
						    "https://upload.wikimedia.org/wikipedia/en/d/dd/Brotherbear2.jpg",
						    "https://www.youtube.com/watch?v=B80VKbxZs6E")

AManalledove=media.Movie("A Man Called Ove",
						"Brother Bear is a 2003 American animated comedy-drama film produced by Walt Disney Feature Animation and released by Walt Disney Pictures. It is the 44th Disney animated feature film. In the film, an Inuit boy named Kenai pursues a bear in revenge for a battle that he provoked in which his oldest brother Sitka is killed",
						"https://upload.wikimedia.org/wikipedia/en/3/3d/A_Man_Called_Ove_%28novel%29.jpg",
						"https://www.youtube.com/watch?v=oCh4iiAXuAc")

youngsheldon=media.Movie("Yong sheldon",
							"Brother Bear is a 2003 American animated comedy-drama film produced by Walt Disney Feature Animation and released by Walt Disney Pictures. It is the 44th Disney animated feature film. In the film, an Inuit boy named Kenai pursues a bear in revenge for a battle that he provoked in which his oldest brother Sitka is killed",
							"http://images6.fanpop.com/image/photos/40700000/Cast-of-Young-Sheldon-young-sheldon-40742795-960-1440.jpg",
						    "https://www.youtube.com/watch?v=EXsvAK3EFqo")

movies = [toy_story, avatar, Intouchables, brother_bear, AManalledove, youngsheldon]
fresh_tomatoes.open_movies_page(movies)