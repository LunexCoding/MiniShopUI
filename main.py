import sys

from PySide2.QtWidgets import QApplication

from app import MainWindow
from dbApp.dbApp import DatabaseInitializer


if __name__ == "__main__":
    DatabaseInitializer.run()
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
