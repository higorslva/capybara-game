import pygame #Biblioteca pygame
import time   #Para reiniciar o jogo
import random #Para deixar os inimigos aleatórios
pygame.init() 
#Cores em RGB
gray=(60,60,60)
black=(255,0,0) 
display=pygame.display.set_mode((830,600)) #Tamanho da janela
pygame.display.set_caption("Capivara game (i)Ltda") #Nome da janela
capyimg=pygame.image.load("./sprites/capivara.png") #Carrega sprite da capivara
backgroundleft=pygame.image.load("./sprites/left.png") #Sprite do lado direito
backgroundright=pygame.image.load("./sprites/right.png") #Sprite do lado esquerdo
capy_width=23 #Tamanho da capivara

#define as funções do inimigo que vem do lado oposto(inimigo_f)
def enemy_f(enemy_startx,enemy_starty,enemy):
    if enemy==0:
        enemy_come=pygame.image.load("./sprites/jacare.png") 
    if enemy==1: 
        enemy_come=pygame.image.load("./sprites/cobra.png")
    if enemy==2:
        enemy_come=pygame.image.load("./sprites/nave.png") 
    display.blit(enemy_come,(enemy_startx,enemy_starty))

def background():
    display.blit(backgroundleft,(0,0)) #Define a posição da imagem de fundo do lado direito nos eixos x e y
    display.blit(backgroundright,(700,0)) #Define a posição da imagem de fundo do lado esquerdo nos eixos x e y

#Função que imprime a mensagem caso o player perca
def crash():       
    message_display("YOU DIED")

#Função para customizar o estilo do texto imprimido em "crash()"
def message_display(text):
    large_text=pygame.font.Font("freesansbold.ttf",80) #Estilo da fonte e tamanho do texto
    textsurf,textrect=text_object(text,large_text) #Função para editar a mensagem
    textrect.center=((400),(300)) #Posição da mensagem no jogo
    display.blit(textsurf,textrect) #Mostra a mensagem
    pygame.display.update()
    time.sleep(3) #Após o jogador morrer, aguardar 3 segundos para reiniciar
    loop() #Chamada da função "loop()" para reiniciar o jogo

def text_object(text,font): #Função que mostrará a mensagem após o jogador perder
    text_surface=font.render(text,True,black)
    return text_surface,text_surface.get_rect()  
#Função que gera a capivara
def capybara(x,y): 
    #Posição do protagonista
    display.blit(capyimg,(x,y))

#Todas as funções serão chamadas por esta função
def loop():
    x=400 #Define a posição x da capivara
    y=540 #Define a posição y da capivara

    x_change=0
    y_change=0

    enemy_f_speed=9 #Define a velocidade dos inimigos caindo

    enemy=0 #definir estágio inicial para o inimigo
    enemy_startx=random.randrange(130,(700-capy_width)) #Para os inimigos aparecerem aleatoriamente
    enemy_starty=-600 #Inimigos virão com eixo y em negativo pois estão vindo do lado oposto
    # Define o tamanho dos inimigos
    enemy_width=23
    enemy_height=47
    #Se o jogo não possuir nenhum problema ao executar
    bumped=False
    #Inicia o jogo
    while not bumped: 
        #Define o input do jogo
        for event in pygame.event.get():   
            #Se o input de saída é dado ao jogo
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

            #Definindo as setas do teclado como controle
            if event.type==pygame.KEYDOWN: 
                #Se o usuário pressionar a seta esquerda
                if event.key==pygame.K_LEFT:
                    #A capivara moverá no eixo x em -2 
                    x_change=-2
                    #Se o usuário pressionar a seta direita
                if event.key==pygame.K_RIGHT: 
                    #A capivara moverá no eixo x em 2
                    x_change=2
            #Se nenhuma tecla for presionada o player permanecerá parado
            if event.type==pygame.KEYUP:   
                x_change=0
        x+=x_change
        #Define a cor do background
        display.fill(gray) 
        background()
        enemy_starty-=(enemy_f_speed/1.1) #Velocidade do carro vindo do outro lado
        enemy_f(enemy_startx,enemy_starty,enemy) 
        #Inimigo aumenta a velocidade lentamente
        enemy_starty+=enemy_f_speed         
        capybara(x,y) #se o carro sair do alcance(parede lateral do jogo)
        if x<130 or x>700-capy_width:

            crash()
        #Define quão longe os inimigos irão
        if enemy_starty>600:
            #Só um inimigo irá cair de uma vez
            enemy_starty=0-enemy_height 
            #Outros inimigos irão vir
            enemy_startx=random.randrange(130,(1000-300)) 
            #Define quantos inimigos virão
            enemy=random.randrange(0,3)   
        if y<enemy_starty+enemy_height:
            if x > enemy_startx and x < enemy_startx + enemy_width or x + capy_width > enemy_startx and x + capy_width < enemy_startx + enemy_width :
                crash()   
        #reinicia o jogo
        pygame.display.update() 
loop() # sai do jogo
pygame.quit() 
quit()