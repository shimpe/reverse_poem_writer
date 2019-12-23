from iface import Ui_Dialog
from PyQt5.QtWidgets import QFileDialog, QMessageBox


class MyDialog(Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.parent = None
        self.filename = None
        self.modified = False

    def on_modification_changed(self, modified):
        self.modified = modified

    def on_text_changed(self):
        text = self.left.toPlainText()
        textlines = text.splitlines()
        new_text = ""
        for l in reversed(textlines):
            new_text += l
            new_text += "\n"
        self.right.setPlainText(new_text)

    def check_save_required(self):
        if self.modified:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("You have unsaved changes. Save first?")
            msg.setWindowTitle("Unsaved changes")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            retval = msg.exec_()
            if retval == QMessageBox.Ok:
                self.on_save_button_clicked()

    def on_load_button_clicked(self):
        self.check_save_required()

        from pathlib import Path
        home = str(Path.home())
        filename = QFileDialog.getOpenFileName(None, 'Open file',
                                               home, "Text files (*.txt)")
        filename = filename[0]
        if filename:
            with open(filename, "r") as f:
                self.left.setPlainText(f.read())
            self.filename = filename
            self.parent.setWindowTitle("Reverse Poem Writer - {0}".format(self.filename))
            self.left.document().setModified(False)

    def on_save_as_button_clicked(self):
        from pathlib import Path
        home = str(Path.home())
        filename = QFileDialog.getSaveFileName(None, 'Save file',
                                               home, "Text files (*.txt)")
        filename = filename[0]
        if filename:
            with open(filename, "w") as f:
                f.write(self.left.toPlainText())
            self.filename = filename
            self.parent.setWindowTitle("Reverse Poem Writer - {0}".format(self.filename))
            self.left.document().setModified(False)

    def on_save_button_clicked(self):
        if self.filename is None:
            self.on_save_as_button_clicked()
        else:
            with open(self.filename, "w") as f:
                f.write(self.left.toPlainText())
            self.parent.setWindowTitle("Reverse Poem Writer - {0}".format(self.filename))
            self.left.document().setModified(False)

    def on_close_button_clicked(self):
        self.parent.reject()

    def setup_connections(self, parent):
        self.parent = parent
        self.left.textChanged.connect(self.on_text_changed)
        self.left.modificationChanged.connect(self.on_modification_changed)
        self.save.clicked.connect(self.on_save_button_clicked)
        self.load.clicked.connect(self.on_load_button_clicked)
        self.closebtn.clicked.connect(self.on_close_button_clicked)
        self.saveAs.clicked.connect(self.on_save_as_button_clicked)

