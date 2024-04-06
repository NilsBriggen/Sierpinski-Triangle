import turtle
from random import randint

## USER SETTINGS ##
UPDATE_WHILE_RENDERING = False # Increased rendering time, but looks more interesting
SCALE = 300 # Actual side length is 2*SCALE
ACCURACY = 10000 # Number of dots to draw
ACC_MULT = 10 # Number of times to draw ACCURACY dots, progress bar uses this value to update
###################

## DEV SETTINGS ##
C1_POS = (-SCALE, SCALE * 3**0.5 / 2)
C2_POS = (SCALE, SCALE * 3**0.5 / 2)
C3_POS = (0, -SCALE * 3**0.5 / 2)
###################

s = turtle.Screen()
s.tracer(False)
t = turtle.Turtle()

def setupScreen():
    t.penup()
    t.setpos(C3_POS)
    t.pendown()
    t.goto(C1_POS)
    t.goto(C2_POS)
    t.goto(C3_POS)
    t.penup()
    t.hideturtle()
    t.setpos(0, 0)

def main():
    for i in range(ACC_MULT):
        for _ in range(ACCURACY):
            rand_corner = randint(1, 3)
            if rand_corner == 1:
                t.goto((t.xcor() + C1_POS[0]) / 2, (t.ycor() + C1_POS[1]) / 2)
            elif rand_corner == 2:
                t.goto((t.xcor() + C2_POS[0]) / 2, (t.ycor() + C2_POS[1]) / 2)
            else:
                t.goto((t.xcor() + C3_POS[0]) / 2, (t.ycor() + C3_POS[1]) / 2)
            t.dot(2)
        print(f"Rendering progress: {round((i/ACC_MULT)*100, 2)+10}%", end="\r")
        if UPDATE_WHILE_RENDERING:
            s.update()
    print("Rendering complete!"+" "*50+"\nUpdating the screen may take a few seconds!")    

setupScreen()
main()
s.mainloop()