from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import QByteArray, QEvent 
from window import Ui_MainWindow
from images import *
from sys import exit

from PIL import Image, ImageDraw, ImageQt, ImageFont
from math import cos, sin, atan2, pi, floor

el = ['1s', '2s', '2p', '3s', '3p', '4s', '4p', '4d', '4f', 
      '5s', '5p', '5d', '5f', '6s', '6p', '6d', '7s', '7p']

max_el = {
    "s" : 2,
    "p" : 6,
    "d" : 10,
    "f" : 14,
}

pow = {
    "0" : "⁰",    "1" : "¹",
    "2" : "²",    "3" : "³",
    "4" : "⁴",    "5" : "⁵",
    "6" : "⁶",    "7" : "⁷",
    "8" : "⁸",    "9" : "⁹",
}
available_characters = "spdf0123456789⁰¹²³⁴⁵⁶⁷⁸⁹ "
keys = "1234567890qwertyuiopasdfghjklzxcvbnm"
entry = []

def check_sublevel(num_level, sublevel):
    for level in el:
        if num_level == level[0] and sublevel == level[1]:
            return True
    return False

def pow_to_num(power : str):
    if power.isnumeric():
        string = ""
        num = dict((v,k) for k,v in pow.items())
        for i in range(len(power)):
            string += num[power[i]]
        return string
    return None

def num_to_pow(num : str):
    if num.isnumeric():
        string = ""
        for i in num:
            string += pow[i]
        return string
    return None

