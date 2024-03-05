import turtle

sc  = turtle.Screen()
dr  = turtle.Turtle()
XO = 'X'
ninesquare = ['_', '_', '_', '_', '_', '_', '_', '_', '_',]

def draw_grid():
    dr.penup()
    dr.goto(-150,50)
    dr.pendown()
    dr.goto(150,50)
    
    dr.penup()
    dr.goto(-150,-50)
    dr.pendown()
    dr.goto(150,-50)
    
    dr.penup()
    dr.goto(50,-150)
    dr.pendown()
    dr.goto(50,150)
    
    dr.penup()
    dr.goto(-50,-150)
    dr.pendown()
    dr.goto(-50,150)

def switch():
    
    global XO
    
    if XO == 'X':
        XO = 'O'
    else:
        XO = 'X'

def det_mouse(x,y):
    dr.penup()
    dr.goto(x,y)
    dr.pendown
    
    if -150 < x < -50 and 50 < y < 150:
        if ninesquare[0] == '_':
            dr.write(XO, font=("TimesNewRoman", 32))
            ninesquare[0] = XO
            check_win()
            switch()
            
    elif -50 < x < 50 and 50 < y < 150:
        if ninesquare[1] == '_':
            dr.write(XO, font=("TimesNewRoman", 32))
            ninesquare[1] = XO
            check_win()
            switch()
            
    elif 50 < x < 150 and 50 < y < 150:
        if ninesquare[2] == '_':
            dr.write(XO, font=("TimesNewRoman", 32))
            ninesquare[2] = XO
            check_win()
            switch()
            
    elif -150 < x < -50 and -50 < y < 50:
        if ninesquare[3] == '_':
            dr.write(XO, font=("TimesNewRoman", 32))
            ninesquare[3] = XO
            check_win()
            switch()
            
    elif -50 < x < 50 and -50 < y < 50:
        if ninesquare[4] == '_':
            dr.write(XO, font=("TimesNewRoman", 32))
            ninesquare[4] = XO
            check_win()
            switch()
            
    elif 50 < x < 150 and -50 < y < 50:
        if ninesquare[5] == '_':
            dr.write(XO, font=("TimesNewRoman", 32))
            ninesquare[5] = XO
            check_win()
            switch()
            
    elif -150 < x < -50 and -150 < y < -50:
        if ninesquare[6] == '_':
            dr.write(XO, font=("TimesNewRoman", 32))
            ninesquare[6] = XO
            check_win()
            switch()
            
    elif -50 < x < 50 and -150 < y < -50:
        if ninesquare[7] == '_':
            dr.write(XO, font=("TimesNewRoman", 32))
            ninesquare[7] = XO
            check_win()
            switch()
            
    elif 50 < x < 150 and -150 < y < -50:
        if ninesquare[8] == '_':
            dr.write(XO, font=("TimesNewRoman", 32))
            ninesquare[8] = XO
            check_win()
            switch()

def check_win():
    #side to side
    if ninesquare[0] == ninesquare[1] == ninesquare[2] != '_':
        win(ninesquare[0])
    elif ninesquare[3] == ninesquare[4] == ninesquare[5] != '_':
        win(ninesquare[3])
    elif ninesquare[6] == ninesquare[7] == ninesquare[8] != '_':
        win(ninesquare[6])
    
    #up and down
    elif ninesquare[0] == ninesquare[3] == ninesquare[6] != '_':
        win(ninesquare[0])
    elif ninesquare[1] == ninesquare[4] == ninesquare[7] != '_':
        win(ninesquare[1])
    elif ninesquare[2] == ninesquare[5] == ninesquare[8] != '_':
        win(ninesquare[2])
    
    #diagnol
    elif ninesquare[0] == ninesquare[4] == ninesquare[8] != '_':
        win(ninesquare[0])
    elif ninesquare[2] == ninesquare[4] == ninesquare[6] != '_':
        win(ninesquare[2])
    
    
    

def win(x):
    dr.penup()
    dr.goto(0, -300)
    dr.write(x +  " wins!", font=('Arial', 32))
    
dr.speed(100)
draw_grid()
sc.onclick(det_mouse)
sc.mainloop()
