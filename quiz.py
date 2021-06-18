from query import query_colleges

class Answer:
    def __init__(self, answer_index, answer_text):
        self.index = answer_index
        self.text = answer_text


class Question:
    def __init__(self, index, question, field, answers):
        self.index = index
        self.question = question
        self.field = field
        self.answers = answers

    def find_answer(self, index):
        for answer in self.answers:
            if answer.index == index:
                return answer


questions = [
    Question(1, "What is favorite genre of movies?", "Genres",
             [Answer(1, "Thriller"),
              Answer(2, "Romance"),
              Answer(3, "Action"),
              Answer(4, "Comedy"),
              Answer(5, "Drama")]),
    Question(2, "What is your ideal provider?", "Providers",
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
    Question(3, "Would you prefer to...", "OfferTypes",
             [Answer(1, "Buy"),
              Answer(2, "Subscription"),
              Answer(3, "Rent"),
              Answer(4, "Free")]),
    # Question(4, "What rating do you want the movie to have?",
    #          [Answer(1, "90+"),
    #           Answer(2, "80-90"),
    #           Answer(3, "70-80"),
    #           Answer(4, "60-70"),
    #           Answer(5, "50-60"),
    #           Answer(6, "40-50"),
    #           Answer(7, "Below 40")]),
    Question(4, "Do you want to watch a...", "ProgramTypes",
              [Answer(1, "Show"),
               Answer(2, "Movie"),
               Answer(3, "Game"),
               Answer(4, "Certain Episode"),
               Answer(5, "Certain Season")])
    # Question(6, "Which do you prefer for the original release date?",
    #          [Answer(1, "After 2010"),
    #           Answer(2, "2000-2010"),
    #           Answer(3, "1990-2000"),
    #           Answer(4, "Before 1990")
]


def quiz_data():
    return questions


def handle_response(answers):
    print(answers)
    return query_colleges()
    return "Hello my little Pinguino!"

# questions =
#
# What do you prefer the environment to be?
#
# City (Population: over 250,000)
# Suburb (Population: 100,000 - 250,000)
# Town (cluster 10 - 35 miles away from urban area)
# Rural (5 - 25 miles away from urban area)
