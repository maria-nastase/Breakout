add_library('minim')
import random
######################################################################################
# global variables
score = 0
lives = 3
allClear = False
mode = "play"
# variables used to control paddle
controlKeyX = 350
paddlePosition = 350
# variables used to control ball and ball speed
lvl = 1
highestLvl = 1
ballSpeedLvl = 1
ballSpeed = 0.5 + ballSpeedLvl * 0.5
ballSpeedX = ballSpeed
ballSpeedY = -ballSpeed
ballX = random.randrange(100, 600)
ballY = 600
# variables used to control bricks
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
brickCounter = 0

######################################################################################
# main functions
def setup():
    global img, interface, ballTap, brickTap, click, lostLifeSound, winSound, music
    size(700,1000)
    interface = 0
    frameRate(120)
    img = loadImage("img.PNG")
    # sound effects
    minim = Minim(this)
    ballTap = minim.loadSample("mixkit-game-ball-tap-2073.wav")
    brickTap = minim.loadSample("mixkit-unlock-game-notification-253.wav")
    click = minim.loadSample("mixkit-sci-fi-positive-notification-266.wav")
    lostLifeSound = minim.loadSample("mixkit-player-losing-or-failing-2042.wav")
    winSound = minim.loadSample("mixkit-game-level-completed-2059.wav")
    music = minim.loadFile("arcade-game-music-loop.mp3")
    music.loop()
    
def draw():
    if interface == 0:
        welcomeScreen()
    elif interface == 1:
        gameplayScreen()
    elif interface == 2:
        endScreen()
        
######################################################################################
# interfaces    
def welcomeScreen():
    
    # background colour
    background(30,25,35)
    
    # effect image
    image(img,350,100)
    #"BREAKOUT" title shadow
    fill(255)
    textSize(120)
    text("BREAKOUT",37,303)
    
    # "BREAKOUT" title
    fill(100,100,150)
    textSize(120)
    text("BREAKOUT",40,300)
    
    # decorations
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
    
    # instructions
    textSize(40)
    text("INSTRUCTIONS & RULES",130,450)
    textSize(20)
    text("-A layer of bricks lines the top third of the screen and the goal",50,500)
    text("is to destroy them all by repeatedly bouncing a ball off a paddle.",50,530)
    text("-Eliminate the bricks by using the walls and/or the paddle below",50,560)
    text("to hit the ball against them.",50,590)
    text("-If the player's paddle misses the ball's rebound, they will lose",50,620)
    text("a turn. The player has three turns to try to clear the screen of",50,650)
    text("bricks.",50,680)
    text("-The speed of the ball increases after making contact with the",50,710)
    text("next colour of bricks.", 50, 740)
    
    # start button
    stroke(255)
    fill(170,80,75)
    rect(200,890,300,70)
    textSize(30)
    fill(255)
    text("PRESS TO START",235,933)

def gameplayScreen():
    global score, controlKeyX, paddlePosition, ballX, ballY, ballSpeedX, ballSpeedY
   
    # background colour
    background(30,25,35)
    # functions
    scoreDisplay()
    livesDisplay()
    pauseButtomDisplay()
    gameArea()
    checkWin() 
    drawBricks()
    drawPaddle()
    drawBall()
    lifeCount()
    drawControlArea()
    
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
    
    # detect win or loss
    rect(100, 440, 500, 100)
    fill(170,80,75)
    textSize(30)
    if allClear == True:
        text("Congrats!! You've won the game!!",110,500)
    else:
        if highestLvl <= 2:
            text("Nice Try!!",290,500)
        elif highestLvl > 2:
            text("Good job!! Close game!!",180,500)
            
    # score display
    fill(255)
    rect(175, 600, 350, 140)
    fill(170,80,75)
    textSize(40)
    line(330,650,330,700)
    text("LEVEL",195, 650)
    text("SCORE",355, 650)
    textSize(60)
    text(highestLvl,230,715)
    text(score,350,715)
    
    # try again button
    fill(255)
    rect(150, 800, 400, 70)
    fill(170,80,75)
    textSize(40)
    text("TRY AGAIN", 200, 850)
    noFill()
    strokeWeight(6)
    stroke(170,80,75)
    arc(455, 835, 40, 40, 0, PI + HALF_PI)
    line(460, 837, 475, 817)
    line(490, 837, 475, 817)
    
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
    fill(255)
    # to pause
    if mode == "play":
        textSize(40)
        text("Pause",555,85)
    # to resume
    elif mode == "pause":
        textSize(30)
        text("Resume",555,85)

def gameArea():
    global ballX, ballY, ballSpeedX, ballSpeedY, lives
    
    fill(100)
    rect(50,200,600,700)
    
    # ball bounces off sides
    if ballX < 50:
        ballSpeedX = -ballSpeedX
        ballTap.trigger()
    elif ballX > 650:
        ballSpeedX = -ballSpeedX
        ballTap.trigger()
    if ballY < 200:
        ballSpeedY = -ballSpeedY
        ballTap.trigger()
    # ball comes back on screen if user misses it
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
    global brickX,brickY,bricks,brickColour, ballX, ballY, ballSpeedX, ballSpeedY, brickCounter
    
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
                
                # ball bounces off bricks
                if ballX >= brickX + 55 and ballX <= brickX + 105 and ballY >= brickY + 210 and ballY <= brickY + 240 + 20:
                    if ballX >= brickX + 55 - 2.5 and ballX <= brickX + 55 + 2.5 or ballX >= brickX + 105 - 2.5 and ballX <= brickX + 105 + 2.5:
                        ballSpeedX = -ballSpeedX
                    if ballY >= brickY + 210 - 2.5 and ballY <= brickY + 210 + 2.5 or ballY >= brickY + 240 - 2.5 and ballY >= brickY + 240 + 2.5:
                        ballSpeedY = -ballSpeedY
                    brickTap.trigger()
                    addLvlAndScore(yNum)
                    addSpeed()
                    # make bricks disappear when touched
                    bricks[yNum][xNum] = 0
                    brickCounter += 1

