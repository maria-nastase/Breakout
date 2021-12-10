score = 0
ballSpeedLvl = 1
controlKeyX = 350
paddlePosition = 350

def setup():
    global img, interface
    size(700,1000)
    img = loadImage("img.PNG")
    interface = 0

def draw():
    if interface == 0:
        welcomeScreen()
    elif interface == 1:
        gameplayScreen()
    
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
    global score, controlKeyX, paddlePosition
    #700x1000
    #background colour
    background(30,25,35)
    
    #scoredisplay
    strokeWeight(1)
    stroke(255)
    fill(100,75,75)
    rect(0,0,699,150)
    rect(20,10,210,130)
    textSize(60)
    fill(255)
    text("score:",40,60)
    text(score,100,130)
    
    #ball speed lvl display
    fill(100,75,75)
    rect(260,10,250,130)
    textSize(40)
    fill(255)
    text("ball Speed:",280,60)
    text("Lvl",330,120)
    text(ballSpeedLvl,420,120)
    
    #pause/resume buttom
    fill(100,75,75)
    rect(540,10,140,130)
    textSize(30)
    fill(255)
    text("Pause",565,50)
    text("/",600,80)
    text("resume",555,115)

    #game-screen
    fill(100)
    rect(50,200,600,700)
    
    #paddle 
    fill(36, 98, 255)
    if keyPressed == True:
        controlKeyX = paddlePosition 
    else:
        if mouseX >50 and mouseX <650:
            controlKeyX = mouseX-25
        elif mouseX <50:
            controlKeyX = 50
        elif mouseX >650:
            controlKeyX = 600
    rect(controlKeyX, 800, 50, 10)
    print(controlKeyX)
    
    #control area
    fill(100,75,75)
    rect(0,900,699,100)
    fill(0)
    rect(50,940,600,20)
    fill(100)
    if mouseX >=50 and mouseX <=650:
        controlKeyX = mouseX-25
    elif mouseX <50:
        controlKeyX = 25
    elif mouseX >650:
        controlKeyX = 625
    rect(controlKeyX,920,50,60) #draw controlKey
    
def mousePressed():
    global interface
    if interface == 0:
        if mouseX >= 200 and mouseX <= 500 and mouseY >= 890 and mouseY <= 960:
            interface = 1
            
def keyPressed():
    global controlKeyX, paddlePosition
    if key == CODED:
        if keyCode == LEFT:
            paddlePosition += -10
        elif keyCode == RIGHT:
            paddlePosition += 10
        
        if paddlePosition < 50:
            paddlePosition = 50
        elif paddlePosition > 650:
            paddlePosition = 600
