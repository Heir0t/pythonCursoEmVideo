import pygame

#Desafio 21 - Faça um programa em python que abra e reproduza um audio de um arquivo mp3
pygame.mixer.init()
pygame.mixer.music.load('Mundo1/Aula08/heyYa.mp3')
pygame.mixer.music.play()

#Com o compilador certo (pycharm). a música ira tocar