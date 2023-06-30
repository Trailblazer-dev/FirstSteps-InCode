class manual:
    def __init__(self, model, category):
        self.model = model
        self.category = category
    def _str_(self):
        return f"{self.model}{self.category}"
foot = manual("v321", "B")
print(foot)
print(foot.model, foot.category)
#indexing is very important always keep that in Mind
        