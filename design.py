from PyQt6 import QtWidgets, uic, QtGui, QtCore
from KcDobot import *
import os

gs = True
bs = True
pose = [0,0,0]
app = QtWidgets.QApplication([])
ui = uic.loadUi("design.ui")
ui.setWindowTitle("Dobot")
ui.setFixedSize(509, 387)

font12=QtGui.QFont("MS Shell Dlg 2",12)
font8=QtGui.QFont("MS Shell Dlg 2",8)
font12.setBold(True)
font8.setBold(True)
ui.label_3.setFont(font12)
ui.label_4.setFont(font12)
ui.label_5.setFont(font12)
ui.label_6.setFont(font12)
ui.label_7.setFont(font12)
ui.label_8.setFont(font12)
ui.label_9.setFont(font8)
ui.railMove.setFont(font8)
ui.convMove.setFont(font8)
ui.pushButton.setFont(font8)
ui.pushButton_2.setFont(font8)
ui.connectButton.setFont(font8)
ui.homeButton.setFont(font8)
ui.socButton.setFont(font8)
ui.gripButton.setFont(font8)
ui.currentBox.setFont(font8)
ui.currentBox2.setFont(font8)
ui.currentBox3.setFont(font8)
ui.setBox.setFont(font8)
ui.setBox2.setFont(font8)
ui.setBox3.setFont(font8)
ui.railBox.setFont(font8)
ui.convBox.setFont(font8)
ui.connectButton.setStyleSheet('QPushButton {background-color: green; color: white;}')
ui.label_9.setStyleSheet('QLabel {color: red;}')
Button_style = ui.socButton.styleSheet()
label_style = ui.label_3.styleSheet()
threadpool = QtCore.QThreadPool()
t = 0
class AThread(QtCore.QThread):
    global t
    def run(self):
        while t == 0:
            pose = getPose()
            ui.currentBox.setValue(int(pose[0]))
            ui.currentBox2.setValue(int(pose[1]))
            ui.currentBox3.setValue(int(pose[2]))
            
def current():
    pose = getPose()
    ui.currentBox.setValue(int(pose[0]))
    ui.currentBox2.setValue(int(pose[1]))
    ui.currentBox3.setValue(int(pose[2]))
def move():
    global t
    #t = 1
    moveJ(ui.setBox.value(),ui.setBox2.value(),ui.setBox3.value(),0)
    #t = 0
