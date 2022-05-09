# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(375, 191)
        Widget.setMinimumSize(QSize(0, 0))
        Widget.setMaximumSize(QSize(999999, 999999))
        self.horizontalLayout_4 = QHBoxLayout(Widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.lblGuess = QLabel(Widget)
        self.lblGuess.setObjectName(u"lblGuess")
        self.lblGuess.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lblGuess)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.intGuess = QLineEdit(Widget)
        self.intGuess.setObjectName(u"intGuess")
        self.intGuess.setAlignment(Qt.AlignCenter)
        self.intGuess.setReadOnly(True)

        self.horizontalLayout.addWidget(self.intGuess)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnLower = QPushButton(Widget)
        self.btnLower.setObjectName(u"btnLower")

        self.horizontalLayout_2.addWidget(self.btnLower)

        self.btnHigher = QPushButton(Widget)
        self.btnHigher.setObjectName(u"btnHigher")

        self.horizontalLayout_2.addWidget(self.btnHigher)

        self.btnCorrect = QPushButton(Widget)
        self.btnCorrect.setObjectName(u"btnCorrect")

        self.horizontalLayout_2.addWidget(self.btnCorrect)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btnRestart = QPushButton(Widget)
        self.btnRestart.setObjectName(u"btnRestart")

        self.horizontalLayout_3.addWidget(self.btnRestart)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Guessing Game", None))
#if QT_CONFIG(accessibility)
        Widget.setAccessibleName(QCoreApplication.translate("Widget", u"Guessing Game", None))
#endif // QT_CONFIG(accessibility)
        self.label.setText(QCoreApplication.translate("Widget", u"This program can guess the number you're thinking of between 1-100 within 7 guesses!", None))
        self.lblGuess.setText("")
        self.btnLower.setText(QCoreApplication.translate("Widget", u"Lower", None))
        self.btnHigher.setText(QCoreApplication.translate("Widget", u"Higher", None))
        self.btnCorrect.setText(QCoreApplication.translate("Widget", u"Correct", None))
        self.btnRestart.setText(QCoreApplication.translate("Widget", u"Restart", None))
    # retranslateUi

