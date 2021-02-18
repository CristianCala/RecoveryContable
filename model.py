import sys
import os
from vista import *
from controller import *

from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtGui import (QFont, QIcon, QPalette, QBrush, QColor, QPixmap, QRegion, QClipboard,
						 QRegExpValidator, QImage)
from PyQt5.QtCore import (Qt, QDir, pyqtSignal, QFile, QByteArray,QIODevice,QBuffer,QDate, QTime, QSize, QTimer, QRect, QRegExp, QTranslator,QLocale,
						  QLocale, QLibraryInfo, QFileInfo, QDir,QPropertyAnimation,QTranslator,QAbstractAnimation, QLocale)

from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QDialog, QTableWidget, QMenu, 
							 QTableWidgetItem, QAbstractItemView, QLineEdit, QPushButton,
							 QActionGroup, QAction, QMessageBox, QFrame, QStyle, QGridLayout,
							 QVBoxLayout, QHBoxLayout, QLabel, QToolButton, QGroupBox,
							 QDateEdit, QComboBox, QCheckBox, QTextEdit, QRadioButton, QScrollArea, QFileDialog,QGraphicsEffect, QVBoxLayout, 
							 QGraphicsDropShadowEffect, QGraphicsBlurEffect)

class Startup(QDialog):
	def __init__(self, parent=None):
		QDialog.__init__(self)
		self.setFixedSize(500,600)
		self.setWindowTitle("RecoveryContable")
		self.setStyleSheet(backgroundStartup)

		self.initModel()

	def initModel(self):

		self.buttonInit = QPushButton(self)
		self.buttonInit.setGeometry(QRect(0,0,200,60))
		self.buttonInit.move(150,450)
		self.buttonInit.setText("INICIO")
		self.buttonInit.setStyleSheet(buttonStartup)
		self.buttonInit.setFont(QtGui.QFont("Roboto", 17, QtGui.QFont.Bold))
		self.shadow  = QGraphicsDropShadowEffect()        
		self.shadow.setBlurRadius(22)
		self.buttonInit.setGraphicsEffect(self.shadow)
		self.buttonInit.clicked.connect(self.openMain)


	def openMain(self):
		self.interfaceMain = mainWindow()
		self.interfaceMain.show()
		self.close()


