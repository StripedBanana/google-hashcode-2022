class Project:
    def __init__(self, name, requiredTime, reward, bestBeforeCompletion, roles):
        self.name = name
        self.requiredTime = requiredTime
        self.reward = reward
        self.bestBeforeCompletion = bestBeforeCompletion
        self.roles = roles

    def __str__(self):
        contributor_string = ""
        for contributor in self.contributors:
            contributor_string = "{} {} ".format(contributor_string, contributor.name)
        return "{}\n{}\n".format(self.name, contributor_string.rstrip())