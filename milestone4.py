#
#CS 177 - Milestone 4
#Tianze Wu -00323-50856
# Following the Coding Standards and Guidelines
# This program lets the user play Trinko Game, a Trivia game
#where the user answer five questions and gets to score points
#depending on how many they answer correctly. My custom feature
#is to have a socreboard where one gets to insert their name and
#play against their friends and see who ends up getting the most
#points. I put this custom feature in a separate function called
#leaderboard.

from graphics import *
import random

def board():
    #create graphical window
    win = GraphWin("Game Board", 500, 700, autoflush=False)
    #add image
    image = Image(Point(250, 50), "LetsPlay.gif").draw(win)
    #add white rectange
    whiteRect = Rectangle(Point(0, 600), Point(500, 700))
    whiteRect.setFill("white")
    whiteRect.draw(win)
    win.setBackground("light grey")
    #add two lines
    line1 = Line(Point(0, 100), Point(500, 100))
    line2 = Line(Point(0, 600), Point(500, 600))
    line1.setWidth(3)
    line2.setWidth(3)
    line1.draw(win)
    line2.draw(win)
    #chips
    chipc = 0
    word = "Chips: " + str(chipc)
    chip = Text(Point(100, 650), word)
    chip.setSize(24)
    chip.draw(win)
    #score
    scorec = 0
    word2 = "Score: " + str(scorec)
    score = Text(Point(400, 650), word2)
    score.setSize(24)
    score.draw(win)

    #return win and button
    return [win, chip, score]

def clicked(click, rect):
    #if there's no click return false
    if click == None:
        return False
    #variables to getX and getY
    x, y = click.getX(), click.getY()
    #variables to rectangle points
    point, point2 = rect.getP1(), rect.getP2()
    x1, y1=point.getX(), point.getY()
    x2, y2 = point2.getX(), point2.getY()
    #if variables within range return True
    if x1 <= x <= x2 and y1<= y <= y2:
        return True

def bins(win):
    #for loop range(8)
    for i in range(8):
        #create lines at the top
        upline = Line(Point((5+(70*i)), 100), Point((5+(70*i)), 139))
        upline.setWidth(3)
        upline.draw(win)
        #create lines at the bottom
        downline = Line(Point((5+(70*i)), 560), Point((5+(70*i)), 599))
        downline.setWidth(3)
        downline.draw(win)
    #create texts for all of the point values at the bottom
    array = [40, 0, 60, 100, 20, 0, 80]
    for x in range(len(array)):
        values = Text(Point((40+(70*x)), 580), array[x]).draw(win)

def pins(win):
    #list
    List = []
    #for loop range(5)
    for x in range(5):
        #for loop range(7)
        for i in range(7):
            #make 7 circles and append them to list
            circle1 = Circle(Point(40+(i*70), 180+(x*80)), 5).draw(win)
            circle1.setFill("black")
            List.append(circle1)
        #for loop range(6)
        for i in range(6):
            #make 6 circles and append them to list
            circle2 = Circle(Point(75+(i*70), 220+(x*80)), 5).draw(win)
            circle2.setFill("black")
            List.append(circle2)
    #return list
    return List


def makeQuiz():
    #make window
    win = GraphWin("Trivia", 400, 400)
    #set background
    win.setBackground("dark grey")
    #set image
    image = Image(Point(200, 40), "TriviaTime.gif").draw(win)
    #"" question
    question = Text(Point(200, 135), "").draw(win)

    #make four gold rectangles for answers
    one = Rectangle(Point(0, 180), Point(400, 225))
    one.setFill("gold")
    one.draw(win)
    two = Rectangle(Point(0, 225), Point(400, 270))
    two.setFill("gold")
    two.draw(win)
    three = Rectangle(Point(0, 270), Point(400, 315))
    three.setFill("gold")
    three.draw(win)
    four = Rectangle(Point(0, 315), Point(400, 360))
    four.setFill("gold")
    four.draw(win)

    #make four blank ""
    qone = Text(Point(200, 202), "").draw(win)
    qtwo = Text(Point(200, 247), "").draw(win)
    qthree = Text(Point(200, 292), "").draw(win)
    qfour = Text(Point(200, 337), "").draw(win)

    #bottom black rectangle
    bottom = Rectangle(Point(0, 360), Point(400, 400))
    bottom.setFill("black")
    bottom.draw(win)
    #question #1 text
    num = Text(Point(50, 380), "Question #1")
    num.setFill("white")
    num.draw(win)
    #correct answers text
    correct = Text(Point(350, 380), "Correct:  0")
    correct.setFill("white")
    correct.draw(win)

    #return values
    return win, one, two, three, four, question, qone, qtwo, qthree, qfour, num, correct

