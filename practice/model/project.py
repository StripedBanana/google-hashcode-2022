class Project:
    def __init__(self, name, requiredTime, reward, bestBeforeCompletion, roleCount):
        self.name = name
        self.requiredTime = requiredTime
        self.reward = reward
        self.bestBeforeCompletion = bestBeforeCompletion
        self.roleCount = roleCount