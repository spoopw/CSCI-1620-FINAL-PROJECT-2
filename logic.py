from PyQt6.QtWidgets import *

from guiBet import *

import random as r


class Logic(QMainWindow, Ui_MainWindow):

    def __init__(self):

        super().__init__()
        self.setupUi(self)

        self.button_bet.clicked.connect(lambda: self.bet())
        self.button_howtoplay.clicked.connect(lambda: self.howtoplay())
        self.button_cheat.clicked.connect(lambda: self.cheat())
        self.button_exit.clicked.connect(lambda: self.exit())

        self.__balance: float = 500
        self.__bet: float = 0
        self.__guess: int = 0
        self.__roll1: int = 0
        self.__roll2: int = 0
        self.__roll3: int = 0
        self.__amount_rolled: int = 0
        self.label_balance.setText(f'${self.__balance}')

    def bet(self):
        """
        First calls function self.check_information to validate info. Then does the bet.
        :return: Void function
        """
        self.label_howtoplay.setText('')
        if self.check_information(self.__balance, self.input_bet.text()):

            bet = self.input_bet.text()

            self.__roll1 = r.randint(1, 6)
            self.__roll2 = r.randint(1, 6)
            self.__roll3 = r.randint(1, 6)

            if self.radio_1.isChecked():
                self.__guess = 1
            elif self.radio_2.isChecked():
                self.__guess = 2
            elif self.radio_3.isChecked():
                self.__guess = 3
            elif self.radio_4.isChecked():
                self.__guess = 4
            elif self.radio_5.isChecked():
                self.__guess = 5
            elif self.radio_6.isChecked():
                self.__guess = 6
            else:
                self.label_agenda.setText('Please select a number to guess')
                return

            self.label_agenda.setText('')
            if self.__guess == self.__roll1:
                self.__amount_rolled += 1
            if self.__guess == self.__roll2:
                self.__amount_rolled += 1
            if self.__guess == self.__roll2:
                self.__amount_rolled += 1

            if self.__amount_rolled == 0:
                self.label_winnings.setText(f'You lost ${bet}')
                self.__balance -= float(bet)
                self.label_balance.setText(f'${self.__balance:.2f}')
            elif self.__amount_rolled == 1:
                self.label_winnings.setText(f'You won ${float(bet)} (broke even)')
            elif self.__amount_rolled == 2:
                self.label_winnings.setText(f'You won ${float(bet) * 2}')
                self.__balance += float(bet)
                self.label_balance.setText(f'${self.__balance:.2f}')
            elif self.__amount_rolled == 3:
                self.label_winnings.setText(f'You won ${float(bet) * 10}')
                self.__balance += float(bet) * 10
                self.label_balance.setText(f'${self.__balance:.2f}')

            self.__amount_rolled = 0

    def check_information(self, balance, bet):
        """
        Checks for valid information
        :param balance: The balance of the user
        :param bet: The bet the user set
        :return: False if bet invalid, true if bet valid
        """
        try:
            int(bet)

        except ValueError:
            self.label_agenda.setText('Please enter a valid bet.')
            return False

        else:
            bet = int(bet)
            self.__bet = int(self.__bet)

        if balance < bet:
            self.label_agenda.setText('You cannot bet more than your balance.')
            return False

        return True

    def howtoplay(self):
        self.label_howtoplay.setText(f'First, enter a bet amount. Then, guess a number.\n'
                                     f'3 dice will be rolled.\n If your guessed number is rolled 0 times,'
                                     f'you lose your bet.\n If your guessed number is rolled 1 time,'
                                     f'you win back your bet.\n If your guessed number is rolled 2 times,'
                                     f'you win twice your bet.\n If your guessed number is rolled 3 times,'
                                     f'you win 10x your bet.')
        self.label_winnings.setText('')

    def cheat(self):
        self.label_howtoplay.setText('')
        self.__balance += 100
        self.label_balance.setText(f'${self.__balance}')

    def exit(self):
        exit()