class mainWindow(QMainWindow):
	def __init__(self, parent=None):
		QMainWindow.__init__(self)
		self.setFixedSize(900,600)
		self.setWindowTitle("RecoveryContable")
		self.setStyleSheet(backgroundMain)

		self.initModel()

	def initModel(self):
		
		# Status Bar -------------------------------------
		self.statusBar = QFrame(self)
		self.statusBar.setGeometry(QRect(0,0,200,600))
		self.statusBar.setStyleSheet(statusBarFrame)
		self.statusBar.move(0, 0)

		self.title = QLabel(self.statusBar)
		self.title.setGeometry(QRect(0,0,150,100))
		self.title.setText("RecoveryLoid")
		self.title.setStyleSheet(titleStyle)
		self.title.setFont(QtGui.QFont("Roboto", 17, QtGui.QFont.Bold))
		self.title.move(30, 0)

		self.buttonArrow = QPushButton(self)
		self.buttonArrow.setGeometry(QRect(0,0,30,45))
		self.buttonArrow.move(200,100)
		self.buttonArrow.setStyleSheet(buttonArrowStatusBar)
		self.buttonArrow.setIcon(QIcon("arrow white-1.svg"))
		self.buttonArrow.clicked.connect(self.slide)

		self.buttonArrowDown = QPushButton(self.statusBar)
		self.buttonArrowDown.setGeometry(QRect(0,0,30,45))
		self.buttonArrowDown.move(170,100)
		self.buttonArrowDown.setStyleSheet(buttonArrowStatusBarDown)
		self.buttonArrowDown.setIcon(QIcon("arrow-white.png"))
		self.buttonArrowDown.clicked.connect(self.slideDown)

		self.buttonPago = QPushButton(self.statusBar)
		self.buttonPago.setGeometry(QRect(0,0,200,40))
		self.buttonPago.move(0,200)
		self.buttonPago.setText("PAGO")
		self.buttonPago.setStyleSheet(buttonStatusBar)
		self.buttonPago.setFont(QtGui.QFont("Roboto", 14, QtGui.QFont.Bold))

		self.buttonRetiro = QPushButton(self.statusBar)
		self.buttonRetiro.setGeometry(QRect(0,0,200,40))
		self.buttonRetiro.move(0,245)
		self.buttonRetiro.setText("RETIRO")
		self.buttonRetiro.setStyleSheet(buttonStatusBar)
		self.buttonRetiro.setFont(QtGui.QFont("Roboto", 14, QtGui.QFont.Bold))

		self.buttonAcerca = QPushButton(self.statusBar)
		self.buttonAcerca.setGeometry(QRect(0,0,100,40))
		self.buttonAcerca.move(50,500)
		self.buttonAcerca.setText("Acerca de")
		self.buttonAcerca.setStyleSheet(buttonAcercade)
		self.buttonAcerca.setFont(QtGui.QFont("Roboto", 11, QtGui.QFont.Condensed))

		# Frame Estadisticas
		self.statisticFrame = QFrame(self)
		self.statisticFrame.setGeometry(QRect(0,0,500,400))
		self.statisticFrame.move(300,100)
		self.statisticFrame.setStyleSheet(statisticStatusFrame)

		self.statisticTitle = QLabel(self)
		self.statisticTitle.setText("ESTADÍSTICAS")
		self.statisticTitle.setFont(QtGui.QFont("Roboto", 25, QtGui.QFont.Bold))
		self.statisticTitle.setGeometry(QRect(0,0,500,100))
		self.statisticTitle.move(450,0)
		self.statisticTitle.setStyleSheet(titleStyle)

		self.buttonEstadoArrow = QPushButton(self)
		self.buttonEstadoArrow.setGeometry(QRect(0,0,40,40))
		self.buttonEstadoArrow.move(260,50)
		self.buttonEstadoArrow.setIcon(QIcon("arrow white-1.svg"))
		self.buttonEstadoArrow.setStyleSheet(universalArrowSlide)
		self.buttonEstadoArrow.clicked.connect(self.slideToState)

		self.buttonLibroArrow = QPushButton(self)
		self.buttonLibroArrow.setGeometry(QRect(0,0,40,40))
		self.buttonLibroArrow.move(800,50)
		self.buttonLibroArrow.setIcon(QIcon("arrow-white.png"))
		self.buttonLibroArrow.setStyleSheet(universalArrowSlide)
		self.buttonLibroArrow.clicked.connect(self.slideToBook)

		self.statisticTotal = QLabel(self.statisticFrame)
		self.statisticTotal.setText("Total")
		self.statisticTotal.setFont(QtGui.QFont("Roboto", 15, QtGui.QFont.Bold))
		self.statisticTotal.setGeometry(QRect(0,0,100,100))
		self.statisticTotal.move(350,0)
		self.statisticTotal.setStyleSheet(statisticLetter)

		self.statisticRecovery = QLabel(self.statisticFrame)
		self.statisticRecovery.setText("RecoveryLoid")
		self.statisticRecovery.setFont(QtGui.QFont("Roboto", 15, QtGui.QFont.Bold))
		self.statisticRecovery.setGeometry(QRect(0,0,150,100))
		self.statisticRecovery.move(100,0)
		self.statisticRecovery.setStyleSheet(statisticLetter)

		self.statisticLine = QLabel(self.statisticFrame)
		self.statisticLine.setText("---------------->")
		self.statisticLine.setFont(QtGui.QFont("Roboto", 15, QtGui.QFont.Bold))
		self.statisticLine.setGeometry(QRect(0,0,150,100))
		self.statisticLine.move(100,50)
		self.statisticLine.setStyleSheet(statisticLetter)

		self.statisticMount = QLabel(self.statisticFrame)
		self.statisticMount.setText("0.00" + "$")
		self.statisticMount.setFont(QtGui.QFont("Roboto", 15, QtGui.QFont.Thin))
		self.statisticMount.setGeometry(QRect(0,0,100,100))
		self.statisticMount.move(350,50)
		self.statisticMount.setStyleSheet(statisticLetter)

		self.statisticMount = QLabel(self.statisticFrame)
		self.statisticMount.setGeometry(QRect(0,0,100,2))
		self.statisticMount.move(325,70)
		self.statisticMount.setStyleSheet(statisticSeparata)

		# Frame Libro
		self.bookFrame = QFrame(self)
		self.bookFrame.setGeometry(QRect(0,0,700,400))
		self.bookFrame.move(5000,100)
		self.bookFrame.setStyleSheet(statisticStatusFrame)

		self.buttonArrowInBook = QPushButton(self)
		self.buttonArrowInBook.setGeometry(QRect(0,0,40,40))
		self.buttonArrowInBook.move(260,5000)
		self.buttonArrowInBook.setIcon(QIcon("arrow white-1.svg"))
		self.buttonArrowInBook.setStyleSheet(universalArrowSlide)
		self.buttonArrowInBook.clicked.connect(self.fromBookToStatistic)

		nameColumns = ("Ref", "Fecha", "Descripción", "Ingreso/Egreso",
		 "Monto Actual")
		self.bookTable = QTableWidget(self.bookFrame)
		self.bookTable.setToolTip("Transacción")
		self.bookTable.setGeometry(QRect(0,0,600,400))
		self.bookTable.setStyleSheet(bookQTable)
		self.bookTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.bookTable.setDragDropOverwriteMode(False)
		self.bookTable.setSelectionBehavior(QAbstractItemView.SelectRows)
		self.bookTable.setSelectionMode(QAbstractItemView.SingleSelection)
		self.bookTable.setTextElideMode(Qt.ElideRight)
		self.bookTable.setWordWrap(False)
		self.bookTable.setSortingEnabled(False)
		self.bookTable.setColumnCount(5)
		self.bookTable.setRowCount(0)
		self.bookTable.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter|Qt.AlignVCenter|Qt.AlignCenter)
		self.bookTable.horizontalHeader().setHighlightSections(False)
		self.bookTable.horizontalHeader().setStretchLastSection(True)
		self.bookTable.verticalHeader().setVisible(False)
		self.bookTable.setAlternatingRowColors(False)
		self.bookTable.verticalHeader().setDefaultSectionSize(20)
		self.bookTable.setHorizontalHeaderLabels(nameColumns)

		for index, large in enumerate((110, 110, 110, 110, 130), start=0):
			self.bookTable.setColumnWidth(index, large)


		# Frame State 
		self.stateFrame = QFrame(self)
		self.stateFrame.setGeometry(QRect(0,0,500,400))
		self.stateFrame.move(5000,100)
		self.stateFrame.setStyleSheet(statisticStatusFrame)

		self.buttonArrowInState = QPushButton(self)
		self.buttonArrowInState.setGeometry(QRect(0,0,40,40))
		self.buttonArrowInState.move(800,5000)
		self.buttonArrowInState.setIcon(QIcon("arrow-white.png"))
		self.buttonArrowInState.setStyleSheet(universalArrowSlide)
		self.buttonArrowInState.clicked.connect(self.fromStateToStatistic)


	# Slide de libro a estadisticas
	def fromBookToStatistic(self):
		self.statisticTitle.setText("ESTADÍSTICAS")

		# Previous Frame
		self.animationSlidePreviousFrame = QPropertyAnimation(self.bookFrame,b"geometry")
		self.animationSlidePreviousFrame.finished.connect(lambda: (self.bookFrame))

		self.animationSlidePreviousFrame.setDuration(900)
		self.animationSlidePreviousFrame.setStartValue(QRect(300,100,500,400))
		self.animationSlidePreviousFrame.setEndValue(QRect(5000,100,500,400))
		self.animationSlidePreviousFrame.start(QAbstractAnimation.DeleteWhenStopped)

		# ArrowInState
		self.animationSlideArrowInState = QPropertyAnimation(self.buttonArrowInBook,b"geometry")
		self.animationSlideArrowInState.finished.connect(lambda: (self.buttonArrowInBook))

		self.animationSlideArrowInState.setDuration(900)
		self.animationSlideArrowInState.setStartValue(QRect(250,50,40,40))
		self.animationSlideArrowInState.setEndValue(QRect(5000,50,40,40))
		self.animationSlideArrowInState.start(QAbstractAnimation.DeleteWhenStopped)


		# Next Frame
		self.animationSlideFrame = QPropertyAnimation(self.statisticFrame,b"geometry")
		self.animationSlideFrame.finished.connect(lambda: (self.statisticFrame))

		self.animationSlideFrame.setDuration(900)
		self.animationSlideFrame.setStartValue(QRect(-5000,100,500,400))
		self.animationSlideFrame.setEndValue(QRect(300,100,500,400))
		self.animationSlideFrame.start(QAbstractAnimation.DeleteWhenStopped)

		# Arrows 
		self.animationSlideArrow = QPropertyAnimation(self.buttonEstadoArrow,b"geometry")
		self.animationSlideArrow.finished.connect(lambda: (self.buttonEstadoArrow))

		self.animationSlideArrow.setDuration(900)
		self.animationSlideArrow.setStartValue(QRect(-5000,50,40,40))
		self.animationSlideArrow.setEndValue(QRect(260,50,40,40))
		self.animationSlideArrow.start(QAbstractAnimation.DeleteWhenStopped)

		self.animationSlideArrow2 = QPropertyAnimation(self.buttonLibroArrow,b"geometry")
		self.animationSlideArrow2.finished.connect(lambda: (self.buttonLibroArrow))

		self.animationSlideArrow2.setDuration(900)
		self.animationSlideArrow2.setStartValue(QRect(-5000,50,40,40))
		self.animationSlideArrow2.setEndValue(QRect(800,50,40,40))
		self.animationSlideArrow2.start(QAbstractAnimation.DeleteWhenStopped)

		return True

	# Slide de Stado a estadisticas
	def fromStateToStatistic(self):
		self.statisticTitle.setText("ESTADÍSTICAS")
		self.statisticTitle.move(450,0)

		# Previous Frame
		self.animationSlidePreviousFrame = QPropertyAnimation(self.stateFrame,b"geometry")
		self.animationSlidePreviousFrame.finished.connect(lambda: (self.stateFrame))

		self.animationSlidePreviousFrame.setDuration(900)
		self.animationSlidePreviousFrame.setStartValue(QRect(300,100,500,400))
		self.animationSlidePreviousFrame.setEndValue(QRect(-5000,100,500,400))
		self.animationSlidePreviousFrame.start(QAbstractAnimation.DeleteWhenStopped)

		self.animationSlideArrowState = QPropertyAnimation(self.buttonArrowInState,b"geometry")
		self.animationSlideArrowState.finished.connect(lambda: (self.buttonArrowInState))

		self.animationSlideArrowState.setDuration(900)
		self.animationSlideArrowState.setStartValue(QRect(800,50,40,40))
		self.animationSlideArrowState.setEndValue(QRect(-5000,50,40,40))
		self.animationSlideArrowState.start(QAbstractAnimation.DeleteWhenStopped)

		# Next Frame
		self.animationSlideFrame = QPropertyAnimation(self.statisticFrame,b"geometry")
		self.animationSlideFrame.finished.connect(lambda: (self.statisticFrame))

		self.animationSlideFrame.setDuration(900)
		self.animationSlideFrame.setStartValue(QRect(5000,100,500,400))
		self.animationSlideFrame.setEndValue(QRect(300,100,500,400))
		self.animationSlideFrame.start(QAbstractAnimation.DeleteWhenStopped)

		# Arrows 
		self.animationSlideArrow = QPropertyAnimation(self.buttonEstadoArrow,b"geometry")
		self.animationSlideArrow.finished.connect(lambda: (self.buttonEstadoArrow))

		self.animationSlideArrow.setDuration(900)
		self.animationSlideArrow.setStartValue(QRect(5000,50,40,40))
		self.animationSlideArrow.setEndValue(QRect(260,50,40,40))
		self.animationSlideArrow.start(QAbstractAnimation.DeleteWhenStopped)

		self.animationSlideArrow2 = QPropertyAnimation(self.buttonLibroArrow,b"geometry")
		self.animationSlideArrow2.finished.connect(lambda: (self.buttonLibroArrow))

		self.animationSlideArrow2.setDuration(900)
		self.animationSlideArrow2.setStartValue(QRect(5000,50,40,40))
		self.animationSlideArrow2.setEndValue(QRect(800,50,40,40))
		self.animationSlideArrow2.start(QAbstractAnimation.DeleteWhenStopped)

		return True

	# Slide a libro
	def slideToBook(self):

		self.statisticTitle.setText("Libro de Registro")
		self.statisticTitle.move(400,0)

		# Previous Frame
		self.animationSlidePreviousFrame = QPropertyAnimation(self.statisticFrame,b"geometry")
		self.animationSlidePreviousFrame.finished.connect(lambda: (self.statisticFrame))

		self.animationSlidePreviousFrame.setDuration(900)
		self.animationSlidePreviousFrame.setStartValue(QRect(300,100,500,400))
		self.animationSlidePreviousFrame.setEndValue(QRect(-5000,100,500,400))
		self.animationSlidePreviousFrame.start(QAbstractAnimation.DeleteWhenStopped)

		# Arrows 
		self.animationSlideArrow = QPropertyAnimation(self.buttonEstadoArrow,b"geometry")
		self.animationSlideArrow.finished.connect(lambda: (self.buttonEstadoArrow))

		self.animationSlideArrow.setDuration(900)
		self.animationSlideArrow.setStartValue(QRect(260,50,40,40))
		self.animationSlideArrow.setEndValue(QRect(-5000,100,40,40))
		self.animationSlideArrow.start(QAbstractAnimation.DeleteWhenStopped)

		self.animationSlideArrow2 = QPropertyAnimation(self.buttonLibroArrow,b"geometry")
		self.animationSlideArrow2.finished.connect(lambda: (self.buttonLibroArrow))

		self.animationSlideArrow2.setDuration(900)
		self.animationSlideArrow2.setStartValue(QRect(800,50,40,40))
		self.animationSlideArrow2.setEndValue(QRect(-5000,50,40,40))
		self.animationSlideArrow2.start(QAbstractAnimation.DeleteWhenStopped)

		# Next Frame
		self.animationSlideFrame = QPropertyAnimation(self.bookFrame,b"geometry")
		self.animationSlideFrame.finished.connect(lambda: (self.bookFrame))

		self.animationSlideFrame.setDuration(900)
		self.animationSlideFrame.setStartValue(QRect(5000,100,500,400))
		self.animationSlideFrame.setEndValue(QRect(200,100,600,400))
		self.animationSlideFrame.start(QAbstractAnimation.DeleteWhenStopped)

		self.animationSlideArrowInState = QPropertyAnimation(self.buttonArrowInBook,b"geometry")
		self.animationSlideArrowInState.finished.connect(lambda: (self.buttonArrowInBook))

		self.animationSlideArrowInState.setDuration(900)
		self.animationSlideArrowInState.setStartValue(QRect(5000,50,40,40))
		self.animationSlideArrowInState.setEndValue(QRect(250,50,40,40))
		self.animationSlideArrowInState.start(QAbstractAnimation.DeleteWhenStopped)

		return True
	
	# Slide a Estado
	def slideToState(self):
		self.statisticTitle.setText("ESTADO")
		self.statisticTitle.move(500,0)

		# Previous Frame
		self.animationSlidePreviousFrame = QPropertyAnimation(self.statisticFrame,b"geometry")
		self.animationSlidePreviousFrame.finished.connect(lambda: (self.statisticFrame))

		self.animationSlidePreviousFrame.setDuration(900)
		self.animationSlidePreviousFrame.setStartValue(QRect(300,100,500,400))
		self.animationSlidePreviousFrame.setEndValue(QRect(5000,100,500,400))
		self.animationSlidePreviousFrame.start(QAbstractAnimation.DeleteWhenStopped)

		# Arrows 
		self.animationSlideArrow = QPropertyAnimation(self.buttonEstadoArrow,b"geometry")
		self.animationSlideArrow.finished.connect(lambda: (self.buttonEstadoArrow))

		self.animationSlideArrow.setDuration(900)
		self.animationSlideArrow.setStartValue(QRect(260,50,40,40))
		self.animationSlideArrow.setEndValue(QRect(5000,100,40,40))
		self.animationSlideArrow.start(QAbstractAnimation.DeleteWhenStopped)

		self.animationSlideArrow2 = QPropertyAnimation(self.buttonLibroArrow,b"geometry")
		self.animationSlideArrow2.finished.connect(lambda: (self.buttonLibroArrow))

		self.animationSlideArrow2.setDuration(900)
		self.animationSlideArrow2.setStartValue(QRect(800,50,40,40))
		self.animationSlideArrow2.setEndValue(QRect(5000,50,40,40))
		self.animationSlideArrow2.start(QAbstractAnimation.DeleteWhenStopped)

		# Next Frame
		self.animationSlideFrame = QPropertyAnimation(self.stateFrame,b"geometry")
		self.animationSlideFrame.finished.connect(lambda: (self.stateFrame))

		self.animationSlideFrame.setDuration(900)
		self.animationSlideFrame.setStartValue(QRect(-5000,100,500,400))
		self.animationSlideFrame.setEndValue(QRect(300,100,500,400))
		self.animationSlideFrame.start(QAbstractAnimation.DeleteWhenStopped)

		self.animationSlideArrowState = QPropertyAnimation(self.buttonArrowInState,b"geometry")
		self.animationSlideArrowState.finished.connect(lambda: (self.buttonArrowInState))

		self.animationSlideArrowState.setDuration(900)
		self.animationSlideArrowState.setStartValue(QRect(-5000,50,40,40))
		self.animationSlideArrowState.setEndValue(QRect(800,50,40,40))
		self.animationSlideArrowState.start(QAbstractAnimation.DeleteWhenStopped)

		return True

	# Slides Status bar
	def slide(self):
		# Titulo
		self.title.setText("RC")
		self.title.move(10, 0)
		# statusBar
		self.animationSlide = QPropertyAnimation(self.statusBar,b"geometry")
		self.animationSlide.finished.connect(lambda: (self.statusBar))

		self.animationSlide.setDuration(900)
		self.animationSlide.setStartValue(QRect(0,0,200,600))
		self.animationSlide.setEndValue(QRect(0,0,50,600))
		self.animationSlide.start(QAbstractAnimation.DeleteWhenStopped)

		# Flecha
		self.animationSlideArrow = QPropertyAnimation(self.buttonArrow, b"geometry")
		self.animationSlideArrow.finished.connect(lambda: (self.buttonArrow))

		self.animationSlideArrow.setDuration(900)
		self.animationSlideArrow.setStartValue(QRect(200,100,30,45))
		self.animationSlideArrow.setEndValue(QRect(50,100,30,45))
		self.animationSlideArrow.start(QAbstractAnimation.DeleteWhenStopped)

		# FlechaDown
		self.animationSlideArrowDown = QPropertyAnimation(self.buttonArrowDown, b"geometry")
		self.animationSlideArrowDown.finished.connect(lambda: (self.buttonArrowDown))

		self.animationSlideArrowDown.setDuration(900)
		self.animationSlideArrowDown.setStartValue(QRect(170,100,30,45))
		self.animationSlideArrowDown.setEndValue(QRect(20,100,30,45))
		self.animationSlideArrowDown.start(QAbstractAnimation.DeleteWhenStopped)

		# Pago
		self.animationSlidePago = QPropertyAnimation(self.buttonPago, b"geometry")
		self.animationSlidePago.finished.connect(lambda: (self.buttonPago))

		self.animationSlidePago.setDuration(900)
		self.animationSlidePago.setStartValue(QRect(0,200,200,40))
		self.animationSlidePago.setEndValue(QRect(0,200,50,40))
		self.animationSlidePago.start(QAbstractAnimation.DeleteWhenStopped)
		self.buttonPago.setText("P")

		# Retiro
		self.animationSlideRetiro = QPropertyAnimation(self.buttonRetiro, b"geometry")
		self.animationSlideRetiro.finished.connect(lambda: (self.buttonRetiro))

		self.animationSlideRetiro.setDuration(900)
		self.animationSlideRetiro.setStartValue(QRect(0,245,200,40))
		self.animationSlideRetiro.setEndValue(QRect(0,245,50,40))
		self.animationSlideRetiro.start(QAbstractAnimation.DeleteWhenStopped)
		self.buttonRetiro.setText("R")

		# Acerca
		self.animationSlideAcerca = QPropertyAnimation(self.buttonAcerca, b"geometry")
		self.animationSlideAcerca.finished.connect(lambda: (self.buttonAcerca))

		self.animationSlideAcerca.setDuration(900)
		self.animationSlideAcerca.setStartValue(QRect(50,500,100,40))
		self.animationSlideAcerca.setEndValue(QRect(0,500,50,40))
		self.animationSlideAcerca.start(QAbstractAnimation.DeleteWhenStopped)
		self.buttonAcerca.setText("Ac")

	def slideDown(self):
		# Titulo
		self.title.setText("RecoveryLoid")
		self.title.move(30, 0)
		# statusBar
		self.animationSlide = QPropertyAnimation(self.statusBar,b"geometry")
		self.animationSlide.finished.connect(lambda: (self.statusBar))

		self.animationSlide.setDuration(900)
		self.animationSlide.setStartValue(QRect(0,0,50,600))
		self.animationSlide.setEndValue(QRect(0,0,200,600))
		self.animationSlide.start(QAbstractAnimation.DeleteWhenStopped)

		# Flecha
		self.animationSlideArrow = QPropertyAnimation(self.buttonArrow, b"geometry")
		self.animationSlideArrow.finished.connect(lambda: (self.buttonArrow))

		self.animationSlideArrow.setDuration(900)
		self.animationSlideArrow.setStartValue(QRect(50,100,30,45))
		self.animationSlideArrow.setEndValue(QRect(200,100,30,45))
		self.animationSlideArrow.start(QAbstractAnimation.DeleteWhenStopped)

		# FlechaDown
		self.animationSlideArrowDown = QPropertyAnimation(self.buttonArrowDown, b"geometry")
		self.animationSlideArrowDown.finished.connect(lambda: (self.buttonArrowDown))

		self.animationSlideArrowDown.setDuration(900)
		self.animationSlideArrowDown.setStartValue(QRect(30,100,30,45))
		self.animationSlideArrowDown.setEndValue(QRect(170,100,30,45))
		self.animationSlideArrowDown.start(QAbstractAnimation.DeleteWhenStopped)

		# Pago
		self.animationSlidePago = QPropertyAnimation(self.buttonPago, b"geometry")
		self.animationSlidePago.finished.connect(lambda: (self.buttonPago))

		self.animationSlidePago.setDuration(900)
		self.animationSlidePago.setStartValue(QRect(0,200,50,40))
		self.animationSlidePago.setEndValue(QRect(0,200,200,40))
		self.animationSlidePago.start(QAbstractAnimation.DeleteWhenStopped)
		self.buttonPago.setText("PAGO")

		# Retiro
		self.animationSlideRetiro = QPropertyAnimation(self.buttonRetiro, b"geometry")
		self.animationSlideRetiro.finished.connect(lambda: (self.buttonRetiro))

		self.animationSlideRetiro.setDuration(900)
		self.animationSlideRetiro.setStartValue(QRect(0,245,50,40))
		self.animationSlideRetiro.setEndValue(QRect(0,245,200,40))
		self.animationSlideRetiro.start(QAbstractAnimation.DeleteWhenStopped)
		self.buttonRetiro.setText("RETIRO")

		# Acerca
		self.animationSlideAcerca = QPropertyAnimation(self.buttonAcerca, b"geometry")
		self.animationSlideAcerca.finished.connect(lambda: (self.buttonAcerca))

		self.animationSlideAcerca.setDuration(900)
		self.animationSlideAcerca.setStartValue(QRect(0,500,50,40))
		self.animationSlideAcerca.setEndValue(QRect(50,500,100,40))
		self.animationSlideAcerca.start(QAbstractAnimation.DeleteWhenStopped)
		self.buttonAcerca.setText("Acerca de")


		return True


if __name__ == "__main__":
	app = QApplication(sys.argv)
	interface = Startup()
	interface.show()
	app.exec_()