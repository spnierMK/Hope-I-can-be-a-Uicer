import turtle  
  
def draw_圣诞老人():  
    window = turtle.Screen()  
    window.bgcolor("white")  
  
    # 绘制圣诞老人的身体  
    body = turtle.Turtle()  
    body.shape("square")  
    body.color("red")  
    body.shapesize(stretch_wid=2, stretch_len=4)  
    body.penup()  
    body.goto(-70, -30)  
    body.pendown()  
    body.forward(140)  
  
    # 绘制圣诞老人的帽子  
    hat = turtle.Turtle()  
    hat.shape("triangle")  
    hat.color("white")  
    hat.shapesize(stretch_wid=1, stretch_len=3)  
    hat.penup()  
    hat.goto(-35, 50)  
    hat.pendown()  
    hat.setheading(0)  
    for _ in range(2):  
        hat.circle(15, 180)  
        hat.circle(-15, 180)  
  
    # 绘制圣诞老人的眼睛  
    eye1 = turtle.Turtle()  
    eye1.shape("circle")  
    eye1.color("black")  
    eye1.penup()  
    eye1.goto(-15, 70)  
    eye1.pendown()  
    eye1.dot(10)  
  
    eye2 = turtle.Turtle()  
    eye2.shape("circle")  
    eye2.color("black")  
    eye2.penup()  
    eye2.goto(-45, 70)  
    eye2.pendown()  
    eye2.dot(10)  
  
    # 绘制圣诞老人的嘴巴  
    mouth = turtle.Turtle()  
    mouth.shape("square")  
    mouth.color("red")  
    mouth.shapesize(stretch_wid=1, stretch_len=2)  
    mouth.penup()  
    mouth.goto(-25, 40)  
    mouth.pendown()  
    mouth.right(90)  
    mouth.forward(20)  
    mouth.right(90)  
    mouth.forward(40)  
    mouth.right(90)  
    mouth.forward(20)  
    mouth.right(90)  
  
    turtle.done()  
  
draw_圣诞老人()  