def pickQs():
    #open file
    file = open("questions.txt", "r", encoding="utf8")
    #initialize list
    List = []
    #readlines
    #for i in file.readlines()
    for i in file.readlines():
        #append i.split to list
        List.append(i.split(","))
    #shuffle list
    random.shuffle(List)
    #initialize dictionary
    d = dict([])
    tup = []

    #for i in 5
    for i in range(5):
        #append from list i 1-4
        tup.append(List[i][1])
        tup.append(List[i][2])
        tup.append(List[i][3])
        tup.append(List[i][4])
        #append only the letter (not \n)
        tup.append(List[i][5][:-1])
        #add to dictionary with question being key, tuple the list
        d[List[i][0]] = tuple(tup)
        #set tuple/list back to nothing
        tup = []
    file.close()
    #return d
    return d

def takeQuiz():
    #values from makeQuiz()
    win, one, two, three, four, question, qone, qtwo, qthree, qfour, num, correct = makeQuiz()
    #d = pickQs()
    d = pickQs()
    #initialize variables
    i = 0
    qcounter = 1
    ccounter = 0
    boo = False
    chance = 1
    cho = ["A", "B", "C", "D"]
    #strings for boxes that show up
    string = Text(Point(200, 125), "")
    cont = Text(Point(200, 175), "Click to continue")
    cont.setStyle("italic")
    #while true
    while True:
        #checkmouse
        mouse = win.checkMouse()
        #initialize variables and dictionary keys
        key = list(d.keys())[i]
        a = key.split()
        p = ""
        #for i in range(1, len(key split +1)
        for x in range(1, len(a)+1):
            #if x/5 == round x/5
            if x/5 == round(x/5):
                #add to p with \n
                p += a[x-1] + "\n"
            #else
            else:
                #add to p with " "
                p += a[x-1] + " "
        #set question to p
        question.setText(p)
        #set answers
        qone.setText(d[key][0])
        qtwo.setText(d[key][1])
        qthree.setText(d[key][2])
        qfour.setText(d[key][3])

        #if not mouse then continue
        if not mouse:
            continue
        #if mouse
        if mouse:
            #answer 1 mouse click
            if 225>mouse.getY()>180 and d[key][4] == "A":
                boo = True
            #answer 2 mouse click
            elif 270>mouse.getY()>225 and d[key][4] == "B":
                boo = True
            #answer 3 mouse click
            elif 315>mouse.getY()>270 and d[key][4] == "C":
                boo = True
            #answer 4 mouse click
            elif 360>mouse.getY()>315 and d[key][4] == "D":
                boo = True
            #else if not clicked on answer box then continue
            elif 180>mouse.getY()>0 or 400>mouse.getY()>360:
                continue
                        
            #else answer is false
            else:
                boo = False

        #yellow/red rectangle and white rectangle
        corr = Rectangle(Point(100, 100), Point(300, 200))
        white = Rectangle(Point(95, 95), Point(305, 205))
        white.setFill("white")

        #if answer is correct
        if boo == True:
            #draw white rect, yellow rect, set correct string, increase correct counter
            white.draw(win)
            corr.setFill("yellow")
            corr.draw(win)
            string.setText("You are correct!")
            string.setStyle("bold")
            string.draw(win)
            cont.draw(win)
            ccounter += 1
            st2 = "Correct:  " + str(ccounter)
            correct.setText(st2)

        #if answer is incorrect
        if boo == False:
            #draw white rect, red rect, set incorrect string
            white.draw(win)
            corr.setFill("red")
            corr.draw(win)
            string.setText("Sorry, that is incorrect")
            string.setStyle("bold")
            string.draw(win)
            cont.draw(win)

        #while true
        while True:
            #checkmouse
            click = win.checkMouse()
            #if not click continue
            if not click:
                continue
            #if click on the box
            if click:
                if 300>click.getX()>100 and 200>click.getY()>100:
                    #undraw white rect, yellow/red rect, string, and increase question counter and break
                    corr.undraw()
                    white.undraw()
                    string.undraw()
                    cont.undraw()
                    qcounter += 1
                    break
        #strings to add together to set text
        st = "Question #" + str(qcounter)
        num.setText(st)
        
        #another counter for question increments
        i += 1
        #if question counter is 6 then break
        if qcounter == 6:
            break

    #draw white rect, yellow rect, and completed quiz string and set question counter to "All done!"
    white.draw(win)
    corr.setFill("yellow")
    corr.draw(win)
    an = "Your final score is: " + str(ccounter)
    string.setText(an)
    string.setStyle("bold")
    string.draw(win)
    cont.draw(win)
    num.setText("All done!")

    #if getmouse then close window
    
    while True:
        closing = win.getMouse()
        if 300>closing.getX()>100 and 200>closing.getY()>100:
            win.close()
            break
        else:
            continue
    print(ccounter)
    return ccounter

