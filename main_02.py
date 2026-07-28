import pgzrun
import random
import pygame.display
import sys
from ctypes import windll
from pgzero.actor import Actor
from pgzero.keyboard import keyboard

def random_location(actor):
    actor.x = random.randint(0, 1280)
    actor.y = random.randint(0, 720)

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
    mod.screen.blit("back", (0, 0))
    mario.draw()
    luigi.draw()
    enemy.draw()
    coin.draw()

def update():
    # luigi section
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
    correct_location(luigi)
    # mario section
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
    correct_location(mario)

WIDTH = 1280
HEIGHT = 720

hwnd = pygame.display.get_wm_info()['window' ]
windll.user32.MoveWindow(hwnd, 130, 30, WIDTH, HEIGHT, False)
mod = sys . modules["main"]

luigi = Actor("luigi_right")
random_location(luigi)

mario = Actor("mario_right")
random_location(mario)


enemy = Actor("enemy_right")
random_location(enemy)

coin = Actor("coin")
random_location(coin)

pgzrun.go()