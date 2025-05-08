from PyQt6.QtWidgets import QApplication
from voting_gui import VotingApp
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VotingApp()
    window.show()
    sys.exit(app.exec())
