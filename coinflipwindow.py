from graphics import *
from random import randrange
import time
def main():
    win = GraphWin("Coin Flip", 500,500)
    welcome_txt = Text(Point(250,20),"Welcome to Heads or Tails")
    welcome_txt.setSize(20)
    welcome_txt.draw(win)
    
    question_txt = Text(Point(250,100),"How many times do you want to flip the coin?")
    question_txt.setSize(20)
    question_txt.draw(win)
    
    entry_box = Entry(Point(480,100),5)
    entry_box.draw(win)
    
    
    
    
    
    
    answer = 'y'
    while answer == 'y':
        win.getMouse()
        x = entry_box.getText()
        x = int(x)
        question_txt.undraw()
        entry_box.undraw()        
        headcount = 0
        tailscount = 0        
        for i in range(x):
            coin = randrange(2)
            if coin == 0:
                
                headcount += 1
                head_txt = Text(Point(100,350),"Heads has been flipped")
                times_txt = Text(Point(230,350),"times.")
                headcount_txt = Text(Point(190,350),headcount)
                head_txt.setSize(15)
                times_txt.setSize(15)
                headcount_txt.setSize(15)
                             
                head_txt.draw(win)
                times_txt.draw(win)
                headcount_txt.draw(win)
                time.sleep(.15)
                headcount_txt.undraw()
                
                
                
                
                
            elif coin == 1:
                tailscount += 1
                tails_txt= Text(Point(350,350),"Tails has been flipped")
                times1_txt = Text(Point(480,350),"times.")
                tailscount_txt = Text(Point(440,350),tailscount)
                tails_txt.setSize(15)
                times1_txt.setSize(15)
                tailscount_txt.setSize(15)
                tailscount_txt.draw(win)
                times1_txt.draw(win)
                tails_txt.draw(win)
                time.sleep(.15)
                tailscount_txt.undraw()
                
        tailscount_txt.draw(win)
        headcount_txt.draw(win)
        question2_txt = Text(Point(250,400),"Do you want to play again? (y or n)")
        entry2= Entry(Point(250,430),5)
        entry2.draw(win)
        question2_txt.draw(win)
        win.getMouse()
        answer = entry2.getText()
        tailscount_txt.undraw()
        headcount_txt.undraw()
        if answer== 'y':
            entry_box.draw(win)
            question_txt.draw(win)
        
    
    
    win.close()
main()