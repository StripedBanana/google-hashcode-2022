class Project:
    def __init__(self, name, requiredTime, reward, bestBeforeCompletion, roles):
        self.name = name
        self.requiredTime = requiredTime
        self.reward = reward
        self.bestBeforeCompletion = bestBeforeCompletion
        self.roles = roles