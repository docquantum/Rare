from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QTabWidget, QWidget
from qtawesome import icon

from rare.components.tab_utils import TabBar, TabButtonWidget
from rare.components.tabs.cloud_saves import SyncSaves
from rare.components.tabs.downloads.__init__ import DownloadTab
from rare.components.tabs.games import GameTab
from rare.components.tabs.settings import SettingsTab
from rare.utils.models import InstallOptions
from custom_legendary.core import LegendaryCore


class TabWidget(QTabWidget):
    def __init__(self, core: LegendaryCore):
        super(TabWidget, self).__init__()
        disabled_tab = 3
        self.setTabBar(TabBar(disabled_tab))
        self.settings = SettingsTab(core)
        self.game_list = GameTab(core)
        self.game_list.default_widget.game_list.update_game.connect(lambda: self.setCurrentIndex(1))
        updates = self.game_list.default_widget.game_list.updates
        self.addTab(self.game_list, self.tr("Games"))
        self.downloadTab = DownloadTab(core, updates)
        self.addTab(self.downloadTab, "Downloads" + (" (" + str(len(updates)) + ")" if len(updates) != 0 else ""))
        self.downloadTab.finished.connect(self.dl_finished)
        self.game_list.default_widget.game_list.install_game.connect(lambda x: self.downloadTab.install_game(x))

        self.game_list.game_info.info.verify_game.connect(lambda app_name: self.downloadTab.install_game(
            InstallOptions(app_name, core.get_installed_game(app_name).install_path, repair=True)))

        self.tabBarClicked.connect(lambda x: self.game_list.layout.setCurrentIndex(0) if x == 0 else None)

        self.cloud_saves = SyncSaves(core)
        self.addTab(self.cloud_saves, "Cloud Saves")

        # Space Tab
        self.addTab(QWidget(), "")
        self.setTabEnabled(disabled_tab, False)

        self.account = QWidget()
        self.addTab(self.account, "")
        self.setTabEnabled(disabled_tab + 1, False)
        # self.settings = SettingsTab(core)

        self.addTab(self.settings, icon("fa.gear", color='white'), "(!)" if self.settings.about.update_available else "")
        self.setIconSize(QSize(25, 25))
        self.tabBar().setTabButton(3, self.tabBar().RightSide, TabButtonWidget(core))

    def dl_finished(self):
        self.game_list.default_widget.game_list.update_list()
        self.setTabText(1, "Downloads")

    def resizeEvent(self, event):
        self.tabBar().setMinimumWidth(self.width())
        super(TabWidget, self).resizeEvent(event)
