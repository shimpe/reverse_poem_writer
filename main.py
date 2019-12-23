from myiface import MyDialog
from PyQt5 import QtWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = MyDialog()
    ui.setupUi(Dialog)
    Dialog.show()
    ui.setup_connections(Dialog)
    sys.exit(app.exec_())