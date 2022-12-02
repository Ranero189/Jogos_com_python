import turtle
import winsound

wn = turtle.Screen()
wn.title("PingPong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Pontuação

pontuação_j1 = 0
pontuação_j2 = 0

# Jogador 1

jogador1 = turtle.Turtle()
jogador1.speed(0)
jogador1.shape("square")
jogador1.color("white")
jogador1.shapesize(stretch_wid=5, stretch_len=1)
jogador1.penup()
jogador1.goto(-350, 0)

# Jogador 2

jogador2 = turtle.Turtle()
jogador2.speed(0)
jogador2.shape("square")
jogador2.color("white")
jogador2.shapesize(stretch_wid=5, stretch_len=1)
jogador2.penup()
jogador2.goto(350, 0)

# Bola

bola = turtle.Turtle()
bola.speed(0)
bola.shape("square")
bola.color("white")
bola.shapesize(stretch_wid=1, stretch_len=1)
bola.penup()
bola.goto(0, 0)
bola.dx = 0.02
bola.dy = 0.02

# Placar

placar = turtle.Turtle()
placar.speed(0)
placar.color("white")
placar.hideturtle()
placar.penup()
placar.goto(0, 260)
placar.write("Jogador 1: 0 jogador 2: 0", align="center", font=("Courier", 24, "normal"))

# Funções

def pedal_1_Subir():
    y = jogador1.ycor()
    y += 20
    jogador1.sety(y)

def pedal_1_Decer():
    y = jogador1.ycor()
    y -= 20
    jogador1.sety(y)

def pedal_2_Subir():
    y = jogador2.ycor()
    y += 20
    jogador2.sety(y)

def pedal_2_Decer():
    y = jogador2.ycor()
    y -= 20
    jogador2.sety(y)

# Comandos Teclado

wn.listen()
wn.onkeypress(pedal_1_Subir, "w")
wn.onkeypress(pedal_1_Decer, "s")
wn.onkeypress(pedal_2_Subir, "8")
wn.onkeypress(pedal_2_Decer, "5")



# Loop principal

while True:
    wn.update()

    # Movendo a bola

    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    # Controle de tela

    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if bola.xcor() > 390:
        bola.goto(0,0)
        bola.dx *= -1
        pontuação_j1 += 1
        placar.clear()
        placar.write(f"Jogador 1: {pontuação_j1} jogador 2: {pontuação_j2}", align="center", font=("Courier", 24, "normal"))
        bola.dx = 0.02   

    if bola.xcor() < -390:
        bola.goto(0,0)
        bola.dx *= -1
        pontuação_j2 += 1
        placar.clear()
        placar.write(f"Jogador 1: {pontuação_j1} jogador 2: {pontuação_j2}", align="center", font=("Courier", 24, "normal"))
        bola.dx = 0.02

    # Colisão

    if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < jogador2.ycor() + 40 and bola.ycor() > jogador2.ycor() - 40):
        bola.setx(340)
        bola.dx *= -1
        bola.dx += -0.02
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < jogador1.ycor() + 40 and bola.ycor() > jogador1.ycor() - 40):
        bola.setx(-340)
        bola.dx *= -1
        bola.dx += 0.02
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
