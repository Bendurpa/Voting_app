import csv
from typing import Dict

class VoteData:
    def __init__(self, file_name: str):
        self.file_name = file_name

    def load(self) -> Dict[str, int]:
        votes = {"John": 0, "Jane": 0, "Other": 0}
        try:
            with open(self.file_name, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] in votes:
                        votes[row[0]] = int(row[1])
        except FileNotFoundError:
            pass
        return votes

    def save(self, votes: Dict[str, int]):
        with open(self.file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            for name, count in votes.items():
                writer.writerow([name, count])
