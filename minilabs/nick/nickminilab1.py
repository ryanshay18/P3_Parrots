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
        stack = ['Better Grocery Bulk Dispensing in Grocery Stores', 'Smart Toliet for Biometric Data', 'A vertical social network for floraphiles', 'Infrastructure to launch resaurants at lower cost', 'An Api for Multiple Real estate listing services']
        n = random.randint(0, 3)
        return stack[n]


ideaStack = startupStack()

ideaStack.setIndustry('Tech')

print("The industry chosen is: " + ideaStack.getIndustry())

print(ideaStack.getIdea())

