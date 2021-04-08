# generate random startup ideas, based on industry/topic chosen

import random


class startupStack:

    def __init__(self, industry="tech"):
        self.industry = industry

    def setIndustry(self, input):
        self.industry = input

    def getIndustry(self):
        return self.industry
        # might need to add underscore after self

    def getIdea(self):
        stack = ['idea1', 'idea2']
        n = random.randint(0, 1)
        return stack[n]


ideaStack = startupStack()

ideaStack.setIndustry('Tech')

print("The industry chosen is: " + ideaStack.getIndustry())

print(ideaStack.getIdea())
