from iface import Ui_Dialog
from PyQt5.QtWidgets import QDialogButtonBox, QFileDialog


class MyDialog(Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.parent = None

    def on_text_changed(self):
        text = self.left.toPlainText()
        textlines = text.splitlines()
        new_text = ""
        for l in reversed(textlines):
            new_text += l
            new_text += "\n"
        self.right.setPlainText(new_text)

    def on_load_button_clicked(self):
        from pathlib import Path
        home = str(Path.home())
        filename = QFileDialog.getOpenFileName(None, 'Open file',
                                               home, "Text files (*.txt)")
        filename = filename[0]
        if filename:
            with open(filename, "r") as f:
                self.left.setPlainText(f.read())

    def on_save_button_clicked(self):
        from pathlib import Path
        home = str(Path.home())
        filename = QFileDialog.getSaveFileName(None, 'Save file',
                                               home, "Text files (*.txt)")
        filename = filename[0]
        if filename:
            with open(filename, "w") as f:
                f.write(self.left.toPlainText())

    def on_close_button_clicked(self):
        self.parent.reject()

    def setup_connections(self, parent):
        self.parent = parent
        self.left.textChanged.connect(self.on_text_changed)
        self.save.clicked.connect(self.on_save_button_clicked)
        self.load.clicked.connect(self.on_load_button_clicked)
        self.closebtn.clicked.connect(self.on_close_button_clicked)

