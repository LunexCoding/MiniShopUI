import sys

from PySide2.QtWidgets import QApplication

from admin.interface import resources_rc
from admin.interface.app import MainWindow
from admin.backend.dbApp.dbApp import DatabaseInitializer


if __name__ == "__main__":
    DatabaseInitializer.run()
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
