# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rare/ui/components/tabs/store/shop_game_info.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ShopInfo(object):
    def setupUi(self, ShopInfo):
        ShopInfo.setObjectName("ShopInfo")
        ShopInfo.resize(434, 250)
        ShopInfo.setWindowTitle("ShopGameInfo")
        self.main_layout = QtWidgets.QHBoxLayout(ShopInfo)
        self.main_layout.setObjectName("main_layout")
        self.left_layout = QtWidgets.QVBoxLayout()
        self.left_layout.setObjectName("left_layout")
        self.main_layout.addLayout(self.left_layout)
        self.right_layout = QtWidgets.QVBoxLayout()
        self.right_layout.setObjectName("right_layout")
        self.info_layout = QtWidgets.QFormLayout()
        self.info_layout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.info_layout.setContentsMargins(6, 6, 6, 6)
        self.info_layout.setSpacing(12)
        self.info_layout.setObjectName("info_layout")
        self.title_label = QtWidgets.QLabel(ShopInfo)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.title_label.setObjectName("title_label")
        self.info_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.title_label)
        self.title = QtWidgets.QLabel(ShopInfo)
        self.title.setText("title")
        self.title.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.title.setObjectName("title")
        self.info_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.title)
        self.developer_label = QtWidgets.QLabel(ShopInfo)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.developer_label.setFont(font)
        self.developer_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.developer_label.setObjectName("developer_label")
        self.info_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.developer_label)
        self.dev = QtWidgets.QLabel(ShopInfo)
        self.dev.setText("dev")
        self.dev.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.dev.setObjectName("dev")
        self.info_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.dev)
        self.status_label = QtWidgets.QLabel(ShopInfo)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.status_label.setFont(font)
        self.status_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.status_label.setObjectName("status_label")
        self.info_layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.status_label)
        self.owned_label = QtWidgets.QLabel(ShopInfo)
        self.owned_label.setObjectName("owned_label")
        self.info_layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.owned_label)
        self.price_label = QtWidgets.QLabel(ShopInfo)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.price_label.setFont(font)
        self.price_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.price_label.setObjectName("price_label")
        self.info_layout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.price_label)
        self.price_widget = QtWidgets.QWidget(ShopInfo)
        self.price_widget.setObjectName("price_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.price_widget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.price = QtWidgets.QLabel(self.price_widget)
        self.price.setText("price")
        self.price.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.price.setObjectName("price")
        self.horizontalLayout.addWidget(self.price)
        self.discount_price = QtWidgets.QLabel(self.price_widget)
        self.discount_price.setText("discount")
        self.discount_price.setObjectName("discount_price")
        self.horizontalLayout.addWidget(self.discount_price)
        self.info_layout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.price_widget)
        self.tags_label = QtWidgets.QLabel(ShopInfo)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tags_label.setFont(font)
        self.tags_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.tags_label.setObjectName("tags_label")
        self.info_layout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.tags_label)
        self.tags = QtWidgets.QLabel(ShopInfo)
        self.tags.setText("tags")
        self.tags.setObjectName("tags")
        self.info_layout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.tags)
        self.links_label = QtWidgets.QLabel(ShopInfo)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.links_label.setFont(font)
        self.links_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.links_label.setObjectName("links_label")
        self.info_layout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.links_label)
        self.social_group = QtWidgets.QWidget(ShopInfo)
        self.social_group.setMinimumSize(QtCore.QSize(250, 0))
        self.social_group.setObjectName("social_group")
        self.social_layout = QtWidgets.QHBoxLayout(self.social_group)
        self.social_layout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.social_layout.setContentsMargins(0, 0, 0, 0)
        self.social_layout.setObjectName("social_layout")
        self.info_layout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.social_group)
        self.actions_label = QtWidgets.QLabel(ShopInfo)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.actions_label.setFont(font)
        self.actions_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.actions_label.setObjectName("actions_label")
        self.info_layout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.actions_label)
        self.buttons_widget = QtWidgets.QWidget(ShopInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttons_widget.sizePolicy().hasHeightForWidth())
        self.buttons_widget.setSizePolicy(sizePolicy)
        self.buttons_widget.setMinimumSize(QtCore.QSize(250, 0))
        self.buttons_widget.setMaximumSize(QtCore.QSize(250, 16777215))
        self.buttons_widget.setObjectName("buttons_widget")
        self.button_layout = QtWidgets.QVBoxLayout(self.buttons_widget)
        self.button_layout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.button_layout.setContentsMargins(0, 0, 0, 0)
        self.button_layout.setObjectName("button_layout")
        self.open_store_button = QtWidgets.QPushButton(self.buttons_widget)
        self.open_store_button.setObjectName("open_store_button")
        self.button_layout.addWidget(self.open_store_button)
        self.wishlist_button = QtWidgets.QPushButton(self.buttons_widget)
        self.wishlist_button.setObjectName("wishlist_button")
        self.button_layout.addWidget(self.wishlist_button)
        self.info_layout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.buttons_widget)
        self.right_layout.addLayout(self.info_layout)
        self.requirements_group = QtWidgets.QFrame(ShopInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.requirements_group.sizePolicy().hasHeightForWidth())
        self.requirements_group.setSizePolicy(sizePolicy)
        self.requirements_group.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.requirements_group.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.requirements_group.setObjectName("requirements_group")
        self.requirements_layout = QtWidgets.QHBoxLayout(self.requirements_group)
        self.requirements_layout.setContentsMargins(0, 0, 0, 0)
        self.requirements_layout.setObjectName("requirements_layout")
        self.right_layout.addWidget(self.requirements_group)
        self.main_layout.addLayout(self.right_layout)
        self.main_layout.setStretch(1, 1)

        self.retranslateUi(ShopInfo)

    def retranslateUi(self, ShopInfo):
        _translate = QtCore.QCoreApplication.translate
        self.title_label.setText(_translate("ShopInfo", "Title"))
        self.developer_label.setText(_translate("ShopInfo", "Developer"))
        self.status_label.setText(_translate("ShopInfo", "Status"))
        self.owned_label.setText(_translate("ShopInfo", "You already own this game"))
        self.price_label.setText(_translate("ShopInfo", "Price"))
        self.tags_label.setText(_translate("ShopInfo", "Tags"))
        self.links_label.setText(_translate("ShopInfo", "Links"))
        self.actions_label.setText(_translate("ShopInfo", "Actions"))
        self.open_store_button.setText(_translate("ShopInfo", "Buy in Epic Games Store"))
        self.wishlist_button.setText(_translate("ShopInfo", "Add to wishlist"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ShopInfo = QtWidgets.QWidget()
    ui = Ui_ShopInfo()
    ui.setupUi(ShopInfo)
    ShopInfo.show()
    sys.exit(app.exec_())
