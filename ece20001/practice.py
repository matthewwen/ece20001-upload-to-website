class Practice:

    def __init__(self, data):
        self.ref = data["ref"] if "ref" in data else ""
        self.title = data["title"] if "title" in data else ""
        self.answerPath = data["answerPath"] if "answerPath" in data else ""
        self.description = data["description"] if "description" in data else ""
        self.note = data["note"] if "note" in data else ""
        self.problemPath = data["problemPath"] if "problemPath" in data else ""
        self.uid = data["uid"] if "uid" in data else ""

    def get_hash(self):
        return hash(self.title + self.description + self.note)
