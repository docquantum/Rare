# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pathedit.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets


class Ui_PathEdit(object):
    def setupUi(self, PathEdit):
        PathEdit.setObjectName("PathEdit")
        self.layout_pathedit = QtWidgets.QGridLayout(PathEdit)
        self.layout_pathedit.setContentsMargins(0, 0, 0, 0)
        self.layout_pathedit.setObjectName("layout_pathedit")
        self.path_select = QtWidgets.QToolButton(PathEdit)
        self.path_select.setObjectName("path_select")
        self.layout_pathedit.addWidget(self.path_select, 0, 1, 1, 1)
        self.text_edit = QtWidgets.QLineEdit(PathEdit)
        self.text_edit.setMinimumSize(QtCore.QSize(300, 0))
        self.text_edit.setObjectName("text_edit")
        self.layout_pathedit.addWidget(self.text_edit, 0, 0, 1, 1)
        self.layout_pathedit_save = QtWidgets.QHBoxLayout()
        self.layout_pathedit_save.setObjectName("layout_pathedit_save")
        spacerItem = QtWidgets.QSpacerItem(40, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_pathedit_save.addItem(spacerItem)
        self.save_path_button = QtWidgets.QPushButton(PathEdit)
        self.save_path_button.setEnabled(True)
        self.save_path_button.setObjectName("save_path_button")
        self.layout_pathedit_save.addWidget(self.save_path_button)
        self.layout_pathedit.addLayout(self.layout_pathedit_save, 1, 0, 1, 2)

        self.retranslateUi(PathEdit)
        QtCore.QMetaObject.connectSlotsByName(PathEdit)

    def retranslateUi(self, PathEdit):
        _translate = QtCore.QCoreApplication.translate
        PathEdit.setWindowTitle(_translate("PathEdit", "PathEdit"))
        self.path_select.setText(_translate("PathEdit", "Browse..."))
        self.text_edit.setPlaceholderText(_translate("PathEdit", "Default"))
        self.save_path_button.setText(_translate("PathEdit", "Save"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    PathEdit = QtWidgets.QWidget()
    ui = Ui_PathEdit()
    ui.setupUi(PathEdit)
    PathEdit.show()
    sys.exit(app.exec_())
