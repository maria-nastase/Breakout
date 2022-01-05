add_library('minim')
import random
######################################################################################
#global variables
score = 0
lvl = 1
highestLvl = 1
ballSpeedLvl = 1
controlKeyX = 350
paddlePosition = 350
ballSpeed = 1 + ballSpeedLvl * 0.5
ballSpeedX = ballSpeed
ballSpeedY = -ballSpeed
ballX = random.randrange(100, 600)
ballY = 600
lives = 3

bricks = [
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1,1,1],
]
brickX = 0
brickY = 0
brickColour = 0
######################################################################################
#main functions
def setup():
    global img, interface
    size(700,1000)
    img = loadImage("img.PNG")
    interface = 0
    frameRate(120)

def draw():
    if interface == 0:
        welcomeScreen()
    elif interface == 1:
        gameplayScreen()
    elif interface == 2:
        endScreen()
        
######################################################################################
#interfaces    
def welcomeScreen():
    #background colour
    background(30,25,35)
 
    #effect image
    image(img,350,100)
    #"BREAKOUT" title shadow
    fill(255)
    textSize(120)
    text("BREAKOUT",37,303)
    
    #"BREAKOUT" title
    fill(100,100,150)
    textSize(120)
    text("BREAKOUT",40,300)
    
    #decorations
    noStroke()
    fill(255)
    rect(425,335,190,50)
    fill(170,80,75)
    rect(430,330,190,50)
    strokeWeight(12)
    stroke(170,80,75)
    line(200,350,210,350)
    line(230,350,270,350)
    line(290,350,410,350)
    line(170,375,180,375)
    line(200,375,250,375)
    line(270,375,390,375)
    fill(255)
    textSize(23)
    text("ARCADE",455,355)
    text("GAME",530,370)
    
    #Instruction
    textSize(40)
    text("INSTRUCTIONS & RULES",130,450)
    textSize(20)
    text("-a layer of bricks lines the top third of the screen and the goal",50,500)
    text("is to destroy them all by repeatedly bouncing a ball off a paddle",50,530)
    text(" into them.",50,560)
    text("-by using the walls and/or the paddle below to hit the ball",50,590)
    text("against the bricks and eliminate them.",50,620)
    text("-If the player's paddle misses the ball's rebound, they will lose",50,650)
    text("a turn. The player has three turns to try to clear two screens of",50,680)
    text("bricks.",50,710)
    text("The paddle shrinks to one-half its size after the ball has broken",50,740)
    text("through the red row and hit the upper wall.",50,770)
    text("-Ball speed increases at specific intervals: after four hits, after",50,800)
    text("twelve hits, and after making contact with the orange and red",50,830)
    text("rows.",50,860)
    
    #press to start
    stroke(255)
    fill(170,80,75)
    rect(200,890,300,70)
    textSize(30)
    fill(255)
    text("PRESS TO START",235,933)

def gameplayScreen():
    global score, controlKeyX, paddlePosition, ballX, ballY, ballSpeedX, ballSpeedY
    #700x1000
    #background colour
    background(30,25,35)
    scoreDisplay()
    livesDisplay()
    pauseButtomDisplay()
    gameArea()
    drawBricks()
    drawPaddle()
    drawBall()
    lifeCount()
    drawControlArea()
######################################################################################    
#functions
def scoreDisplay():
    global score
    strokeWeight(1)
    stroke(255)
    fill(100,75,75)
    rect(0,0,699,150)
    rect(20,10,210,130)
    textSize(60)
    fill(255)
    text("Score:",40,60)
    textAlign(CENTER)
    text(score,115,130)
    textAlign(LEFT)
        
def livesDisplay():
    fill(100,75,75)
    rect(260,10,250,130)
    textSize(40)
    fill(255)
    text("Lives left:",280,60)
    text(lives,420,120)
    
def pauseButtomDisplay():
    fill(100,75,75)
    rect(540,10,140,130)
    textSize(30)
    fill(255)
    text("Pause",565,50)
    text("/",600,80)
    text("resume",555,115)

def gameArea():
    global ballX, ballY, ballSpeedX, ballSpeedY, lives
    fill(100)
    rect(50,200,600,700)
    if ballX < 50:
        ballSpeedX = ballSpeed
    elif ballX > 650:
        ballSpeedX = -ballSpeed
    if ballY < 200:
        ballSpeedY = ballSpeed
    elif ballY > 900:
        ballX = random.randrange(100, 600)
        ballY = 600

def drawBrick():
    global brickX,brickY,brickColour,brickColours
    noStroke()
    if brickColour == 0:
        fill(255, 17, 0)
    elif brickColour == 1:
        fill(255, 111, 0)
    elif brickColour == 2:
        fill(255, 238, 0)
    elif brickColour == 3:
        fill(0, 255, 4)
    rect(55+brickX,210+brickY,50,30)

