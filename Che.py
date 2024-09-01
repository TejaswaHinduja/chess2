
import pygame as py
import chess
import chengine
from chengine import GameState
WIDTH=HGHT=512
DIM=8
Sq_size=HGHT//DIM
Max_fps=15
img={}

def loadimage():
    img["wp"]=py.transform.scale(py.image.load('chesspiece/wp.png'),(Sq_size,Sq_size))
    img["wR"]=py.transform.scale(py.image.load("chesspiece/wR.png"),(Sq_size,Sq_size))
    img["wB"]=py.transform.scale(py.image.load("chesspiece/wB.png"),(Sq_size,Sq_size))
    img["wN"]=py.transform.scale(py.image.load("chesspiece/wN.png"),(Sq_size,Sq_size))
    img["wQ"]=py.transform.scale(py.image.load("chesspiece/wQ.png"),(Sq_size,Sq_size))
    img["wK"]=py.transform.scale(py.image.load("chesspiece/wK.png"),(Sq_size,Sq_size))
    img["bp"]=py.transform.scale(py.image.load("chesspiece/bp.png"),(Sq_size,Sq_size))
    img["bR"]=py.transform.scale(py.image.load("chesspiece/bR.png"),(Sq_size,Sq_size))
    img["bB"]=py.transform.scale(py.image.load("chesspiece/bB.png"),(Sq_size,Sq_size))
    img["bN"]=py.transform.scale(py.image.load("chesspiece/bN.png"),(Sq_size,Sq_size))
    img["bK"]=py.transform.scale(py.image.load("chesspiece/bK.png"),(Sq_size,Sq_size))
    img["bQ"]=py.transform.scale(py.image.load("chesspiece/bQ.png"),(Sq_size,Sq_size))


        
def main():
    py.init()
    screen = py.display.set_mode((WIDTH, HGHT))
    clock = py.time.Clock()
    screen.fill(py.Color("white"))
    gs = GameState()
    validmoves=gs.getvalidmove()
    movemade=False
    loadimage()
    running = True
    Sqselect=()
    playerclick=[]
    while running:
        for e in py.event.get():
            if e.type == py.QUIT:
                running = False
            elif e.type == py.MOUSEBUTTONDOWN:#mouse handle
                loc=py.mouse.get_pos()
                col=loc[0]// Sq_size
                row=loc[1]//Sq_size
                if Sqselect == (row,col): #user double clicked
                    Sqselect=() #deselect
                    playerclick=[]
                else:
                    Sqselect=(row,col)
                    playerclick.append(Sqselect)
                if len(playerclick) == 2:
                    move=chengine.Move(playerclick[0], playerclick[1], gs.board)
                    print(move.chessnota())
                    if move in validmoves:
                        gs.makemove(move)
                        movemade=True

                    gs.makemove(move)
                    Sqselect=()
                    playerclick=[]
            elif e.type== py.KEYDOWN:#keys handle
                if e.key==py.K_z:#z is used to undo
                    gs.undomove()
                    movemade=True
            if movemade:
                validmoves=gs.getvalidmove()
                movemade=False
               
            clock.tick(Max_fps)
            py.display.flip()
            drawGameState(screen,gs)


def drawGameState(screen,gs):
    drawboard(screen)
    drawpiece(screen, gs.board)


def drawboard(screen):
    colors=[py.Color("blue"),py.Color("light blue")]
    for r in range (DIM):
        for c in range(DIM):
            color = colors [(r+c)%2]
            py.draw.rect(screen, color, py.Rect(c*Sq_size, r*Sq_size,Sq_size, Sq_size))

def drawpiece(screen, board):
    for r in range (DIM):
        for c in range(DIM):
            piece=board[r][c]
            if piece!="--":
                screen.blit(img[piece],py.Rect(c*Sq_size, r*Sq_size,Sq_size, Sq_size))


if __name__ == main:
    main()




main()