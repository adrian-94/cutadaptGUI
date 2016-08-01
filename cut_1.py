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
        self.prompt_1=0
        self.file_1=""
        self.file_2=""
        self.command=""
        self.command_1=""
        self.type=""
        self.adapter=""
        self.input_file=""
        self.output_file=""
        self.min_length="0"
        self.max_length="150"
        
        self.too_short=" --too-short-output too_short_Output"
        self.too_long=" --too-long-output too_long_Output"
        self.untrimmed_output=""
        self.discard_t=""
        self.discard_unt=""
        self.max_error="0.1"
        self.bases="0"
        
        self.frame.hide()
        self.frame_2.hide()
        self.checkBox_2.stateChanged.connect(self.checkBox_2_stateChanged)
        self.checkBox_5.stateChanged.connect(self.checkBox_5_stateChanged)
        self.checkBox_4.stateChanged.connect(self.checkBox_4_stateChanged)
        self.checkBox_6.stateChanged.connect(self.checkBox_6_stateChanged)
        self.checkBox_7.stateChanged.connect(self.checkBox_7_stateChanged)
        self.checkBox_8.stateChanged.connect(self.checkBox_8_stateChanged)
        
        self.checkBox_10.stateChanged.connect(self.checkBox_10_stateChanged)
        self.pushButton_6.clicked.connect(self.browseAdapter)
        self.pushButton_2.clicked.connect(self.browseInput)
        self.pushButton_4.clicked.connect(self.deMulti)
        self.checkBox_3.stateChanged.connect(self.adapterType)
        self.pushButton.clicked.connect(self.adapterFile)
        self.pushButton_3.clicked.connect(self.inputFile)
        self.pushButton_5.clicked.connect(self.trimming)
        self.radioButton.clicked.connect(self.adpt_3)
        self.radioButton_2.clicked.connect(self.adpt_5)
        self.radioButton_5.clicked.connect(self.adpt_anch5)
        self.radioButton_3.clicked.connect(self.adpt_anch3)  
        self.radioButton_6.clicked.connect(self.linked)
       
        
        
    def linked(self):
        self.type="a"
        
    def adpt_anch3(self):
        self.type="a"
    
    def adpt_anch5(self):
        self.type="g"

    def adpt_5(self):
        self.type="g"
        
    def adpt_3(self):
        self.type="a"
        
    
        
    def adapterType(self):
        
       self.prompt_1=self.checkBox_3.checkState()
       if self.prompt_1==2:
           self.pushButton.hide()
       if self.prompt_1!=2:
           self.pushButton.show()
           
    def adapterFile(self):
        
        caption="Open File"
        directory='./'
        #filter_mask="fastq files (*.fastq)"
        
        self.adapter=(QFileDialog.getOpenFileNames(None, caption, directory))[0]
        self.lineEdit_6.setText(str(os.path.basename(self.adapter))) 
        
    def inputFile(self):
        
        caption="Open File"
        directory='./'
        filter_mask="fastq files (*.fastq)"
        
        self.input_file=(QFileDialog.getOpenFileNames(None, caption, directory, filter_mask))[0]
        self.lineEdit_7.setText(str(os.path.basename(self.input_file)))
        
    def browseInput(self):
        
        caption="Open File"
        directory='./'
        filter_mask="fastq files (*.fastq)"
        
        self.file_1=(QFileDialog.getOpenFileNames(None, caption, directory, filter_mask))[0]
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
        
    def checkBox_6_stateChanged(self):#too short output
       self.prompt=self.checkBox_6.checkState()
       if self.prompt==2:
           self.too_short+="_"+str(os.path.basename(self.input_file))+" "
      
           
    
       
       
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
       
    def checkBox_8_stateChanged(self):#too long output
        
       self.prompt=self.checkBox_8.checkState()
       if self.prompt==2:
           self.too_long+="_"+str(os.path.basename(self.input_file))+" "
   
           
   
       


           
  
       
    def checkBox_10_stateChanged(self):#remove fixed number of bases
     
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
      
        self.frame.show()
    
    def trimShown(self):
       
        self.frame_2.show()
        self.lineEdit_10.hide()
        self.checkBox_6.hide()
        
        self.lineEdit_12.hide()
        self.checkBox_8.hide()
        
     
        self.lineEdit_2.hide()
       
    def trimHide(self):
        
        self.frame_2.hide()
     
    def trimming(self):
        if self.radioButton_4.isChecked():
           self.untrimmed_output=" --untrimmed-output untrimmed_Output_"+str(os.path.basename(self.input_file))+" "
        if self.radioButton_7.isChecked():
           self.discard_t=" --discard-trimmed "
        if self.radioButton_8.isChecked():
           self.discard_unt=" --discard-untrimmed "
        if self.prompt_1!=2:
            self.file_2=str(self.lineEdit_6.text())
        if (self.radioButton_2.isChecked()|self.radioButton_5.isChecked()): 
           self.command_1="~/.local/bin/cutadapt -g "+str(self.file_2)+" -m "+str(self.lineEdit_10.text())+str(self.too_short)+" -M "+str(self.lineEdit_12.text())+str(self.too_long)+str(self.untrimmed_output)+str(self.discard_t)+str(self.discard_unt)+" -e "+str(self.lineEdit.text())+" -u "+str(self.lineEdit_2.text())+" -o trimmed_"+str(os.path.basename(self.input_file))+" "+self.input_file 
        if (self.radioButton.isChecked()|self.radioButton_3.isChecked()|self.radioButton_6.isChecked()):
           self.command_1="~/.local/bin/cutadapt -a "+str(self.file_2)+" -m "+str(self.lineEdit_10.text())+str(self.too_short)+" -M "+str(self.lineEdit_12.text())+str(self.too_long)+str(self.untrimmed_output)+str(self.discard_t)+str(self.discard_unt)+" -e "+str(self.lineEdit.text())+" -u "+str(self.lineEdit_2.text())+" -o trimmed_"+str(os.path.basename(self.input_file))+" "+self.input_file
        print self.command_1
        subprocess.call(self.command_1,shell=True)
        
form = Cutadapt()
form.show()
app.exec_()
app.deleteLater()
sys.exit()        