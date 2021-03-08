from query import query_colleges

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
    Question(1, "What do you prefer the environment to be?",
             [Answer(1, "City (Population: over 250,000)"),
              Answer(2, "Suburb (Population: 100,000 - 250,000)"),
              Answer(3, "Town (cluster 10 - 35 miles away from urban area)"),
              Answer(4, "Rural (5 - 25 miles away from urban area)")]),
    Question(2, "What is your ideal location?",
             [Answer(1, "New England (CT, ME, MA, NH, RI, VT)"),
              Answer(2, "Mid East (DE, DC, MD, NJ, NY, PA)"),
              Answer(3, "Great Lakes (IL, IN, MI, OH, WI)"),
              Answer(4, "Plains (IA, KS, MN, MO, NE, ND, SD)"),
              Answer(5, "Southeast (AL, AR, FL, GA, KY, LA, MS, NC, SC, TN, VA, WV)"),
              Answer(6, "Southwest (AZ, NM, OK, TX)"),
              Answer(7, "Rocky Mountains (CO, ID, MT, UT, WY)"),
              Answer(8, "Outlying Areas (AS, FM, GU, MH, MP, PR, PW, VI)")]),
    Question(3, "What do you prefer the environment to be?",
             [Answer(1, "City (Population: 250,000+)"),
              Answer(2, "Suburb (Population: 100,000 - 250,000)"),
              Answer(3, "Town (cluster 10 - 35 miles away from urban area)"),
              Answer(4, "Rural (5 - 25 miles away from urban area)")]),
    Question(4, "What majors/areas of study are you most interested in?",
             [Answer(1, "STEM"),
              Answer(2, "English/Journalism/History"),
              Answer(3, "Fine Arts"),
              Answer(4, "Other")]),
    Question(5, "What degree are you looking to get in college?",
             [Answer(1, "Associates Degree"),
              Answer(2, "Doctorate"),
              Answer(3, "Master's Degree"),
              Answer(4, "Bachelor's Degree"),
              Answer(5, "2 Year / 4 Year Special Focus")]),
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
