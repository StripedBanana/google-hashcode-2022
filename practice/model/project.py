class Project:
    def __init__(self, name, requiredTime, reward, bestBeforeCompletion, roles):
        self.name = name
        self.requiredTime = requiredTime
        self.reward = reward
        self.bestBeforeCompletion = bestBeforeCompletion
        self.roles = roles

    def __str__(self):
        return "{}\n{}\n".format(self.name, " ".join([cont.name for cont in self.contributors]))