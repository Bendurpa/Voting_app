import csv
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QDialog, QVBoxLayout, QTextEdit, QPushButton
from voting_window import Ui_voting_window


class VotingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_voting_window()
        self.ui.setupUi(self)
        self.setup_connections()
        self.votes_file = "votes.csv"
        self.initialize_ui()

    def setup_connections(self):
        self.ui.confirm_button.clicked.connect(self.submit_vote)
        self.ui.summary_button.clicked.connect(self.display_summary)
        self.ui.reset_button.clicked.connect(self.clear_votes)
        self.ui.exit_button.clicked.connect(self.close)
        self.ui.other_button.toggled.connect(self.toggle_other_input)

    def initialize_ui(self):
        self.ui.other_lineedit.setEnabled(False)

    def toggle_other_input(self):
        self.ui.other_lineedit.setEnabled(self.ui.other_button.isChecked())

    def submit_vote(self):
        voter_id = self.ui.id_enter.text().strip()

        if not voter_id:
            QMessageBox.warning(self, "Input Error", "Please enter your ID.")
            return

        if self.ui.john_button.isChecked():
            selected_candidate = "John"
        elif self.ui.jane_button.isChecked():
            selected_candidate = "Jane"
        elif self.ui.other_button.isChecked():
            selected_candidate = self.ui.other_lineedit.text().strip()
            if not selected_candidate:
                QMessageBox.warning(self, "Input Error", "Please enter a name for 'Other' candidate.")
                return
        else:
            QMessageBox.warning(self, "Selection Error", "Please select a candidate.")
            return

        with open(self.votes_file, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([voter_id, selected_candidate])

        QMessageBox.information(self, "Vote Submitted", f"Vote for {selected_candidate} has been submitted.")
        self.clear_form()

    def clear_form(self):
        self.ui.id_enter.clear()
        self.ui.john_button.setChecked(False)
        self.ui.jane_button.setChecked(False)
        self.ui.other_button.setChecked(False)
        self.ui.other_lineedit.clear()
        self.ui.other_lineedit.setEnabled(False)

    def clear_votes(self):
        with open(self.votes_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Voter ID", "Candidate"])
        QMessageBox.information(self, "Votes Cleared", "All votes have been cleared.")

    def display_summary(self):
        try:
            with open(self.votes_file, newline="") as file:
                reader = csv.reader(file)
                data = list(reader)
        except FileNotFoundError:
            data = []

        summary_dialog = QDialog(self)
        summary_dialog.setWindowTitle("Voting Summary")
        layout = QVBoxLayout()
        text_area = QTextEdit()
        text_area.setReadOnly(True)

        if len(data) <= 1:
            text_area.setText("No votes have been submitted yet.")
        else:
            summary = "\n".join([f"{row[0]} voted for {row[1]}" for row in data[1:]])
            text_area.setText(summary)

        close_button = QPushButton("Close")
        close_button.clicked.connect(summary_dialog.close)
        layout.addWidget(text_area)
        layout.addWidget(close_button)
        summary_dialog.setLayout(layout)
        summary_dialog.exec()
