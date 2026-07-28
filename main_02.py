import pgzrun
import random
import pygame.display
import sys
from ctypes import windll
from pgzero.actor import Actor
from pgzero.keyboard import keyboard


def correct_location(actor):
    if actor.x > WIDTH + actor.width//2:
        actor.x = -actor.width//2
    if actor.x < -actor.width//2:
        actor.x = WIDTH + actor.width//2
    if actor.y > HEIGHT + actor.height//2:
        actor.y = -actor.height//2
    if actor.y < -actor.height//2:
        actor.y = HEIGHT + actor.height//2

def draw():
    screen.blit("back", (0, 0))
    mario.draw()
    luigi.draw()
    enemy.draw()
    coin.draw()

def update():
    if keyboard.right:
        luigi.x += 5
        luigi.image = "luigi_right"
    if keyboard.left:
        luigi.x -= 5
        luigi.image = "luigi_left"
    if keyboard.down:
        luigi.y += 5
    if keyboard.up:
        luigi.y -= 5
    
    if keyboard.d:
        mario.x += 5
        mario.image = "mario_right"
    if keyboard.a:
        mario.x -= 5
        mario.image = "mario_left"
    if keyboard.s:
        mario.y += 5
    if keyboard.w:
       mario.y -= 5

WIDTH = 1280
HEIGHT = 720

luigi = Actor("luigi_right")
luigi .x = 600
luigi .y = 200

mario = Actor("mario_right")
mario.x = random.randint(0, 1280)
mario.x = random.randint(0, 720)
mario.x = 300
mario.y = 200


enemy = Actor("enemy_right")
enemy.x = 700
enemy.y = 300

coin = Actor("coin")
coin.x = 700
coin.y = 400

pgzrun.go()