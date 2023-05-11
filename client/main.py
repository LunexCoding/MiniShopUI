import sys

from PySide2.QtWidgets import QApplication

from client.interface import resources_rc
from client.interface.app import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