def is_pow(s : str):
    for i in pow.values():
        if s == i:
            return True
    return False

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.image = Image.new("RGBA", (1, 1))
        self.cell_size = 30
        self.thickness = 2
        self.x = 0
        self.x1 = 0

        self.entry_size_old = 0

        pm = QPixmap()
        pm.loadFromData(QByteArray(icon_img))
        self.setWindowIcon(QIcon(pm))
        pm.loadFromData(QByteArray(save_img))
        self.ui.save_btn.setIcon(QIcon(pm))
        pm.loadFromData(QByteArray(copy_img))
        self.ui.copy_btn.setIcon(QIcon(pm))
        self.ui.dock_widget.setWindowTitle("Налаштування")
        self.show()

        self.ui.entry_line.installEventFilter(self)
        self.ui.entry_line.textEdited.connect(self.filter_callback)
        self.ui.entry_line.returnPressed.connect(self.ok_click)

        self.ui.ok_btn.clicked.connect(self.ok_click)
        self.ui.save_btn.clicked.connect(self.save_table)
        self.ui.copy_btn.clicked.connect(self.copy_table)

        self.ui.size_spinbox.valueChanged.connect(self.size_changed)
        self.ui.thickness_spinbox.valueChanged.connect(self.thickness_changed)

    def eventFilter(self, source, event):
        if event.type() == QEvent.KeyPress and source is self.ui.entry_line:
            if event.text() == ' ':
                self.check_levels()
                self.filter_callback(self.ui.entry_line.text())
        return super(MainWindow, self).eventFilter(source, event)

    def size_changed(self):
        self.cell_size = self.ui.size_spinbox.value()
        self.ok_click()

    def thickness_changed(self):
        self.thickness = self.ui.thickness_spinbox.value()
        self.ok_click()

    def filter_callback(self, text):
        if self.entry_size_old > len(text):
            self.entry_size_old = len(text)
            return True
        
        self.entry_size_old = len(text)
        try:
            s = ""
            for i in text:
                if i in available_characters:
                    s += i

            if not s:
                self.ui.entry_line.setText("")
                return True
            
            global entry
            entry.clear()
            entry = s.split(' ')

            for i in range(len(entry)):
                entry[i] = self.check_max(entry[i])

            s = ' '.join(entry)
            self.ui.entry_line.setText(s)

            return True
        except:
            pass

    def check_max(self, level : str):
        try:
            level_len = len(level)
            if level_len < 3:
                return level
            sl = level[1]       # sublevel
            
            n = level[2]
            if is_pow(n):
                n = pow_to_num(n)    

            if sl == 's' and int(n) > 2:
                n = '2'
            elif sl == 'p' and int(n) > 6:
                n = '6'
            elif (sl == 'd' or sl == 'f') and level_len == 4 and int(n) > 0:
                n = '1'
            
            p1 = pow[n]
            p2 = ""

            if level_len == 4 and (sl == 'd' or sl == 'f'):
                n = level[3]
                if is_pow(n):
                    n = pow_to_num(n)

                if sl == 'd' and int(n) > 0:
                    n = '0'
                elif sl == 'f' and int(n) > 4: 
                    n = '4'
                p2 = pow[n]
            
            return level[0] + sl + p1 + p2
        except:
            pass
        
    def check_levels(self):
        global entry
        try:
            entry = [i for i in entry if i]
            for i, level in enumerate(el):
                if entry[i][:2] != level and entry[i][0].isnumeric() and not entry[i][1].isnumeric() and check_sublevel(entry[i][0], entry[i][1]):
                    entry.insert(i, level + num_to_pow(str(max_el[level[1]])))
                elif entry[i][:2] == level and len(entry) > (i+1):
                    continue
                else:
                    break
        except:
            return False
        self.filter_callback(' '.join(entry))
        return True
    
    def ok_click(self):
        if self.check_levels():
            self.draw_table()

    def save_table(self):
        try:
            self.draw_table()
            options = QFileDialog.Options()
            fileName = ''.join(entry)
            fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()",fileName,".png", options=options)
            if fileName:
                self.image.save(fileName + ".png")
        except:
            pass
    
    def copy_table(self):
        self.draw_table()
        qt_image1 = ImageQt.ImageQt(self.image)
        qt_image2 = QPixmap.fromImage(qt_image1)
        QApplication.clipboard().setPixmap(qt_image2)

    def draw_table(self):
        self.image = Image.new("RGBA", self.get_geometry())
        self.draw()
        qt_image1 = ImageQt.ImageQt(self.image)
        qt_image2 = QPixmap.fromImage(qt_image1)
        self.ui.table.setPixmap(qt_image2)

    def get_geometry(self):
        try:
            width, height = self.thickness*2, self.cell_size*2

            lvl = "1"
            for level in entry:
                if lvl == level[0]:
                    height += self.cell_size
                else:
                    height += self.cell_size / 2
                lvl = level[0]

                width += self.cell_size * (max_el[level[1]] / 2)
            return (int(width), int(height))
        except:
            return (1, 1)
            

    def draw(self):
        self.x, y = self.thickness, self.image.height
        self.x1, y1 = self.cell_size + self.thickness, y - self.cell_size
        im = ImageDraw.Draw(self.image)
        im.rectangle((0, 0, self.image.width, self.image.height), fill=(0, 0, 0, 0))

        lvl = "1"
        slvl = 's'

        try:
            for level in entry:
                self.draw_cell(im, y, y1, int(pow_to_num(level[2:])), int(max_el[level[1]] / 2), level)
                if lvl == level[0]:
                    y -= self.cell_size
                    y1 -= self.cell_size
                else:
                    y -= self.cell_size / 2
                    y1 -= self.cell_size / 2

                lvl = level[0]
                slvl = level[1]
        except:
            pass
        
    def draw_cell(self, im : ImageDraw.Draw, y, y1, arrows = 10, blocks = 7, text = 'none'):
        for i in range(blocks):
            im.rectangle([self.x -  floor(self.thickness /2), y, self.x1, y1], outline="black", width=self.thickness)
            if arrows - blocks - i > 0:
                self.arrowedLine(im, (self.x+self.cell_size/3, y-self.cell_size/6), (self.x+self.cell_size/3, y1+self.cell_size/6))
                self.arrowedLine(im, (self.x+self.cell_size/1.5, y1+self.cell_size/6), (self.x+self.cell_size/1.5, y-self.cell_size/6))
            elif arrows - i % blocks > 0:
                self.arrowedLine(im, (self.x+self.cell_size/2, y-self.cell_size/6), (self.x+self.cell_size/2, y1+self.cell_size/6))
            else:
                pass
            self.x+=self.cell_size
            self.x1+=self.cell_size
        
        font = ImageFont.truetype("calibri.ttf", int(self.cell_size/1.5), encoding="unic")
        im.text((self.x - self.thickness / 2 - blocks/2 * self.cell_size - self.cell_size / 2, y1-self.cell_size/1.5), text, font=font, fill="black")


    def arrowedLine(self, draw, ptA, ptB, color=(0,0,0)):
        if self.thickness > 2:
            draw.line((ptA, ptB), width=2, fill=color)
        else:
            draw.line((ptA, ptB), width=self.thickness, fill=color)
        x0, y0 = ptA
        x1, y1 = ptB
        xb = 0.60*(x1-x0)+x0
        yb = 0.60*(y1-y0)+y0
        if x0==x1:
            vtx0 = (xb-5, yb)
            vtx1 = (xb+5, yb)
        elif y0==y1:
            vtx0 = (xb, yb+5)
            vtx1 = (xb, yb-5)
        else:
            alpha = atan2(y1-y0,x1-x0)-90*pi/180
            a = 8*cos(alpha)
            b = 8*sin(alpha)
            vtx0 = (xb+a, yb+b)
            vtx1 = (xb-a, yb-b)
        draw.polygon([vtx0, vtx1, ptB], fill=color)

app = QApplication([])
window = MainWindow()
exit(app.exec())