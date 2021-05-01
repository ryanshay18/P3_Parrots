# generate random startup ideas, based on industry/topic chosen

import random


class startupStack:

    def __init__(self, industry="tech"):
        self.industry = industry

    def setIndustry(self, input):
        self.industry = input

    @property
    def getIndustry(self):
        return self.industry

    def getIdea(self):
        stack = ['Better Grocery Bulk Dispensing in Grocery Stores', 'Smart Toilet for Biometric Data',
                 'A vertical social network for floraphiles', 'Infrastructure to launch restaurants at lower cost',
                 'An Api for Multiple Real estate listing services']
        n = random.randint(0, 3)
        return stack[n]

    def sequential_search(self, alist, item):
        position = 0

        while position < len(alist):
            if alist[position] == item:
                print("Its there!")
                return True
            position = position + 1

        print("No luck! :(")
        return False


# Initialization:
ideaStack = startupStack()

# Setter
ideaStack.setIndustry('Tech')
# Getter
print("The industry chosen is: " + ideaStack.getIndustry)

# Getter
print(ideaStack.getIdea())

# Algorithm
Industries = ["Tech", "Florists", "Retail"]
ideaStack.sequential_search(Industries, "Tech")
ideaStack.sequential_search(Industries, "Movies")