bc = True
c = 0
def connected():
    global t
    global pose
    global gs
    global bs
    global bc
    global c
    if c == 0:
        c = connect()
    if bc == True:
        t = 0
        thread = AThread()
        thread.start()
        if c == "Dobot Connected":
            ui.connectButton.setStyleSheet('QPushButton {background-color: red; color: white;}')
            ui.label_9.setText("Dobot подключен")
            ui.label_9.setStyleSheet('QLabel {color: green;}')
            ui.connectButton.setText("Отключить Dobot")
            #enabled
            ui.currentBox.setEnabled(True)
            ui.currentBox2.setEnabled(True)
            ui.currentBox3.setEnabled(True)
            ui.setBox.setEnabled(True)
            ui.setBox2.setEnabled(True)
            ui.setBox3.setEnabled(True)
            ui.pushButton.setEnabled(True)
            ui.pushButton_2.setEnabled(True)
            ui.railBox.setEnabled(True)
            ui.railMove.setEnabled(True)
            ui.convBox.setEnabled(True)
            ui.convMove.setEnabled(True)
            ui.homeButton.setEnabled(True)
            ui.socButton.setEnabled(True)
            ui.gripButton.setEnabled(True)
            #enabled
            if bs == True:
                ui.socButton.setStyleSheet('QPushButton {background-color: green; color: white;}')
            else:
                ui.socButton.setStyleSheet('QPushButton {background-color: red; color: white;}')
            if gs == True:
                ui.gripButton.setStyleSheet('QPushButton {background-color: green; color: white;}')
            else:
                ui.gripButton.setStyleSheet('QPushButton {background-color: red; color: white;}')
                
            ui.label_5.setStyleSheet('QLabel {color: red;}')
            ui.label_4.setStyleSheet('QLabel {color: green;}')
            ui.label_3.setStyleSheet('QLabel {color: blue;}')
            ui.label_6.setStyleSheet('QLabel {color: red;}')
            ui.label_7.setStyleSheet('QLabel {color: green;}')
            ui.label_8.setStyleSheet('QLabel {color: blue;}')
            ui.homeButton.setStyleSheet('QPushButton {background-color: #ff7100; color: white;}')
            ui.pushButton.setStyleSheet('QPushButton {background-color: #0086ff; color: white;}')
            ui.pushButton_2.setStyleSheet('QPushButton {background-color: #0086ff; color: white;}')
            ui.railMove.setStyleSheet('QPushButton {background-color: #7400ff; color: white;}')
            ui.convMove.setStyleSheet('QPushButton {background-color: #7400ff; color: white;}')
            ui.railBox.setValue(int(getRailMove()[0]))
            pose = getPose()
            ui.currentBox.setValue(int(pose[0]))
            ui.currentBox2.setValue(int(pose[1]))
            ui.currentBox3.setValue(int(pose[2]))
            bc = False
    else:
        t = 1
        ui.connectButton.setStyleSheet('QPushButton {background-color: green; color: white;}')
        ui.label_9.setText("Dobot не подключен")
        ui.label_9.setStyleSheet('QLabel {color: red;}')
        ui.connectButton.setText("Подключить Dobot")
        #disabled
        ui.currentBox.setEnabled(False)
        ui.currentBox2.setEnabled(False)
        ui.currentBox3.setEnabled(False)
        ui.setBox.setEnabled(False)
        ui.setBox2.setEnabled(False)
        ui.setBox3.setEnabled(False)
        ui.pushButton.setEnabled(False)
        ui.pushButton_2.setEnabled(False)
        ui.railBox.setEnabled(False)
        ui.railMove.setEnabled(False)
        ui.convBox.setEnabled(False)
        ui.convMove.setEnabled(False)
        ui.homeButton.setEnabled(False)
        ui.socButton.setEnabled(False)
        ui.gripButton.setEnabled(False)
        #disabled
        ui.socButton.setStyleSheet(Button_style)
        ui.gripButton.setStyleSheet(Button_style)
        ui.homeButton.setStyleSheet(Button_style)
        ui.pushButton.setStyleSheet(Button_style)
        ui.pushButton_2.setStyleSheet(Button_style)
        ui.railMove.setStyleSheet(Button_style)
        ui.convMove.setStyleSheet(Button_style)
        ui.label_3.setStyleSheet(label_style)
        ui.label_4.setStyleSheet(label_style)
        ui.label_5.setStyleSheet(label_style)
        ui.label_6.setStyleSheet(label_style)
        ui.label_7.setStyleSheet(label_style)
        ui.label_8.setStyleSheet(label_style)
        ui.railBox.setValue(0)
        pose = getPose()
        ui.currentBox.setValue(0)
        ui.currentBox2.setValue(0)
        ui.currentBox3.setValue(0)
        bc = True
    
def rail():
    railMove(ui.railBox.value())
def conv():
    convMove(ui.convBox.value())
def moveHome():
    home()
def suc():
    global bs
    suction(bs)
    if bs == True:
        ui.socButton.setStyleSheet('QPushButton {background-color: red; color: white;}')
        ui.socButton.setText("Выключить присоску")
        bs = False
    else:
        ui.socButton.setStyleSheet('QPushButton {background-color: green; color: white;}')
        ui.socButton.setText("Включить присоску")
        bs = True
def grip():
    global gs
    gripper(gs)
    if gs == True:
        ui.gripButton.setStyleSheet('QPushButton {background-color: red; color: white;}')
        ui.gripButton.setText("Выключить захват")
        gs = False
    else:
        ui.gripButton.setStyleSheet('QPushButton {background-color: green; color: white;}')
        ui.gripButton.setText("Включить захват")
        gs = True
        
#button.setStyleSheet('QPushButton {background-color: #A3C1DA; color: red;}')

ui.pushButton.clicked.connect(current)
ui.pushButton_2.clicked.connect(move)
ui.connectButton.clicked.connect(connected)
ui.railMove.clicked.connect(rail)
ui.convMove.clicked.connect(conv)
ui.homeButton.clicked.connect(moveHome)
ui.socButton.clicked.connect(suc)
ui.gripButton.clicked.connect(grip)



ui.show()

app.exec()
