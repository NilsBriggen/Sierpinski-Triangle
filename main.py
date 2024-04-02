import turtle

t = turtle.Turtle()
t.speed(0)
s = turtle.Screen()
s.tracer(False)

STARTING_LENGTH = 400
MAX_DEPTH = 6
recursions = 0
total_recs = 0


def triangle(side_length):
    for _ in range(3):
        t.forward(side_length)
        t.right(120)


def sierpinski(side_length, triangle_num, rec_num, depth=0):
    global recursions
    recursions += 1
    print(
        f"Triangle: {triangle_num}/3 | Recursions: {recursions} ({int(round((recursions/(rec_num/3))*100, 0))}%)",
        end="\r",
    )
    for _ in range(3):
        for _ in range(2):
            triangle(side_length)
            if depth < MAX_DEPTH:
                sierpinski(side_length / 2, triangle_num, rec_num, depth + 1)
            t.forward(side_length)
        t.right(120)
    if depth <= 1:
        raise Exception


HEIGHT_OFFSET = STARTING_LENGTH * 3**0.5 / 2

rec_num = 6
for i in range(MAX_DEPTH - 1):
    rec_num = rec_num * 6 - 12


def triangle1():
    global total_recs, recursions
    t.penup()
    t.setpos(-STARTING_LENGTH, HEIGHT_OFFSET)
    t.pendown()

    try:
        sierpinski(STARTING_LENGTH, 1, rec_num)
    except:
        total_recs = recursions
        recursions = 0
        pass


def triangle2():
    global total_recs, recursions
    t.penup()
    t.setpos(0, HEIGHT_OFFSET)
    t.pendown()

    try:
        print(" " * 50, end="\r")
        sierpinski(STARTING_LENGTH, 2, rec_num)
    except:
        total_recs += recursions
        recursions = 0
        pass


def triangle3():
    global total_recs, recursions
    t.penup()
    t.setpos(-STARTING_LENGTH / 2, 0)
    t.pendown()

    try:
        print(" " * 50, end="\r")
        sierpinski(STARTING_LENGTH, 3, rec_num)
    except:
        total_recs += recursions
        recursions = 0
        pass


triangle1()
triangle2()
triangle3()

print(f"\nTotal Recursions: {total_recs}")

s.update()
s.mainloop()
