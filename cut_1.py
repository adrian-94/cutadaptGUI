# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 16:04:29 2016

@author: DEEPN
"""
import sip
sip.setapi('QString', 2)
import subprocess
import sys
import os
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import QFileDialog


app = QtGui.QApplication(sys.argv)
form_class, base_class = uic.loadUiType(os.path.join('ui', 'cut_1.ui'))

class vQlistWidgetItem(QtGui.QListWidgetItem):
    def __init__(self, value, data):
        super(vQlistWidgetItem, self).__init__(QtCore.QString('%s' % value))
        
        
        
        

class Cutadapt(QtGui.QMainWindow, form_class):
    def __init__(self, *args):
        super(Cutadapt, self).__init__(*args)
        self.setupUi(self)
        self.prompt=0
        self.file_1=""
        self.file_2=""
        self.command=""
        self.frame.hide()
        self.frame_2.hide()
        """
        self.label_4.hide()
        self.lineEdit_3.hide()
        self.label_6.hide()
        self.pushButton_2.hide()
        self.lineEdit_5.hide()
        #self.label_5.hide()
        #self.lineEdit_4.hide() 
        self.pushButton_6.hide()
        self.pushButton_4.hide()
        self.label_10.hide()#demulthide
        self.label_7.hide()
        self.groupBox.hide()
        self.label_8.hide()
        self.checkBox_3.hide()
        self.pushButton.hide()
        self.lineEdit_6.hide()
        self.label_9.hide()
        self.pushButton_3.hide()
        self.lineEdit_3.hide()
        self.label_11.hide()
        self.lineEdit_9.hide()
        self.lineEdit_7.hide()
        self.label_14.hide()
        self.checkBox_4.hide()
        self.lineEdit_10.hide()
        self.checkBox_6.hide()
        self.lineEdit_11.hide()
        self.checkBox_7.hide()
        self.checkBox_8.hide()
        self.lineEdit_13.hide()
        self.lineEdit_12.hide()
        self.checkBox_9.hide()
        self.lineEdit_14.hide()
        self.checkBox_10.hide()
        self.checkBox_11.hide()
        self.label_2.hide()
        self.lineEdit.hide()
        self.checkBox.hide()
        self.label_3.hide()
        #self.buttonBox.hide()
        #self.pushButton_7.hide()
        #self.pushButton_8.hide()
        self.lineEdit_2.hide()
        self.pushButton_5.hide()#trimHide
        """
        self.checkBox_2.stateChanged.connect(self.checkBox_2_stateChanged)
        self.checkBox_5.stateChanged.connect(self.checkBox_5_stateChanged)
        self.checkBox_4.stateChanged.connect(self.checkBox_4_stateChanged)
        self.checkBox_6.stateChanged.connect(self.checkBox_6_stateChanged)
        self.checkBox_7.stateChanged.connect(self.checkBox_7_stateChanged)
        self.checkBox_8.stateChanged.connect(self.checkBox_8_stateChanged)
        self.checkBox_9.stateChanged.connect(self.checkBox_9_stateChanged)
        self.checkBox_10.stateChanged.connect(self.checkBox_10_stateChanged)
        self.pushButton_6.clicked.connect(self.browseAdapter)
        self.pushButton_2.clicked.connect(self.browseInput)
        self.pushButton_4.clicked.connect(self.deMulti)
    
    def browseInput(self):
        
        caption="Open File"
        directory='./'
        #filter_mask="fastq files (*.fastq)"
        
        self.file_1=(QFileDialog.getOpenFileNames(None, caption, directory))[0]
        self.lineEdit_5.setText(str(os.path.basename(self.file_1)))
        
        
    def browseAdapter(self):
        
        caption="Open File"
        directory='./'
        #filter_mask="fastq files (*.fastq)"
        
        self.file_2=(QFileDialog.getOpenFileNames(None, caption, directory))[0]
        self.lineEdit_3.setText(str(os.path.basename(self.file_2)))
        
    def deMulti(self):
        
        self.command="~/.local/bin/cutadapt -a file:"+self.file_2+" --no-trim --untrimmed-o noadapter_"+os.path.basename(self.file_1)+".gz -o {name}_"+os.path.basename(self.file_1)+".gz "+self.file_1
        print self.command        
        subprocess.call("~/.local/bin/cutadapt -a file:"+self.file_2+" --no-trim --untrimmed-o noadapter_"+os.path.basename(self.file_1)+".gz -o {name}_"+os.path.basename(self.file_1)+".gz "+self.file_1, shell=True)
        
    def demultiHide(self):
        """
        self.label_4.hide()
        self.lineEdit_3.hide()
        self.label_6.hide()
        self.pushButton_2.hide()
        self.lineEdit_5.hide()
        #self.label_5.hide()
        #self.lineEdit_4.hide() 
        self.label_10.hide()
        self.pushButton_6.hide()
        self.pushButton_4.hide()
        """
        self.frame.hide()
        
    def checkBox_2_stateChanged(self):
       self.prompt=self.checkBox_2.checkState()
       if self.prompt==2:
           self.demultiShown()
       if self.prompt!=2:
           self.demultiHide()
    def checkBox_5_stateChanged(self):
       self.prompt=self.checkBox_5.checkState()
       if self.prompt==2:
           self.trimShown()
       if self.prompt!=2:
           self.trimHide()
           
    def checkBox_4_stateChanged(self):
        
       self.prompt=self.checkBox_4.checkState()
       if self.prompt==2:
           self.Shown_1()
       if self.prompt!=2:
           self.Hide_1()
    
    def Shown_1(self):
       
       self.lineEdit_10.show()
       self.checkBox_6.show()
       
    def Hide_1(self):
        
       self.lineEdit_10.hide()
       self.checkBox_6.hide()
        
    def checkBox_6_stateChanged(self):
       self.prompt=self.checkBox_6.checkState()
       if self.prompt==2:
           self.Shown_2()
       if self.prompt!=2:
           self.Hide_2()
           
    def Shown_2(self):
       
       self.lineEdit_11.show()
       
       
    def Hide_2(self):
        
       self.lineEdit_11.hide()
       
       
    def checkBox_7_stateChanged(self):
       self.prompt=self.checkBox_7.checkState()
       if self.prompt==2:
           self.Shown_3()
       if self.prompt!=2:
           self.Hide_3()
           
    def Shown_3(self):
       
       self.lineEdit_12.show()
       self.checkBox_8.show()
       
    def Hide_3(self):
        
       self.lineEdit_12.hide()
       self.checkBox_8.hide()
       
    def checkBox_8_stateChanged(self):
        
       self.prompt=self.checkBox_8.checkState()
       if self.prompt==2:
           self.Shown_4()
       if self.prompt!=2:
           self.Hide_4()
           
    def Shown_4(self):
       
       self.lineEdit_13.show()
   
       
    def Hide_4(self):
        
       self.lineEdit_13.hide()
       
       
    def checkBox_9_stateChanged(self):
    
       self.prompt=self.checkBox_9.checkState()
       if self.prompt==2:
           self.Shown_9()
       if self.prompt!=2:
           self.Hide_9()
           
    def Shown_9(self):
       
       self.lineEdit_14.show()
       
    def Hide_9(self):
        
       self.lineEdit_14.hide()
       
    def checkBox_10_stateChanged(self):
     
       self.prompt=self.checkBox_10.checkState()
       if self.prompt==2:
           self.Shown_10()
       if self.prompt!=2:
           self.Hide_10()
           
    def Shown_10(self):
       
       self.lineEdit_2.show()
       
    def Hide_10(self):
        
       self.lineEdit_2.hide()
        
    def demultiShown(self):
        """
       self.label_4.show()
       self.lineEdit_3.show()
       self.label_6.show()
       self.pushButton_2.show()
       self.lineEdit_5.show()
       #self.label_5.show()
       #self.lineEdit_4.show()
       self.label_10.show()
       self.pushButton_6.show()
       self.pushButton_4.show()
       """
        self.frame.show()
    
    def trimShown(self):
        """
        self.label_7.show()
        self.groupBox.show()
        self.label_8.show()
        self.checkBox_3.show()
        self.pushButton.show()
        self.lineEdit_6.show()
        self.label_9.show()
        self.pushButton_3.show()
        self.label_11.show()
        self.lineEdit_9.show()
        self.lineEdit_7.show()
        self.label_14.show()
        self.checkBox_4.show()
        self.checkBox_7.show()
        self.checkBox_9.show()
        self.checkBox_10.show()
        self.checkBox_11.show()
        self.label_2.show()
        self.lineEdit.show()
        self.checkBox.show()
        self.pushButton_5.show()
        self.label_3.show()
        self.buttonBox.show()#trimHide
        """
        self.frame_2.show()
        self.lineEdit_10.hide()
        self.checkBox_6.hide()
        self.lineEdit_11.hide()
        self.lineEdit_12.hide()
        self.checkBox_8.hide()
        self.lineEdit_13.hide()
        self.lineEdit_14.hide()
        self.lineEdit_2.hide()
       
    def trimHide(self):
        """
        self.label_7.hide()
        self.groupBox.hide()
        self.label_8.hide()
        self.checkBox_3.hide()
        self.pushButton.hide()
        self.lineEdit_6.hide()
        self.label_9.hide()
        self.pushButton_3.hide()
        self.label_11.hide()
        self.lineEdit_9.hide()
        self.lineEdit_7.hide()
        self.label_14.hide()
        self.checkBox_4.hide()
        self.checkBox_7.hide()
        self.checkBox_9.hide()
        self.checkBox_10.hide()
        self.checkBox_11.hide()
        self.label_2.hide()
        self.lineEdit.hide()
        self.checkBox.hide()
        self.lineEdit_2.hide()
        self.pushButton_5.hide()
        self.label_3.hide()
        self.buttonBox.hide()#trimHide
        """
        self.frame_2.hide()

form = Cutadapt()
form.show()
app.exec_()
app.deleteLater()
sys.exit()        