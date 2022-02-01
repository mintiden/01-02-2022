import turtle, random
krasas = ["red", "magenta", "purple",]
Rafael = turtle.Turtle()
Rafael.speed(0)
Rafael.shape("turtle")
Rafael.color("magenta")

for i in range(0,12):
  Rafael.circle(100)
  Rafael.circle(100,steps=4)
  Rafael.circle(100,steps=3)
  Rafael.right(30)
  Rafael.color(random.choice(krasas))