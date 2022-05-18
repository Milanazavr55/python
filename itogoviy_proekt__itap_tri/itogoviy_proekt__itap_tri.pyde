import time
x = 150
y = -5
d = 0
def setup ():
    size (500, 500)
    global d
    d = loadImage ("dino.png")
def draw ():
    global x, y, d
    background (255)
    noStroke()
    push ()
    fill (0)
    rect (0, 0, 150, 500)
    rect (150, 80, 100, 150)
    rect (250, 80, 100, 200)
    rect (450, 0, 100, 500)
    rect (250, 380, 500, 150)
    # push()
    # fill (255)
    # stroke (139, 0, 255)
    # strokeWeight (5)
    # rect (170, 180, 200, 100)
    # pop()
    pop ()
    push ()
    fill (142, 210, 255)
    pop ()
    push ()
    fill (255, 0, 0)
    rect (150, 480, 100, 10)
    pop ()
    image (d, x, y, 80, 90)
    frameRate (130)
    if keyPressed == True:
        if key == CODED: 
            if keyCode == UP:
                y = y - 1
            if keyCode == DOWN:
                y = y + 1 
            if keyCode == LEFT:
                x = x - 1
            if keyCode == RIGHT:
                x = x + 1
    if y >= 490:
        y = 5
        x = 150
    
    if x + 45 >= 0 and y < -20 and y + 90 >= 0 and y <= 150:
        x = 150
        y = 5
    if y + 45 >= 55 and y < 215 and x + 80 >= 150 and x <= 250:
        x = 150
        y = 5
    if y + 45 >= 55 and y < 265 and x + 80 >= 250 and x <= 350:
        x = 150
        y = 5
    if y + 45 >= 0 and y < 500 and x + 80 >= 460 and x <= 550:
        x = 150
        y = 5
    if y + 45 >= 0 and y < 500 and x + 80 >= 0 and x <= 140:
        x = 150
        y = 5
    if y + 45 >= 350 and y < 530 and x + 80 >= 250 and x <= 750:
        x = 150
        y = 5
    if y + 45 >= 460 and y < 490 and x + 150 and x <= 250:
        background (255)
        x = 150
        y = 5
        fill (255)
        stroke (139, 0, 255)
        strokeWeight (5)
        rect (170, 180, 200, 100)
        fill (255, 0, 0)
        textSize (20)
        text (u"Победа!", 250, 250)
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # if x > 175 and x < 275 and y > 105 and y < 255:
    #     x = 150
    #     y = 5
    # if x > 275 and x < 375 and y > 105 and y < 305:
    #     x = 150
    #     y = 5
    # if x > 475 and x < 575 and y > 25 and y < 525:
    #     x = 150
    #     y = 5
    # if x > 275 and x < 775 and y > 405 and y < 455:
    #     x = 150
    #     y = 5
        
        
        
        
    #         if x > 25 and x < 175 and y > 25 and y < 525:
    #     x = 150
    #     y = 5
    # if x > 180 and x < 280 and y > 70 and y < 230:
    #     x = 150
    #     y = 5
    # if x > 290 and x < 380 and y > 80 and y < 300:
    #     x = 150
    #     y = 5
    # if x > 425 and x < 550 and y > 0 and y < 500:
    #     x = 150
    #     y = 5
    # if x > 230 and x < 750 and y > 360 and y < 530:
    #     x = 150
    #     y = 5
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
