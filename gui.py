# gui.py
from PyQt6 import QtWidgets, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("Voting Application")
        MainWindow.resize(300, 250)

        self.central_widget = QtWidgets.QWidget(parent=MainWindow)
        MainWindow.setCentralWidget(self.central_widget)

        self.layout = QtWidgets.QVBoxLayout(self.central_widget)

        self.title_label = QtWidgets.QLabel("VOTING APPLICATION")
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(12)
        self.title_label.setFont(font)
        self.layout.addWidget(self.title_label)

        self.id_label = QtWidgets.QLabel("ID")
        self.layout.addWidget(self.id_label)

        self.id_input = QtWidgets.QLineEdit()
        self.layout.addWidget(self.id_input)

        self.candidates_label = QtWidgets.QLabel("CANDIDATES")
        self.layout.addWidget(self.candidates_label)

        self.radio_jane = QtWidgets.QRadioButton("Jane")
        self.radio_john = QtWidgets.QRadioButton("John")
        self.layout.addWidget(self.radio_jane)
        self.layout.addWidget(self.radio_john)

        self.submit_button = QtWidgets.QPushButton("SUBMIT VOTE")
        self.layout.addWidget(self.submit_button)

        self.message_label = QtWidgets.QLabel("")
        self.layout.addWidget(self.message_label)
