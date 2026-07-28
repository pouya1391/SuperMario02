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


def random_location(actor):
    actor.x = random.randint(0, 1280)
    actor.y = random.randint(0, 720)


def draw():
    mod.screen.blit("back", (0, 0))
    mario.draw()
    luigi.draw()
    enemy.draw()
    coin.draw()

def update():

    # luigi section
    if keyboard.right:
        luigi.x += luigi.speed
        luigi.image = "luigi_right"
    if keyboard.left:
        luigi.x -= luigi.speed
        luigi.image = "luigi_left"
    if keyboard.down:
        luigi.y += luigi.speed
    if keyboard.up:
        luigi.y -= luigi.speed
    correct_location(luigi)

    # mario section
    if keyboard.d:
        mario.x += mario.speed
        mario.image = "mario_right"
    if keyboard.a:
        mario.x -= mario.speed
        mario.image = "mario_left"
    if keyboard.s:
        mario.y += mario.speed
    if keyboard.w:
       mario.y -= mario.speed
    correct_location(mario)

    # enemy section
    enemy.x += enemy.speed
    enemy.x += enemy.speed
    correct_location(enemy)

    # coin section
    coin.x += coin.speed
    coin.x += coin.speed
    correct_location(coin)


WIDTH = 1280
HEIGHT = 720


hwnd = pygame.display.get_wm_info()['window' ]
windll.user32.MoveWindow(hwnd, 130, 30, WIDTH, HEIGHT, False)
mod = sys. modules["__main__"]


luigi = Actor("luigi_right")
random_location(luigi)
luigi.speed = 5


mario = Actor("mario_right")
random_location(mario)
mario.speed = 6


enemy = Actor("enemy_right")
random_location(enemy)
enemy.speed = 3


coin = Actor("coin")
random_location(coin)
coin.speed = 2


pgzrun.go()