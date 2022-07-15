from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QTableWidgetItem 
from matplotlib.pyplot import margins 
from BukuTelefonIndah import Ui_MainWindow
import sys
import sqlite3 as sql
import os 
os.system('python Connection_2.py')
os.system('python CreateTable_2.py')

global id, namadepan, namabelakang, kota, notelefon, email

# Users (id INT, Nama Depan TEXT, Nama Belakang TEXT, Kota TEXT, No Telefon TEXT, Email TEXT)

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()  
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)     

        self.btnDaftarClick()
        self.ui.btnDaftar.clicked.connect(self.btnDaftarClick)
        self.ui.btnSimpan.clicked.connect(self.btnSimpanClick)
        self.ui.btnHapus.clicked.connect(self.btnHapusClick)
        self.ui.btnPerbarui.clicked.connect(self.btnPerbaruiClick)
        self.ui.tblDaftar.clicked.connect(self.ListOnClick) 
 
    def btnClear(self):
        self.ui.txtID.clear()
        self.ui.txtNamaDepan.clear()
        self.ui.txtNamaBelakang.clear()
        self.ui.txtKota.clear()
        self.ui.txtNoTelefon.clear()
        self.ui.txtEmail.clear()

    def ListOnClick(self): 
        self.ui.txtID.setText(self.ui.tblDaftar.item(self.ui.tblDaftar.currentRow(), 0).text())
        self.ui.txtNamaDepan.setText(self.ui.tblDaftar.item(self.ui.tblDaftar.currentRow(), 1).text())
        self.ui.txtNamaBelakang.setText(self.ui.tblDaftar.item(self.ui.tblDaftar.currentRow(), 2).text())
        self.ui.txtKota.setText(self.ui.tblDaftar.item(self.ui.tblDaftar.currentRow(), 3).text())
        self.ui.txtNoTelefon.setText(self.ui.tblDaftar.item(self.ui.tblDaftar.currentRow(), 4).text())
        self.ui.txtEmail.setText(self.ui.tblDaftar.item(self.ui.tblDaftar.currentRow(), 5).text())
 
    def btnSimpanClick(self): 
        id = self.ui.txtID.text()
        namadepan = self.ui.txtNamaDepan.text()
        namabelakang = self.ui.txtNamaBelakang.text()
        kota = self.ui.txtKota.text()
        notelefon = self.ui.txtNoTelefon.text()
        email = self.ui.txtEmail.text()

        try:
            self.conn = sql.connect("BukuTelefonIndah.db")
            self.c = self.conn.cursor() 
            self.c.execute("INSERT INTO Users VALUES (?,?,?,?,?,?)",(id,namadepan,namabelakang,kota,notelefon,email))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            print('Successful','User is added successfully to the database.')
        except Exception:
            print('Error', 'Could not add student to the database.')
        
        self.btnClear()
        self.btnDaftarClick()

    def btnDaftarClick(self):  
        self.ui.tblDaftar.clear()
        self.ui.tblDaftar.setColumnCount(6)
        self.ui.tblDaftar.setHorizontalHeaderLabels(('ID','NamaDepan','NamaBelakang','Kota','NoTelefon','Email'))
        self.ui.tblDaftar.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        db = sql.connect('BukuTelefonIndah.db')
        cur = db.cursor()
        selectquery = "SELECT * FROM Users"
        cur.execute(selectquery) 
        rows = cur.fetchall()
         
        self.ui.tblDaftar.setRowCount(len(rows))
        
        for rowIndeks, rowData in enumerate(rows):
            for columnIndeks, columnData in enumerate (rowData):
                self.ui.tblDaftar.setItem(rowIndeks,columnIndeks,QTableWidgetItem(str(columnData))) 
    
    def btnPerbaruiClick(self):  
        id = self.ui.txtID.text()
        namadepan = self.ui.txtNamaDepan.text()
        namabelakang = self.ui.txtNamaBelakang.text()
        kota = self.ui.txtKota.text()
        notelefon = self.ui.txtNoTelefon.text()
        email = self.ui.txtEmail.text()

        try:
            self.conn = sql.connect("BukuTelefonIndah.db")
            self.c = self.conn.cursor()  
            self.c.execute("UPDATE Users SET namadepan = ?, namabelakang = ?, kota = ?, \
                notelefon = ?, email = ? WHERE id = ?",(namadepan,namabelakang,kota,notelefon,email,id))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            print('Successful','User is updated successfully to the database.')
        except Exception:
            print('Error', 'Could not update student to the database.')

        self.btnClear()
        self.btnDaftarClick()

    def btnHapusClick(self): 
        id = self.ui.txtID.text() 

        try:
            self.conn = sql.connect("BukuTelefonIndah.db")
            self.c = self.conn.cursor() 
            self.c.execute('DELETE FROM Users WHERE id = ?  ', (id,))
            self.conn.commit()
            self.c.close()
            self.conn.close()
            print('Successful','User is deleted successfully from the database.')
        except Exception:
            print('Error', 'Could not delete student to the database.')
        
        self.btnClear()
        self.btnDaftarClick()

            
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()