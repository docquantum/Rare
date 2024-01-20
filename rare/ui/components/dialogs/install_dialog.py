# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rare/ui/components/dialogs/install_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InstallDialog(object):
    def setupUi(self, InstallDialog):
        InstallDialog.setObjectName("InstallDialog")
        InstallDialog.resize(197, 195)
        InstallDialog.setWindowTitle("InstallDialog")
        self.main_layout = QtWidgets.QFormLayout(InstallDialog)
        self.main_layout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.main_layout.setObjectName("main_layout")
        self.install_dir_label = QtWidgets.QLabel(InstallDialog)
        self.install_dir_label.setObjectName("install_dir_label")
        self.main_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.install_dir_label)
        self.platform_label = QtWidgets.QLabel(InstallDialog)
        self.platform_label.setObjectName("platform_label")
        self.main_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.platform_label)
        self.platform_combo = QtWidgets.QComboBox(InstallDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.platform_combo.sizePolicy().hasHeightForWidth())
        self.platform_combo.setSizePolicy(sizePolicy)
        self.platform_combo.setObjectName("platform_combo")
        self.main_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.platform_combo)
        self.shortcut_label = QtWidgets.QLabel(InstallDialog)
        self.shortcut_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.shortcut_label.setObjectName("shortcut_label")
        self.main_layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.shortcut_label)
        self.shortcut_check = QtWidgets.QCheckBox(InstallDialog)
        self.shortcut_check.setText("")
        self.shortcut_check.setObjectName("shortcut_check")
        self.main_layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.shortcut_check)
        self.selectable_layout = QtWidgets.QVBoxLayout()
        self.selectable_layout.setObjectName("selectable_layout")
        self.main_layout.setLayout(3, QtWidgets.QFormLayout.SpanningRole, self.selectable_layout)
        self.advanced_layout = QtWidgets.QVBoxLayout()
        self.advanced_layout.setObjectName("advanced_layout")
        self.main_layout.setLayout(4, QtWidgets.QFormLayout.SpanningRole, self.advanced_layout)
        self.download_size_label = QtWidgets.QLabel(InstallDialog)
        self.download_size_label.setObjectName("download_size_label")
        self.main_layout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.download_size_label)
        self.download_size_text = QtWidgets.QLabel(InstallDialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.download_size_text.setFont(font)
        self.download_size_text.setObjectName("download_size_text")
        self.main_layout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.download_size_text)
        self.install_size_label = QtWidgets.QLabel(InstallDialog)
        self.install_size_label.setObjectName("install_size_label")
        self.main_layout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.install_size_label)
        self.install_size_text = QtWidgets.QLabel(InstallDialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.install_size_text.setFont(font)
        self.install_size_text.setWordWrap(True)
        self.install_size_text.setObjectName("install_size_text")
        self.main_layout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.install_size_text)
        self.avail_space_label = QtWidgets.QLabel(InstallDialog)
        self.avail_space_label.setObjectName("avail_space_label")
        self.main_layout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.avail_space_label)
        self.avail_space = QtWidgets.QLabel(InstallDialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.avail_space.setFont(font)
        self.avail_space.setText("")
        self.avail_space.setObjectName("avail_space")
        self.main_layout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.avail_space)
        self.warning_label = QtWidgets.QLabel(InstallDialog)
        self.warning_label.setObjectName("warning_label")
        self.main_layout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.warning_label)
        self.warning_text = QtWidgets.QLabel(InstallDialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.warning_text.setFont(font)
        self.warning_text.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.warning_text.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.warning_text.setWordWrap(True)
        self.warning_text.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.warning_text.setObjectName("warning_text")
        self.main_layout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.warning_text)

        self.retranslateUi(InstallDialog)

    def retranslateUi(self, InstallDialog):
        _translate = QtCore.QCoreApplication.translate
        self.install_dir_label.setText(_translate("InstallDialog", "Install folder"))
        self.platform_label.setText(_translate("InstallDialog", "Platform"))
        self.shortcut_label.setText(_translate("InstallDialog", "Create shortcut"))
        self.download_size_label.setText(_translate("InstallDialog", "Download size"))
        self.download_size_text.setText(_translate("InstallDialog", "Click verify..."))
        self.install_size_label.setText(_translate("InstallDialog", "Total install size"))
        self.install_size_text.setText(_translate("InstallDialog", "Click verify..."))
        self.avail_space_label.setText(_translate("InstallDialog", "Available space"))
        self.warning_label.setText(_translate("InstallDialog", "Warning"))
        self.warning_text.setText(_translate("InstallDialog", "None"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InstallDialog = QtWidgets.QWidget()
    ui = Ui_InstallDialog()
    ui.setupUi(InstallDialog)
    InstallDialog.show()
    sys.exit(app.exec_())
