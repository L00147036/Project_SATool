from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_resultsWindow(object):
    def setupUi(self, resultsWindow):
        resultsWindow.setObjectName("resultsWindow")
        resultsWindow.resize(800, 618)
        self.centralwidget = QtWidgets.QWidget(resultsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.results_ResultsBreakdown = QtWidgets.QLabel(self.centralwidget)
        self.results_ResultsBreakdown.setGeometry(QtCore.QRect(10, 25, 311, 451))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.results_ResultsBreakdown.setFont(font)
        self.results_ResultsBreakdown.setAlignment(QtCore.Qt.AlignCenter)
        self.results_ResultsBreakdown.setWordWrap(True)
        self.results_ResultsBreakdown.setObjectName("results_ResultsBreakdown")
        self.results_SaveBtn = QtWidgets.QPushButton(self.centralwidget)
        self.results_SaveBtn.setGeometry(QtCore.QRect(100, 490, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.results_SaveBtn.setFont(font)
        self.results_SaveBtn.setObjectName("results_SaveBtn")
        self.results_StartOverBtn = QtWidgets.QPushButton(self.centralwidget)
        self.results_StartOverBtn.setGeometry(QtCore.QRect(100, 540, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.results_StartOverBtn.setFont(font)
        self.results_StartOverBtn.setObjectName("results_StartOverBtn")
        self.results_AnalysisResults = QtWidgets.QListWidget(self.centralwidget)
        self.results_AnalysisResults.setGeometry(QtCore.QRect(330, 10, 451, 551))
        self.results_AnalysisResults.setObjectName("results_AnalysisResults")
        resultsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(resultsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        resultsWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(resultsWindow)
        self.statusbar.setObjectName("statusbar")
        resultsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(resultsWindow)
        QtCore.QMetaObject.connectSlotsByName(resultsWindow)

    def retranslateUi(self, resultsWindow):
        _translate = QtCore.QCoreApplication.translate
        resultsWindow.setWindowTitle(_translate("resultsWindow", "Analysis results"))
        self.results_ResultsBreakdown.setText(_translate("resultsWindow", "Click on a sentence in the list to show a breakdown of its emotion here."))
        self.results_SaveBtn.setToolTip(_translate("resultsWindow", "Save the results of the sentiment analysis as a text file."))
        self.results_SaveBtn.setText(_translate("resultsWindow", "Save results"))
        self.results_SaveBtn.setShortcut(_translate("resultsWindow", "Ctrl+C"))
        self.results_StartOverBtn.setToolTip(_translate("resultsWindow", "Delete the results of the analysis & start over with a new piece of text."))
        self.results_StartOverBtn.setText(_translate("resultsWindow", "Start over"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    resultsWindow = QtWidgets.QMainWindow()
    ui = Ui_resultsWindow()
    ui.setupUi(resultsWindow)
    resultsWindow.show()
    sys.exit(app.exec_())
