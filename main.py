from logic import *

'''
def main1():
    application2 = QApplication([])
    window2 = LogicLogin()
    window2.setGeometry(100, 100, 300, 100)
    window2.show()
    application2.exec()
'''

def main():
    application = QApplication([])
    window = Logic()
    window.setGeometry(100, 100, 300, 100)
    window.show()
    application.exec()


if __name__ == '__main__':
    main()
