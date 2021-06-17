from query import query_movies

class Answer:
    def __init__(self, answer_index, answer_text):
        self.index = answer_index
        self.text = answer_text


class Question:
    def __init__(self, index, question, answers):
        self.index = index
        self.question = question
        self.answers = answers


questions = [
    Question(1, "What is favorite genre of movies?",
             [Answer(1, "Thriller"),
              Answer(2, "Rom-Com"),
              Answer(3, "Action"),
              Answer(4, "Comedy")]),
    Question(2, "What is your ideal provider?",
             [Answer(1, "AmazonInstantVideo"),
              Answer(2, "NBC"),
              Answer(3, "ABC"),
              Answer(4, "FOX"),
              Answer(5, "FandangoMovies"),
              Answer(6, "GooglePlay"),
              Answer(7, "CBS"),
              Answer(8, "TheCW"),
              Answer(9, "TBS"),
              Answer(10,"Nickelodeon"),
              Answer(11,"PBS"),
              Answer(12,"Discovery Channel"),
              Answer(13,"HBO"),
              Answer(14,"DisneyXD"),
              Answer(15,"USANetwork"),
              Answer(16,"Hulu"),
              Answer(17,"AmazonPrimeVideo"),
              Answer(18,"iTunes"),
              Answer(19,"Netflix"),
              Answer(20,"AtomTickets")]),
    Question(3, "Would you prefer to...",
             [Answer(1, "Buy the movie"),
              Answer(2, "Have a subscription"),
              Answer(3, "Free rent")]),
    Question(4, "What (iVa) rating do you want the movie to have?",
             [Answer(1, "90+"),
              Answer(2, "80-90"),
              Answer(3, "70-80"),
              Answer(4, "60-70"),
              Answer(5, "50-60"),
              Answer(6, "40-50"),
              Answer(7, "Below 40")]),
    Question(5, "Do you want to watch a...",
             [Answer(1, "Show"),
              Answer(2, "Movie"),
              Answer(3, "Game"),
              Answer(4, "Certain Episode"),
              Answer(5, "Certain Season")]),
    Question(6, "Which do you prefer for the original release date?",
             [Answer(1, "After 2010"),
              Answer(2, "2000-2010"),
              Answer(3, "1990-2000"),
              Answer(4, "Before 1990")]),
]


def quiz_data():
    return questions


def handle_response(answers):
    print(answers)
    return query_movies()
    return "Works!"

# questions =
#
# What do you prefer the environment to be?
#
# City (Population: over 250,000)
# Suburb (Population: 100,000 - 250,000)
# Town (cluster 10 - 35 miles away from urban area)
# Rural (5 - 25 miles away from urban area)