def drawBricks():
    global brickX,brickY,bricks,brickColour, ballX, ballY, ballSpeedX, ballSpeedY, ballSpeed, lvl, highestLvl, ballSpeedLvl, score
    for yNum in range(8):
        for xNum in range(10):
            brickX = xNum*60
            brickY = yNum*40
            if bricks[yNum][xNum] == 1:
                if yNum == 0 or yNum == 1:
                    brickColour = 0
                if yNum == 2 or yNum == 3:
                    brickColour = 1
                if yNum == 4 or yNum == 5:
                    brickColour = 2
                if yNum == 6 or yNum == 7:
                    brickColour = 3
                drawBrick()
                
                if ballX >= brickX + 55 and ballX <= brickX + 105 and ballY >= brickY + 210 and ballY <= brickY + 240 + 30:
                    # change ball speed and calculate score
                    if yNum == 6 or yNum == 7:
                        lvl = 1
                        score += 10
                    if yNum == 4 or yNum == 5:
                        lvl = 2
                        score += 20
                    elif yNum == 2 or yNum == 3:
                        lvl = 3
                        score += 30
                    elif yNum == 0 or yNum == 1:
                        lvl = 4
                        score += 40
                    if lvl > highestLvl:
                        highestLvl = lvl
                        ballSpeedLvl = highestLvl
                        ballSpeed = 1 + ballSpeedLvl * 0.5
                        ballSpeedX = ballSpeed
                        ballSpeedY = ballSpeed
                    ballSpeedY = -ballSpeedY
                    # make bricks disappear when touched
                    bricks[yNum][xNum] = 0

def drawPaddle():
    global ballX, ballY, ballSpeedX, ballSpeedY, ballSpeed
    fill(36, 98, 255)
    rect(controlKeyX, 800, 50, 10)
    if ballY >= 800 and ballY <= 810:
        if ballX >= controlKeyX and ballX <= controlKeyX + 50:
            ballSpeedY = -ballSpeed
            
def drawBall():
    global ballX, ballY, ballSpeedX, ballSpeedY
    fill(255)
    ellipse(ballX, ballY, 20, 20)
    ballX += ballSpeedX
    ballY += ballSpeedY
    
def lifeCount():
    global lives, ballY, interface
    if ballY > 900:
        lives = lives - 1
        if lives == 0:
            print(lives)
            interface = 2
    
def drawControlArea():
    fill(100,75,75)
    rect(0,900,699,100)
    fill(0)
    rect(50,940,600,20)
    fill(100)
    rect(controlKeyX,920,50,60) #draw controlKey
    
def endScreen():
    #background colour
    background(30,25,35)
 
    #effect image
    image(img,350,100)
    #"BREAKOUT" title shadow
    fill(255)
    textSize(120)
    text("BREAKOUT",37,303)
    
    #"BREAKOUT" title
    fill(100,100,150)
    textSize(120)
    text("BREAKOUT",40,300)
    
    #decorations
    noStroke()
    fill(255)
    rect(425,335,190,50)
    fill(170,80,75)
    rect(430,330,190,50)
    strokeWeight(12)
    stroke(170,80,75)
    line(200,350,210,350)
    line(230,350,270,350)
    line(290,350,410,350)
    line(170,375,180,375)
    line(200,375,250,375)
    line(270,375,390,375)
    fill(255)
    textSize(23)
    text("ARCADE",455,355)
    text("GAME",530,370)
    
    rect(250, 500, 200, 50)
    fill(170,80,75)
    text("TRY AGAIN", 275, 535)
    noFill()
    strokeWeight(2)
    stroke(170,80,75)
    arc(415, 525, 20, 20, 0, PI + HALF_PI)
    line(420, 527, 425, 517)
    line(425, 517, 430, 527)
 
def mouseDragged():
    global controlKeyX
    if mouseX >=75 and mouseX <=625:
        controlKeyX = mouseX-25
    elif mouseX <50:
        controlKeyX = 50
    elif mouseX >650:
        controlKeyX = 600
    paddlePosition = controlKeyX     
 
def mousePressed():
    global interface, lives, bricks, score
    if interface == 0:
        if mouseX >= 200 and mouseX <= 500 and mouseY >= 890 and mouseY <= 960:
            interface = 1
    elif interface == 2:
        if mouseX >= 250 and mouseX <= 450 and mouseY >= 500 and mouseY <= 550:
            interface = 0
            lives = 3
            score = 0
            for y in range(len(bricks)):
                for x in range(len(bricks[y])):
                    bricks[y][x] = 1
            
def keyPressed():
    global controlKeyX, paddlePosition
    if key == CODED:
        if keyCode == LEFT:
            controlKeyX += -10
        elif keyCode == RIGHT:
            controlKeyX += 10
        
        if controlKeyX < 50:
            controlKeyX = 50
        elif controlKeyX > 600:
            controlKeyX = 600
