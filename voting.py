from storage import VoteData

class VotingSystem:
    def __init__(self):
        self.vote_data = VoteData("votes.csv")
        self.votes_count = {"John": 0, "Jane": 0, "Other": 0}
        self.load_votes()

    def load_votes(self):
        try:
            self.votes_count = self.vote_data.load()
        except Exception as error:
            print(f"Error loading votes: {error}")

    def add_vote(self, name: str):
        if name in self.votes_count:
            self.votes_count[name] += 1
            self.save_votes()

    def save_votes(self):
        try:
            self.vote_data.save(self.votes_count)
        except Exception as error:
            print(f"Error saving votes: {error}")

    def get_summary(self) -> str:
        total = sum(self.votes_count.values())
        return ", ".join([f"{name}: {count}" for name, count in self.votes_count.items()]) + f", Total: {total}"

    def reset_votes(self):
        self.votes_count = {"John": 0, "Jane": 0, "Other": 0}
        self.save_votes()
