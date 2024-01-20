from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QLayout, QGroupBox

from rare.models.game import RareGame
from rare.models.install import SelectiveDownloadsModel
from rare.utils.misc import icon
from rare.widgets.dialogs import ButtonDialog, dialog_title_game
from rare.widgets.selective_widget import SelectiveWidget


class SelectiveDialog(ButtonDialog):
    result_ready = pyqtSignal(RareGame, SelectiveDownloadsModel)

    def __init__(self, rgame: RareGame, parent=None):
        super(SelectiveDialog, self).__init__(parent=parent)
        header = self.tr("Optional downloads for")
        self.setWindowTitle(dialog_title_game(header, rgame.app_title))
        self.setSubtitle(dialog_title_game(header, rgame.app_title))

        self.rgame = rgame
        self.selective_widget = SelectiveWidget(rgame, rgame.igame.platform, self)

        container = QGroupBox(self.tr("Optional downloads"), self)
        container_layout = QVBoxLayout(container)
        container_layout.setContentsMargins(0, 0, 0, 0)
        container_layout.addWidget(self.selective_widget)

        self.setCentralWidget(container)

        self.accept_button.setText(self.tr("Verify"))
        self.accept_button.setIcon(icon("fa.check"))

        self.options: SelectiveDownloadsModel = SelectiveDownloadsModel(rgame.app_name)

    def done_handler(self):
        self.result_ready.emit(self.rgame, self.options)

    def accept_handler(self):
        self.options.accepted = True
        self.options.install_tag = self.selective_widget.install_tags()

    def reject_handler(self):
        self.options.accepted = False
        self.options.install_tag = None