def addLvlAndScore(yNum):
    global lvl,score
    
    # find level of brick touched (based on colour)
    # calculate score
    if yNum == 6 or yNum == 7:
        lvl = 1
        score += 10
    elif yNum == 4 or yNum == 5:
        lvl = 2
        score += 20
    elif yNum == 2 or yNum == 3:
        lvl = 3
        score += 30
    elif yNum == 0 or yNum == 1:
        lvl = 4
        score += 40

def addSpeed():
    global lvl,highestLvl,ballSpeedLvl,ballSpeed,ballSpeedX,ballSpeedY
    
    # ball speed increases as the user touches higher bricks (based on colour)
    if lvl > highestLvl:
        highestLvl = lvl
        ballSpeedLvl = highestLvl
        ballSpeed = 0.5 + ballSpeedLvl * 0.5
        ballSpeedX = ballSpeed
        ballSpeedY = ballSpeed
        
def drawPaddle():
    global ballX, ballY, ballSpeedX, ballSpeedY, ballSpeed
    
    fill(36, 98, 255)
    rect(controlKeyX, 800, 50, 10)
    # ball bounces off paddle
    # the angle changes so that the ball does not follow the same path continously
    if ballY >= 800 and ballY <= 810:
        if ballX >= controlKeyX and ballX <= controlKeyX + 50:
            ballTap.trigger()
            if ballX >= controlKeyX and ballX <= controlKeyX+10 or ballX > controlKeyX+40 and ballX <= controlKeyX+50:
                ballSpeedY = -ballSpeed - 0.5
                if ballSpeedX < 0:
                    ballSpeedX = -1
                else:
                    ballSpeedX = 1
            if ballX > controlKeyX+10 and ballX <= controlKeyX+20 or ballX > controlKeyX+30 and ballX <= controlKeyX+40:
                ballSpeedY = -ballSpeed  - 0.5
                if ballSpeedX < 0:
                    ballSpeedX = 0.5
                else:
                    ballSpeedX = 0.5
            elif ballX > controlKeyX+20 and ballX <= controlKeyX+30:
                    ballSpeedY = -ballSpeed - 1
                    ballSpeedX = -0.5
            
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
        lostLifeSound.trigger()
        # end game if there are no more lives
        if lives == 0:
            interface = 2

def checkWin():
    global allClear, interface
    
    # check if all bricks are gone
    if brickCounter == 80:
        winSound.trigger()
        allClear = True
        interface = 2
        
def drawControlArea():
    
    fill(100,75,75)
    rect(0,900,699,100)
    fill(0)
    rect(50,940,600,20)
    fill(100)
    rect(controlKeyX,920,50,60) #draw controlKey

def mouseDragged():
    global controlKeyX
    
    # control paddle with mouse
    if mouseX >=75 and mouseX <=625:
        controlKeyX = mouseX-25
    elif mouseX <50:
        controlKeyX = 50
    elif mouseX >650:
        controlKeyX = 600
    paddlePosition = controlKeyX     
 
def mousePressed():
    global interface, lives, bricks, score, lvl, highestLvl, ballSpeedLvl, ballSpeed, ballSpeedX, ballSpeedY, originalBallSpeedX, originalBallSpeedY, mode, allClear, brickCounter
    
    if interface == 0:
        # start button
        if mouseX >= 200 and mouseX <= 500 and mouseY >= 890 and mouseY <= 960:
            click.trigger()
            interface = 1
            
    elif interface == 1:
        # pause button
        if mode == "play":
            if mouseX >= 540 and mouseX <= 680 and mouseY >= 10 and mouseY <= 140: 
                click.trigger()
                music.pause()
                mode = "pause" 
                originalBallSpeedX = ballSpeedX
                originalBallSpeedY = ballSpeedY
                ballSpeedX = 0
                ballSpeedY = 0
        # resume button
        elif mode == "pause":
            if mouseX >= 540 and mouseX <= 680 and mouseY >= 10 and mouseY <= 140:
                click.trigger()
                music.loop()
                mode = "play"
                ballSpeedX = originalBallSpeedX
                ballSpeedY = originalBallSpeedY
                
    elif interface == 2:
        # try again button
        if mouseX >= 150 and mouseX <= 550 and mouseY >= 800 and mouseY <= 870:
            click.trigger()
            # reset variables
            interface = 0
            lives = 3
            score = 0
            lvl = 1
            highestLvl = 1
            ballSpeedLvl = 1
            ballSpeed = 0.5 + ballSpeedLvl * 0.5
            allClear = False
            brickCounter = 0
            # redraw bricks
            for y in range(len(bricks)):
                for x in range(len(bricks[y])):
                    bricks[y][x] = 1
            
def keyPressed():
    global controlKeyX, paddlePosition
    
    # control paddle with arrow keys
    if key == CODED:
        if keyCode == LEFT:
            controlKeyX += -10
        elif keyCode == RIGHT:
            controlKeyX += 10
        
        if controlKeyX < 50:
            controlKeyX = 50
        elif controlKeyX > 600:
            controlKeyX = 600
