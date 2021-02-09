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
    Question(2, "How smart are you?",
             [Answer(1, "Not very"),
              Answer(2, "Extremely"),
              Answer(3, "Who, me?")]),
    Question(3, "How dumb are you?",
             [Answer(1, "Not very"),
              Answer(2, "Extremely"),
              Answer(3, "Who, me?")])
]


def quiz_data():
  return questions



# questions =
#
# What do you prefer the environment to be?
#
# City (Population: over 250,000)
# Suburb (Population: 100,000 - 250,000)
# Town (cluster 10 - 35 miles away from urban area)
# Rural (5 - 25 miles away from urban area)