def control():
    #create window
    win = GraphWin("Game Control", 500, 200)
    #add images
    image = Image(Point(250, 50), "TrinkoTitle.gif").draw(win)
    #add play rectangle
    play = Rectangle(Point(125, 135), Point(235, 165))
    play.setFill("green")
    play.draw(win)
    #add exit rectangle
    ex = Rectangle(Point(265, 135), Point(375, 165))
    ex.setFill("red")
    ex.draw(win)
    #add play text
    playText = Text(Point(180, 150), "PLAY")
    playText.setTextColor("white")
    playText.setSize(20)
    playText.draw(win)
    #add exit text
    exText = Text(Point(320, 150), "EXIT")
    exText.setTextColor("white")
    exText.setSize(20)
    exText.draw(win)
    #while
    while True:
        #checkmouse
        mouse = win.checkMouse()
        #if not mouse then contineu
        if not mouse:
            continue
        #if mouse is in play button close window and return True
        if mouse:
            if 235>mouse.getX()>125 and 165>mouse.getY()>135:
                win.close()
                return True
            #if mouse in exit then break
            if 375>mouse.getX()>265 and 165>mouse.getY()>135:
                break
            else:
                continue
    #close window
    win.close()

def drop(chip, win, pin, chiptext, scoretext):
    #bins and pins function
    bins(win)
    pins(win)
    #initialize values
    score = 0
    List = [5, 75, 145, 215, 285, 355, 425, 495]
    points = [40, 0, 60, 100, 20, 0, 80]
    c = chip
    #while chip is over 0
    while c > 0:
        #chip text
        ct = "Chip: " + str(c)
        chiptext.setText(ct)
        #check mouse
        mouse = win.checkMouse()
        #if not mouse then continue
        if not mouse:
            continue
        #if mouse
        if mouse:
            #if mouse in bins
            if 495>mouse.getX()>5 and 139>mouse.getY()>100:
                #divide x value by 70 and then drop it from the bin
                val = 40 + 70*(mouse.getX()//70)
                #initialize values
                dx = 0
                dy=0
                li = [-8, 8]
                #change chip text
                c = c - 1
                ct = "Chip: " + str(c)
                chiptext.setText(ct)
                #make ball
                ball = Circle(Point(val, 120), 15)
                ball.setFill("yellow")
                ball.draw(win)
                #while ball is above the bottom bin
                while ball.getCenter().getY()<575:
                    #dy = dy+4
                    dy = dy + 4
                    #dx = dx*.8
                    dx = dx* .8
                    #ball move and update
                    ball.move(dx, dy)
                    update(30)
                    # for i in pin
                    for i in pin:
                        #if ball is touching pin
                        if ((ball.getCenter().getY()-i.getCenter().getY())**2+(ball.getCenter().getX()-i.getCenter().getX())**2)**.5 <= 25:
                            #add a red ball while touching
                            color = Circle(i.getCenter(), 5)
                            color.setFill("red")
                            color.draw(win)
                            #change dy and dx
                            dy = dy*-.05
                            dx = dx*-1
                            if ball.getCenter().getX()>i.getCenter().getX():
                                dx = dx + 7
                            elif ball.getCenter().getX()<i.getCenter().getX():
                                dx = dx -7
                            elif ball.getCenter().getX() == i.getCenter().getX():
                                dx = dx + random.choice(li)
                            #ball move and update
                            ball.move(dx, dy)
                            update(30)
                            color.undraw()
                        #if ball touchings the left and right edges then change dx
                        if ball.getCenter().getX()<= 15 or ball.getCenter().getX() >= 485:
                            dx = dx*-1
                            ball.move(dx, dy)
                #add score based on which is closest
                endx = int((ball.getCenter().getX()//70))
                #change score text
                score += points[endx]
                st = "Score: " + str(score)
                scoretext.setText(st)
            else:
                continue
    #rectangle message with score
    message = Rectangle(Point(150, 300), Point(350, 400))
    message.setFill("yellow")
    message.draw(win)
    totalscore = "Your score is " + str(score)
    scoremess = Text(Point(250, 350), totalscore).draw(win)
    #while
    while True:
        #check mouse
        click = win.checkMouse()
        #if not mouse continue
        if not click:
            continue
        #if get mouse in rectangle then close window and break
        if click:
            if 350>click.getX()>150 and 400>click.getY()>300:
                win.close()
                return score
            #else continue
            else:
                continue

def leaderboard(points, li):
    #first graphic window for name
    name = GraphWin("Insert Name", 400, 200)
    #entry with text
    nameEntry = Entry(Point(200, 100), 10).draw(name)
    ent = Text(Point(200, 50), "ENTER YOUR NAME:").draw(name)
    #submit button
    sub = Rectangle(Point(150, 135), Point(250, 175))
    sub.setFill("red")
    sub.draw(name)
    subText = Text(Point(200, 150), "SUBMIT").draw(name)
    #initialize lists
    List = li
    List2 = []
    List3 = []
    #while trye
    while True:
        #checkmouse
        mouse = name.checkMouse()
        #if there is nothing in entry then continue
        if not nameEntry:
            continue
        #if not mouse then continue
        if not mouse:
            continue
        #if mouse
        if mouse:
            #if mouse in submit button
            if 250>mouse.getX()>150 and 175>mouse.getY()>135:
                #append name entry with points
                List.append([nameEntry.getText(), points])
                #close win and break
                name.close()
                break
    #append point values to a different list
    for x in List:
        List2.append(int(x[1]))
    #make another window to show leaderboard
    win = GraphWin("Scoreboard", 500, 500)
    win.setBackground("white")
    leader = Text(Point(250, 100), "SCORES")
    leader.setSize(24)
    leader.setStyle("bold")
    leader.draw(win)
    #for x in length of list with point values
    for x in range(len(List2)):
        #max of list
        high = max(List2)
        #for i in original list
        for i in range(len(List)):
            #if max == point
            if high == List[i][1] and (List[i] not in List3):
                List3.append(List[i])
                #set string equal to their name and points
                string = str(List[i][0]) + ": " + str(List[i][1])
                #show text
                n = Text(Point(250, 150+(x*20)), string).draw(win)
                #string back to ""
                string = ""
        #remove max
        List2.remove(high)
    #get mouse
    win.getMouse()
    #close win
    win.close()
    #return list
    return List
    
            
def main():
    #list = []
    List = []
    #while control() is True
    while control():
        #var = take Quiz
        num = takeQuiz()
        #initialize values of board()
        win, chip, score = board()
        points = drop(num, win, pins(win), chip, score)
        List = leaderboard(points, List)
