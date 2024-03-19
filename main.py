from browser import document, html , window, alert
import random

def sketch(p):# This p is needed. It will be the processing sketch itself. To do things like background color, background(0) instead of p.background(0)
  def setup():
    p.createCanvas(1000, 1110)
    p.background(255, 215 )
    p.rectMode(p.CENTER)

  def draw():
    colorlist = ['red','orange','yellow','green','blue','indigo','violet']
    p.noStroke()
    p.fill(random.choice(colorlist))
    p.ellipse(p.mouseX,p.mouseY,50,50)
    
  def mousePressed(self):
    p.background(0)
  def keyPressed(self):
    if p.key=="":
      print("Aloha")
      
    p.setup = setup
  p.draw = draw
  p.mousePressed = mousePressed
  p.keyPressed = keyPressed
  
myp5 = window.p5.new(sketch)