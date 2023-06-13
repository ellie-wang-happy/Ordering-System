"""
Project Name：Ordering System
Author：Lin Wang
Date：2023/1/28
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import datetime
from time import strftime

from mainUI import *
from burgers import *
from drinks import *
from sweets import *


# Main UI
class Main(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_MainWindow()

        self.main_ui.setupUi(self)

        # Button
        btn_del = self.main_ui.pushButton_5
        btn_del.clicked.connect(self.order_del)
        btn_num = self.main_ui.pushButton_6
        btn_num.clicked.connect(self.order_num)
        self.btn_tip = self.main_ui.pushButton_7
        self.btn_tip.clicked.connect(self.order_tip)
        # button disable
        self.btn_tip.setEnabled(False)
        # define the list
        self.num = []
        self.new_num = []

    # Homepage UI
    def person(self):
        #  Homepage Image
        self.main_ui.label_8.setPixmap(QPixmap('./Images/homepage.png'))
        self.main_ui.label_8.setScaledContents(True)

        # initial the balance
        self.balance = 0

        # display the balance
        self.main_ui.label_2.setText(str(self.balance))

        # display home page
        main.show()

    # delete the specific index order from tableWidget
    def order_del(self):
        # get index
        row_index = main.main_ui.tableWidget.currentRow()
        if row_index != -1:
            # remove
            main.main_ui.tableWidget.removeRow(row_index)

    # calc balance
    def order_num(self):
        # enable calc button
        self.btn_tip.setEnabled(True)
        # list all items
        for row_index in range(main.main_ui.tableWidget.rowCount()):
            # add column 3 value
            self.num.append(
                main.main_ui.tableWidget.item(row_index, 2).text())

        # convert to int
        self.new_num = eval('[' + (','.join(self.num)) + ']')
        # sum value
        self.money = sum(self.new_num)
        self.money = round(self.money*1.13, 2)
        self.main_ui.label_2.setText(str(self.money))
        QMessageBox.information(
            self, "Notice", "Settlement completed,added 13% GST!", QMessageBox.Yes)

    # print receipt
    def order_tip(self):
        # open receipt txt file
        time1 = datetime.datetime.now().strftime("%Y.%m.%d-%H:%M:%S")
        time2 = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        with open("order/tip"+str(time2)+".txt", "w") as f:
            f.write(time1+"\n")
            # list
            for row_index in range(main.main_ui.tableWidget.rowCount()):
                # list
                for column_index in range(main.main_ui.tableWidget.columnCount()):
                    # write tableWidget data to *.txt file
                    f.write(main.main_ui.tableWidget.item(
                        row_index, column_index).text() + "\n")
            f.write("Balance：" + str(self.money) + "$")
        f.close()
        QMessageBox.information(
            self, "Congrats", " Transaction completed！", QMessageBox.Yes)


# Burges
class Burgers(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.burgers_ui = Ui_Burgers()
        self.burgers_ui.setupUi(self)

        # int order number
        self.bt1 = 0
        self.bt2 = 0
        self.bt3 = 0
        self.bt4 = 0
        self.bt5 = 0
        self.bt7 = 0
        # return order count
        self.bt6 = 0

        btn_bacon = self.burgers_ui.pushButton
        btn_bacon.clicked.connect(self.order_baconburger)
        btn_beef = self.burgers_ui.pushButton_2
        btn_beef.clicked.connect(self.order_beefburger)
        btn_fish = self.burgers_ui.pushButton_3
        btn_fish.clicked.connect(self.order_fishburger)
        btn_grilled = self.burgers_ui.pushButton_4
        btn_grilled.clicked.connect(self.order_grilledburger)
        btn_jack = self.burgers_ui.pushButton_5
        btn_jack.clicked.connect(self.order_jackburger)
        btn_vegetable = self.burgers_ui.pushButton_7
        btn_vegetable.clicked.connect(self.order_vegburger)
        btn_return = self.burgers_ui.pushButton_6
        btn_return.clicked.connect(self.nor_show)

    # burger page
    def nor_order(self):
        self.burgers_ui.label_3.setPixmap(
            QPixmap('./images/Burgers/Bacon Burger.jpg'))
        self.burgers_ui.label_3.setScaledContents(True)
        self.burgers_ui.label_6.setPixmap(
            QPixmap('./images/Burgers/Beef Burger.jpg'))
        self.burgers_ui.label_6.setScaledContents(True)
        self.burgers_ui.label_9.setPixmap(
            QPixmap('./images/Burgers/Fish Burger.jpg'))
        self.burgers_ui.label_9.setScaledContents(True)
        self.burgers_ui.label_12.setPixmap(
            QPixmap('./images/Burgers/Flame-Grilled Burger.jpg'))
        self.burgers_ui.label_12.setScaledContents(True)
        self.burgers_ui.label_15.setPixmap(
            QPixmap('./images/Burgers/Hungry-Jack Burger.jpg'))
        self.burgers_ui.label_15.setScaledContents(True)
        self.burgers_ui.label_18.setPixmap(
            QPixmap('./images/Burgers/Vegetable Burger.jpg'))
        self.burgers_ui.label_18.setScaledContents(True)
        # price
        self.price_bacon_burger = 7.99
        self.price_beef_burger = 9.99
        self.price_fish_burger = 7.99
        self.price_grilled_burger = 8.99
        self.price_hungry_jack_burger = 10.99
        self.price_vegetable_burger = 11.99
        # show price
        self.burgers_ui.label.setText(str(self.price_bacon_burger) + "$")
        self.burgers_ui.label_4.setText(str(self.price_beef_burger) + "$")
        self.burgers_ui.label_7.setText(str(self.price_fish_burger) + "$")
        self.burgers_ui.label_10.setText(str(self.price_grilled_burger) + "$")
        self.burgers_ui.label_13.setText(
            str(self.price_hungry_jack_burger) + "$")
        self.burgers_ui.label_16.setText(
            str(self.price_vegetable_burger) + "$")
        burger.show()

    # calculate the count
    def order_baconburger(self):
        self.bt1 += 1
        QMessageBox.information(self, "Congrats", "Added " +
                                str(self.bt1) + 'pcs(s)！', QMessageBox.Yes)

    def order_beefburger(self):
        self.bt2 += 1
        QMessageBox.information(self, "Congrats", "Added " +
                                str(self.bt2) + 'pcs(s)！', QMessageBox.Yes)

    def order_fishburger(self):
        self.bt3 += 1
        QMessageBox.information(self, "Congrats", "Added " +
                                str(self.bt3) + 'pcs(s)！', QMessageBox.Yes)

    def order_grilledburger(self):
        self.bt4 += 1
        QMessageBox.information(self, "Congrats", "Added " +
                                str(self.bt4) + 'pcs(s)！', QMessageBox.Yes)

    def order_jackburger(self):
        self.bt5 += 1
        QMessageBox.information(self, "Congrats", "Added " +
                                str(self.bt5) + 'pcs(s)！', QMessageBox.Yes)

    def order_vegburger(self):
        self.bt7 += 1
        QMessageBox.information(self, "Congrats", "Added " +
                                str(self.bt7) + 'pcs(s)！', QMessageBox.Yes)

    # click return button and back to homepage
    def nor_show(self):
        self.bt6 += 1

        # Hide Homepage
        burger.hide()

        # get the prices
        self.num_bacon = self.price_bacon_burger * self.bt1
        self.num_beef = self.price_beef_burger * self.bt2
        self.num_fish = self.price_fish_burger * self.bt3
        self.num_grilled = self.price_grilled_burger * self.bt4
        self.num_jack = self.price_hungry_jack_burger * self.bt5
        self.num_veg = self.price_vegetable_burger * self.bt7
        # Not first time entry
        if self.bt6 > 1:
            for row_index in range(main.main_ui.tableWidget.rowCount()):
                # get tableWidget name and add to name list
                name.append(main.main_ui.tableWidget.item(
                    row_index, 0).text())
            if 'Bacon Burger' in name:

                main.main_ui.tableWidget.setItem(name.index('Bacon Burger'), 1,
                                                 QTableWidgetItem("×" + str(self.bt1)))
                main.main_ui.tableWidget.setItem(name.index('Bacon Burger'), 2,
                                                 QTableWidgetItem(str(self.num_bacon)))
            if 'Bacon Burger' not in name:

                if self.bt1 != 0:

                    row_count = main.main_ui.tableWidget.rowCount()
                    main.main_ui.tableWidget.insertRow(row_count)
                    main.main_ui.tableWidget.setItem(
                        row_count, 0, QTableWidgetItem(burger.burgers_ui.label_2.text()))
                    main.main_ui.tableWidget.setItem(
                        row_count, 1, QTableWidgetItem("×" + str(self.bt1)))
                    main.main_ui.tableWidget.setItem(
                        row_count, 2, QTableWidgetItem(str(self.num_bacon)))
            if 'Beef Burger' in name:
                main.main_ui.tableWidget.setItem(name.index(
                    'Beef Burger'), 1, QTableWidgetItem("×" + str(self.bt2)))
                main.main_ui.tableWidget.setItem(name.index(
                    'Beef Burger'), 2, QTableWidgetItem(str(self.num_beef)))
            if 'Beef Burger' not in name:
                if self.bt2 != 0:
                    row_count = main.main_ui.tableWidget.rowCount()
                    main.main_ui.tableWidget.insertRow(row_count)
                    main.main_ui.tableWidget.setItem(
                        row_count, 0, QTableWidgetItem(burger.burgers_ui.label_5.text()))
                    main.main_ui.tableWidget.setItem(
                        row_count, 1, QTableWidgetItem("×" + str(self.bt2)))
                    main.main_ui.tableWidget.setItem(
                        row_count, 2, QTableWidgetItem(str(self.num_beef)))
            if 'Fish Burger' in name:
                main.main_ui.tableWidget.setItem(name.index('Fish Burger'), 1,
                                                 QTableWidgetItem("×" + str(self.bt3)))
                main.main_ui.tableWidget.setItem(name.index('Fish Burger'), 2,
                                                 QTableWidgetItem(str(self.num_fish)))
            if 'Fish Burger' not in name:
                if self.bt3 != 0:
                    row_count = main.main_ui.tableWidget.rowCount()
                    main.main_ui.tableWidget.insertRow(row_count)
                    main.main_ui.tableWidget.setItem(
                        row_count, 0, QTableWidgetItem(burger.burgers_ui.label_8.text()))
                    main.main_ui.tableWidget.setItem(
                        row_count, 1, QTableWidgetItem("×" + str(self.bt3)))
                    main.main_ui.tableWidget.setItem(
                        row_count, 2, QTableWidgetItem(str(self.num_fish)))
            if 'Flame-Grilled Burger' in name:
                main.main_ui.tableWidget.setItem(name.index(
                    'Flame-Grilled Burger'), 1, QTableWidgetItem("×" + str(self.bt4)))
                main.main_ui.tableWidget.setItem(name.index(
                    'Flame-Grilled Burger'), 2, QTableWidgetItem(str(self.num_grilled)))
            if 'Flame-Grilled Burger' not in name:
                if self.bt4 != 0:
                    row_count = main.main_ui.tableWidget.rowCount()
                    main.main_ui.tableWidget.insertRow(row_count)
                    main.main_ui.tableWidget.setItem(row_count, 0,
                                                     QTableWidgetItem(burger.burgers_ui.label_11.text()))
                    main.main_ui.tableWidget.setItem(
                        row_count, 1, QTableWidgetItem("×" + str(self.bt4)))
                    main.main_ui.tableWidget.setItem(
                        row_count, 2, QTableWidgetItem(str(self.num_grilled)))
            if 'Hungry-Jack Burger' in name:
                main.main_ui.tableWidget.setItem(name.index('Hungry-Jack Burger'), 1,
                                                 QTableWidgetItem("×" + str(self.bt5)))
                main.main_ui.tableWidget.setItem(name.index('Hungry-Jack Burger'), 2,
                                                 QTableWidgetItem(str(self.num_jack)))
            if 'Hungry-Jack Burger' not in name:
                if self.bt5 != 0:
                    row_count = main.main_ui.tableWidget.rowCount()
                    main.main_ui.tableWidget.insertRow(row_count)
                    main.main_ui.tableWidget.setItem(row_count, 0,
                                                     QTableWidgetItem(burger.burgers_ui.label_14.text()))
                    main.main_ui.tableWidget.setItem(
                        row_count, 1, QTableWidgetItem("×" + str(self.bt5)))
                    main.main_ui.tableWidget.setItem(
                        row_count, 2, QTableWidgetItem(str(self.num_jack)))
            if 'Vegetable Burger' in name:
                main.main_ui.tableWidget.setItem(name.index('Hungry-Jack Burger'), 1,
                                                 QTableWidgetItem("×" + str(self.bt5)))
                main.main_ui.tableWidget.setItem(name.index('Hungry-Jack Burger'), 2,
                                                 QTableWidgetItem(str(self.num_veg)))
            if 'Vegetable Burger' not in name:
                if self.bt5 != 0:
                    row_count = main.main_ui.tableWidget.rowCount()
                    main.main_ui.tableWidget.insertRow(row_count)
                    main.main_ui.tableWidget.setItem(row_count, 0,
                                                     QTableWidgetItem(burger.burgers_ui.label_17.text()))
                    main.main_ui.tableWidget.setItem(
                        row_count, 1, QTableWidgetItem("×" + str(self.bt7)))
                    main.main_ui.tableWidget.setItem(
                        row_count, 2, QTableWidgetItem(str(self.num_veg)))
        # first time
        else:
            if self.bt1 != 0:
                row_count = main.main_ui.tableWidget.rowCount()
                main.main_ui.tableWidget.insertRow(row_count)
                main.main_ui.tableWidget.setItem(
                    row_count, 0, QTableWidgetItem(burger.burgers_ui.label_2.text()))
                main.main_ui.tableWidget.setItem(
                    row_count, 1, QTableWidgetItem("×" + str(self.bt1)))
                main.main_ui.tableWidget.setItem(
                    row_count, 2, QTableWidgetItem(str(self.num_bacon)))
            if self.bt2 != 0:
                row_count = main.main_ui.tableWidget.rowCount()
                main.main_ui.tableWidget.insertRow(row_count)
                main.main_ui.tableWidget.setItem(
                    row_count, 0, QTableWidgetItem(burger.burgers_ui.label_5.text()))
                main.main_ui.tableWidget.setItem(
                    row_count, 1, QTableWidgetItem("×" + str(self.bt2)))
                main.main_ui.tableWidget.setItem(
                    row_count, 2, QTableWidgetItem(str(self.num_beef)))
            if self.bt3 != 0:
                row_count = main.main_ui.tableWidget.rowCount()
                main.main_ui.tableWidget.insertRow(row_count)
                main.main_ui.tableWidget.setItem(
                    row_count, 0, QTableWidgetItem(burger.burgers_ui.label_8.text()))
                main.main_ui.tableWidget.setItem(
                    row_count, 1, QTableWidgetItem("×" + str(self.bt3)))
                main.main_ui.tableWidget.setItem(
                    row_count, 2, QTableWidgetItem(str(self.num_fish)))
            if self.bt4 != 0:
                row_count = main.main_ui.tableWidget.rowCount()
                main.main_ui.tableWidget.insertRow(row_count)
                main.main_ui.tableWidget.setItem(
                    row_count, 0, QTableWidgetItem(burger.burgers_ui.label_11.text()))
                main.main_ui.tableWidget.setItem(
                    row_count, 1, QTableWidgetItem("×" + str(self.bt4)))
                main.main_ui.tableWidget.setItem(
                    row_count, 2, QTableWidgetItem(str(self.num_grilled)))
            if self.bt5 != 0:
                row_count = main.main_ui.tableWidget.rowCount()
                main.main_ui.tableWidget.insertRow(row_count)
                main.main_ui.tableWidget.setItem(
                    row_count, 0, QTableWidgetItem(burger.burgers_ui.label_14.text()))
                main.main_ui.tableWidget.setItem(
                    row_count, 1, QTableWidgetItem("×" + str(self.bt6)))
                main.main_ui.tableWidget.setItem(
                    row_count, 2, QTableWidgetItem(str(self.num_jack)))
            if self.bt7 != 0:
                row_count = main.main_ui.tableWidget.rowCount()
                main.main_ui.tableWidget.insertRow(row_count)
                main.main_ui.tableWidget.setItem(
                    row_count, 0, QTableWidgetItem(burger.burgers_ui.label_17.text()))
                main.main_ui.tableWidget.setItem(
                    row_count, 1, QTableWidgetItem("×" + str(self.bt7)))
                main.main_ui.tableWidget.setItem(
                    row_count, 2, QTableWidgetItem(str(self.num_veg)))


# Drinks page
class Drinks(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.drinks_ui = Ui_Drinks()
        self.drinks_ui.setupUi(self)

        # int order count
        self.bt1 = 0
        self.bt2 = 0
        self.bt4 = 0
        self.bt5 = 0
        # return order count
        self.bt3 = 0

        btn_drink1 = self.drinks_ui.pushButton
        btn_drink1.clicked.connect(self.order_drink1)
        btn_drink2 = self.drinks_ui.pushButton_2
        btn_drink2.clicked.connect(self.order_drink2)
        btn_return = self.drinks_ui.pushButton_3
        btn_return.clicked.connect(self.pac_show)
        btn_drink3 = self.drinks_ui.pushButton_4
        btn_drink3.clicked.connect(self.order_drink3)
        btn_drink4 = self.drinks_ui.pushButton_5
        btn_drink4.clicked.connect(self.order_drink4)

    # display drinkd
    def pac_order(self):
        self.drinks_ui.label_5.setPixmap(
            QPixmap('./Images/Drink/Coca-Cola.jpg'))
        self.drinks_ui.label_5.setScaledContents(True)
        self.drinks_ui.label_6.setPixmap(
            QPixmap('./Images/Drink/Orange Juice.jpg'))
        self.drinks_ui.label_6.setScaledContents(True)
        self.drinks_ui.label_11.setPixmap(QPixmap('./Images/Drink/Soda.jpg'))
        self.drinks_ui.label_11.setScaledContents(True)
        self.drinks_ui.label_12.setPixmap(QPixmap('./Images/Drink/Sprite.jpg'))
        self.drinks_ui.label_12.setScaledContents(True)
        # price
        self.price_drink1 = 1.99
        self.price_drink2 = 1.99
        self.price_drink3 = 1.59
        self.price_drink4 = 1.59
        self.drinks_ui.label.setText(str(self.price_drink1) + "$")
        self.drinks_ui.label_2.setText(str(self.price_drink2) + "$")
        self.drinks_ui.label_7.setText(str(self.price_drink3) + "$")
        self.drinks_ui.label_8.setText(str(self.price_drink4) + "$")
        drink.show()

    def order_drink1(self):
        self.bt1 += 1
        QMessageBox.information(self, "Congrats", "Added " +
                                str(self.bt1) + 'pcs(s)!', QMessageBox.Yes)

    def order_drink2(self):
        self.bt2 += 1
        QMessageBox.information(self, "Congrats", "Added " +
                                str(self.bt2) + 'pcs(s)!', QMessageBox.Yes)

    def order_drink3(self):
        self.bt4 += 1
        QMessageBox.information(self, "Congrats", "Added " +
                                str(self.bt4) + 'pcs(s)!', QMessageBox.Yes)

    def order_drink4(self):
        self.bt5 += 1
        QMessageBox.information(self, "Congrats", "Added " +
                                str(self.bt5) + 'pcs(s)!', QMessageBox.Yes)

    def pac_show(self):
        self.bt3 += 1

        drink.hide()

        self.num_drink1 = self.price_drink1 * self.bt1
        self.num_drink2 = self.price_drink2 * self.bt2
        self.num_drink3 = self.price_drink3 * self.bt4
        self.num_drink4 = self.price_drink4 * self.bt5

        #  Back button
        if self.bt3 > 1:
            for row_index in range(main.main_ui.tableWidget.rowCount()):
                name.append(main.main_ui.tableWidget.item(
                    row_index, 0).text())
            if 'Coca-Cola' in name:
                main.main_ui.tableWidget.setItem(name.index('Coca-Cola'), 1,
                                                 QTableWidgetItem("×" + str(self.bt1)))
                main.main_ui.tableWidget.setItem(name.index('Coca-Cola'), 2,
                                                 QTableWidgetItem(str(self.num_drink1)))
            if 'Coca-Cola' not in name:
                if self.bt1 != 0:
                    row_count = main.main_ui.tableWidget.rowCount()
                    main.main_ui.tableWidget.insertRow(row_count)
                    main.main_ui.tableWidget.setItem(row_count, 0,
                                                     QTableWidgetItem(drink.drinks_ui.label_3.text()))
                    main.main_ui.tableWidget.setItem(
                        row_count, 1, QTableWidgetItem("×" + str(self.bt1)))
                    main.main_ui.tableWidget.setItem(
                        row_count, 2, QTableWidgetItem(str(self.num_drink1)))
            if 'Orange Juice' in name:
                main.main_ui.tableWidget.setItem(name.index('Orange Juice'), 1,
                                                 QTableWidgetItem("×" + str(self.bt2)))
                main.main_ui.tableWidget.setItem(name.index('Orange Juice'), 2,
                                                 QTableWidgetItem(str(self.num_drink2)))
            if 'Orange Juice' not in name:
                if self.bt2 != 0:
                    row_count = main.main_ui.tableWidget.rowCount()
                    main.main_ui.tableWidget.insertRow(row_count)
                    main.main_ui.tableWidget.setItem(row_count, 0,
                                                     QTableWidgetItem(drink.drinks_ui.label_4.text()))
                    main.main_ui.tableWidget.setItem(
                        row_count, 1, QTableWidgetItem("×" + str(self.bt2)))
                    main.main_ui.tableWidget.setItem(
                        row_count, 2, QTableWidgetItem(str(self.num_drink2)))
            if 'Soda' in name:
                main.main_ui.tableWidget.setItem(name.index('Soda'), 1,
                                                 QTableWidgetItem("×" + str(self.bt4)))
                main.main_ui.tableWidget.setItem(name.index('Soda'), 2,
                                                 QTableWidgetItem(str(self.num_drink3)))
            if 'Soda' not in name:
                if self.bt4 != 0:
                    row_count = main.main_ui.tableWidget.rowCount()
                    main.main_ui.tableWidget.insertRow(row_count)
                    main.main_ui.tableWidget.setItem(row_count, 0,
                                                     QTableWidgetItem(drink.drinks_ui.label_9.text()))
                    main.main_ui.tableWidget.setItem(
                        row_count, 1, QTableWidgetItem("×" + str(self.bt4)))
                    main.main_ui.tableWidget.setItem(
                        row_count, 2, QTableWidgetItem(str(self.num_drink3)))
            if 'Sprite' in name:
                main.main_ui.tableWidget.setItem(name.index('Sprite'), 1,
                                                 QTableWidgetItem("×" + str(self.bt4)))
                main.main_ui.tableWidget.setItem(name.index('Sprite'), 2,
                                                 QTableWidgetItem(str(self.num_drink3)))
            if 'Sprite' not in name:
                if self.bt5 != 0:
                    row_count = main.main_ui.tableWidget.rowCount()
                    main.main_ui.tableWidget.insertRow(row_count)
                    main.main_ui.tableWidget.setItem(row_count, 0,
                                                     QTableWidgetItem(drink.drinks_ui.label_10.text()))
                    main.main_ui.tableWidget.setItem(
                        row_count, 1, QTableWidgetItem("×" + str(self.bt5)))
                    main.main_ui.tableWidget.setItem(
                        row_count, 2, QTableWidgetItem(str(self.num_drink4)))
        # Cancel
        else:
            if self.bt1 != 0:
                row_count = main.main_ui.tableWidget.rowCount()
                main.main_ui.tableWidget.insertRow(row_count)
                main.main_ui.tableWidget.setItem(
                    row_count, 0, QTableWidgetItem(drink.drinks_ui.label_3.text()))
                main.main_ui.tableWidget.setItem(
                    row_count, 1, QTableWidgetItem("×" + str(self.bt1)))
                main.main_ui.tableWidget.setItem(
                    row_count, 2, QTableWidgetItem(str(self.num_drink1)))
            if self.bt2 != 0:
                row_count = main.main_ui.tableWidget.rowCount()
                main.main_ui.tableWidget.insertRow(row_count)
                main.main_ui.tableWidget.setItem(
                    row_count, 0, QTableWidgetItem(drink.drinks_ui.label_4.text()))
                main.main_ui.tableWidget.setItem(
                    row_count, 1, QTableWidgetItem("×" + str(self.bt2)))
                main.main_ui.tableWidget.setItem(
                    row_count, 2, QTableWidgetItem(str(self.num_drink2)))
            if self.bt4 != 0:
                row_count = main.main_ui.tableWidget.rowCount()
                main.main_ui.tableWidget.insertRow(row_count)
                main.main_ui.tableWidget.setItem(
                    row_count, 0, QTableWidgetItem(drink.drinks_ui.label_9.text()))
                main.main_ui.tableWidget.setItem(
                    row_count, 1, QTableWidgetItem("×" + str(self.bt4)))
                main.main_ui.tableWidget.setItem(
                    row_count, 2, QTableWidgetItem(str(self.num_drink3)))
            if self.bt5 != 0:
                row_count = main.main_ui.tableWidget.rowCount()
                main.main_ui.tableWidget.insertRow(row_count)
                main.main_ui.tableWidget.setItem(
                    row_count, 0, QTableWidgetItem(drink.drinks_ui.label_10.text()))
                main.main_ui.tableWidget.setItem(
                    row_count, 1, QTableWidgetItem("×" + str(self.bt5)))
                main.main_ui.tableWidget.setItem(
                    row_count, 2, QTableWidgetItem(str(self.num_drink4)))


# sweets page
class Sweets(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.sweets_ui = Ui_Sweets()
        self.sweets_ui.setupUi(self)

        # int order count
        self.bt1 = 0
        self.bt2 = 0
        self.bt4 = 0
        self.bt5 = 0
        # return order count
        self.bt3 = 0

        btn_sweet1 = self.sweets_ui.pushButton
        btn_sweet1.clicked.connect(self.order_sweet1)
        btn_sweet2 = self.sweets_ui.pushButton_2
        btn_sweet2.clicked.connect(self.order_sweet2)
        btn_return = self.sweets_ui.pushButton_3
        btn_return.clicked.connect(self.act_show)
        btn_sweet3 = self.sweets_ui.pushButton_4
        btn_sweet3.clicked.connect(self.order_sweet3)
        btn_sweet4 = self.sweets_ui.pushButton_5
        btn_sweet4.clicked.connect(self.order_sweet4)

    def act_order(self):
        self.sweets_ui.label_5.setPixmap(
            QPixmap('./Images/Sweets/AppleTurnover.jpg'))
        self.sweets_ui.label_5.setScaledContents(True)
        self.sweets_ui.label_6.setPixmap(
            QPixmap('./Images/Sweets/Macaron.jpg'))
        self.sweets_ui.label_6.setScaledContents(True)
        self.sweets_ui.label_11.setPixmap(
            QPixmap('./Images/Sweets/Muffin.jpg'))
        self.sweets_ui.label_11.setScaledContents(True)
        self.sweets_ui.label_12.setPixmap(
            QPixmap('./Images/Sweets/Sundae.jpg'))
        self.sweets_ui.label_12.setScaledContents(True)
        # price
        self.price_sweet1 = 1.5
        self.price_sweet2 = 1.2
        self.price_sweet3 = 3.5
        self.price_sweet4 = 1.0
        self.sweets_ui.label.setText(str(self.price_sweet1) + "$")
        sweet.show()
        self.sweets_ui.label_2.setText(str(self.price_sweet2) + "$")
        sweet.show()
        self.sweets_ui.label_7.setText(str(self.price_sweet3) + "$")
        sweet.show()
        self.sweets_ui.label_8.setText(str(self.price_sweet4) + "$")
        sweet.show()

    def order_sweet1(self):
        self.bt1 += 1
        QMessageBox.information(self, "Congrats", "Added " +
                                str(self.bt1) + 'pcs(s)！', QMessageBox.Yes)

    def order_sweet2(self):
        self.bt2 += 1
        QMessageBox.information(self, "Congrats", "Added " +
                                str(self.bt2) + 'pcs(s)!', QMessageBox.Yes)

    def order_sweet3(self):
        self.bt4 += 1
        QMessageBox.information(self, "Congrats", "Added " +
                                str(self.bt4) + 'pcs(s)！', QMessageBox.Yes)

    def order_sweet4(self):
        self.bt5 += 1
        QMessageBox.information(self, "Congrats", "Added " +
                                str(self.bt5) + 'pcs(s)！', QMessageBox.Yes)
    # sweets page

    def act_show(self):
        self.bt3 += 1
        sweet.hide()
        self.num_sweet1 = self.price_sweet1 * self.bt1
        self.num_sweet2 = self.price_sweet2 * self.bt2
        self.num_sweet3 = self.price_sweet3 * self.bt4
        self.num_sweet4 = self.price_sweet4 * self.bt5
        if self.bt3 > 1:
            for row_index in range(main.main_ui.tableWidget.rowCount()):
                name.append(main.main_ui.tableWidget.item(
                    row_index, 0).text())
            if 'AppleTurnovers' in name:
                main.main_ui.tableWidget.setItem(name.index(
                    'AppleTurnovers'), 1, QTableWidgetItem("×" + str(self.bt1)))
                main.main_ui.tableWidget.setItem(name.index(
                    'AppleTurnovers'), 2, QTableWidgetItem(str(self.num_sweet1)))
            if 'AppleTurnovers' not in name:
                if self.bt1 != 0:
                    row_count = main.main_ui.tableWidget.rowCount()
                    main.main_ui.tableWidget.insertRow(row_count)
                    main.main_ui.tableWidget.setItem(row_count, 0,
                                                     QTableWidgetItem(sweet.sweets_ui.label_3.text()))
                    main.main_ui.tableWidget.setItem(
                        row_count, 1, QTableWidgetItem("×" + str(self.bt1)))
                    main.main_ui.tableWidget.setItem(
                        row_count, 2, QTableWidgetItem(str(self.num_sweet1)))

            if 'Macaron' in name:
                main.main_ui.tableWidget.setItem(name.index('Macaron'), 1,
                                                 QTableWidgetItem("×" + str(self.bt2)))
                main.main_ui.tableWidget.setItem(name.index('Macaron'), 2,
                                                 QTableWidgetItem(str(self.num_sweet2)))
            if 'Macaron' not in name:
                if self.bt2 != 0:
                    row_count = main.main_ui.tableWidget.rowCount()
                    main.main_ui.tableWidget.insertRow(row_count)
                    main.main_ui.tableWidget.setItem(row_count, 0,
                                                     QTableWidgetItem(sweet.sweets_ui.label_4.text()))
                    main.main_ui.tableWidget.setItem(
                        row_count, 1, QTableWidgetItem("×" + str(self.bt2)))
                    main.main_ui.tableWidget.setItem(
                        row_count, 2, QTableWidgetItem(str(self.num_sweet2)))
            if 'Muffin' in name:
                main.main_ui.tableWidget.setItem(name.index('Muffin'), 1,
                                                 QTableWidgetItem("×" + str(self.bt4)))
                main.main_ui.tableWidget.setItem(name.index('Muffin'), 2,
                                                 QTableWidgetItem(str(self.num_sweet3)))
            if 'Muffin' not in name:
                if self.bt4 != 0:
                    row_count = main.main_ui.tableWidget.rowCount()
                    main.main_ui.tableWidget.insertRow(row_count)
                    main.main_ui.tableWidget.setItem(row_count, 0,
                                                     QTableWidgetItem(sweet.sweets_ui.label_9.text()))
                    main.main_ui.tableWidget.setItem(
                        row_count, 1, QTableWidgetItem("×" + str(self.bt4)))
                    main.main_ui.tableWidget.setItem(
                        row_count, 2, QTableWidgetItem(str(self.num_sweet3)))
            if 'Sundae' in name:
                main.main_ui.tableWidget.setItem(name.index('Sundae'), 1,
                                                 QTableWidgetItem("×" + str(self.bt5)))
                main.main_ui.tableWidget.setItem(name.index('Sundae'), 2,
                                                 QTableWidgetItem(str(self.num_sweet4)))
            if 'Sundae' not in name:
                if self.bt5 != 0:
                    row_count = main.main_ui.tableWidget.rowCount()
                    main.main_ui.tableWidget.insertRow(row_count)
                    main.main_ui.tableWidget.setItem(row_count, 0,
                                                     QTableWidgetItem(sweet.sweets_ui.label_10.text()))
                    main.main_ui.tableWidget.setItem(
                        row_count, 1, QTableWidgetItem("×" + str(self.bt5)))
                    main.main_ui.tableWidget.setItem(
                        row_count, 2, QTableWidgetItem(str(self.num_sweet4)))
    # Cancel
        else:
            if self.bt1 != 0:
                row_count = main.main_ui.tableWidget.rowCount()
                main.main_ui.tableWidget.insertRow(row_count)
                main.main_ui.tableWidget.setItem(
                    row_count, 0, QTableWidgetItem(sweet.sweets_ui.label_3.text()))
                main.main_ui.tableWidget.setItem(
                    row_count, 1, QTableWidgetItem("×" + str(self.bt1)))
                main.main_ui.tableWidget.setItem(
                    row_count, 2, QTableWidgetItem(str(self.num_sweet1)))
            if self.bt2 != 0:
                row_count = main.main_ui.tableWidget.rowCount()
                main.main_ui.tableWidget.insertRow(row_count)
                main.main_ui.tableWidget.setItem(
                    row_count, 0, QTableWidgetItem(sweet.sweets_ui.label_4.text()))
                main.main_ui.tableWidget.setItem(
                    row_count, 1, QTableWidgetItem("×" + str(self.bt2)))
                main.main_ui.tableWidget.setItem(
                    row_count, 2, QTableWidgetItem(str(self.num_sweet2)))
            if self.bt4 != 0:
                row_count = main.main_ui.tableWidget.rowCount()
                main.main_ui.tableWidget.insertRow(row_count)
                main.main_ui.tableWidget.setItem(
                    row_count, 0, QTableWidgetItem(sweet.sweets_ui.label_9.text()))
                main.main_ui.tableWidget.setItem(
                    row_count, 1, QTableWidgetItem("×" + str(self.bt4)))
                main.main_ui.tableWidget.setItem(
                    row_count, 2, QTableWidgetItem(str(self.num_sweet3)))
            if self.bt5 != 0:
                row_count = main.main_ui.tableWidget.rowCount()
                main.main_ui.tableWidget.insertRow(row_count)
                main.main_ui.tableWidget.setItem(
                    row_count, 0, QTableWidgetItem(sweet.sweets_ui.label_10.text()))
                main.main_ui.tableWidget.setItem(
                    row_count, 1, QTableWidgetItem("×" + str(self.bt5)))
                main.main_ui.tableWidget.setItem(
                    row_count, 2, QTableWidgetItem(str(self.num_sweet4)))


# Main
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    burger = Burgers()
    drink = Drinks()
    sweet = Sweets()
    # display home page
    main.person()
    # bind the button
    btn_burger = main.main_ui.pushButton_2
    btn_burger.clicked.connect(burger.nor_order)
    btn_drink = main.main_ui.pushButton_3
    btn_drink.clicked.connect(drink.pac_order)
    btn_sweet = main.main_ui.pushButton_4
    btn_sweet.clicked.connect(sweet.act_order)
    # init name array
    name = []
    sys.exit(app.exec_())
