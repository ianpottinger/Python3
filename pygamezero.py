import math
import random
import pygame
from pygame import mixer
#import pgzrun

pygame.init()
background = pygame.image.load("G:\WorkingData\Work @ Home\Humanity\oneMcolours.png")
WIDTH = background.get_width()
HEIGHT = background.get_height()
frame = 0


screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption("PyGame screen")

icon = pygame.image.load("G:\WorkingData\Work @ Home\Humanity\My Icon.png")
pygame.display.set_icon(icon)

# Background muisic
mixer.music.load("G:\WorkingData\My Music\Portable\Soul Divas\VideoGames.mp3")
mixer.music.play(-1)

# DaFont.com
score_font = pygame.font.Font("freesansbold.ttf", 32)
scoreX = 32
scoreY = 32

# Ready player
playerIMG = pygame.image.load("G:\WorkingData\Work @ Home\Humanity\Dodecahedron.gif")
playerX = random.randint(0, WIDTH)
playerY = random.randint(0, HEIGHT)
playerWidth = playerIMG.get_width()
playerHeight = playerIMG.get_height()
playerXcentre = playerWidth // 2
playerYcentre = playerHeight // 2
playerXstep = 2
playerYstep = 2
playerXrate = 0
playerYrate = 0
playerScore = 0

# Ready opponent
opponentImages = ['Tetrahedron.gif', 'Octahedron.gif', 'Icosahedron.gif', 'Hexahedron.gif']
opponentIMG = []
opponentX = []
opponentY = []
opponentWidth = []
opponentHeight = []
opponentXcentre = []
opponentYcentre = []
opponentXstep = []
opponentYstep = []
opponentXrate = []
opponentYrate = []
opponentScore = []
opponentXhitbox = []
opponentYhitbox = []
player_opponent = []
opponent_observer = []
opponents = 3

for opponent in range(opponents):
    opponentIMG.append(pygame.image.load(f"G:\WorkingData\Work @ Home\Humanity\{opponentImages[opponent]}"))
    opponentX.append(random.randint(0, WIDTH))
    opponentY.append(random.randint(0, HEIGHT))
    opponentWidth.append(opponentIMG[opponent].get_width())
    opponentHeight.append(opponentIMG[opponent].get_height())
    opponentXcentre.append(opponentWidth[opponent] // 2)
    opponentYcentre.append(opponentHeight[opponent] // 2)
    opponentXstep.append(1)
    opponentYstep.append(1)
    opponentXrate.append(1)
    opponentYrate.append(1)
    opponentXhitbox.append(0)
    opponentYhitbox.append(0)
    opponentScore.append(0)
    player_opponent.append(False)
    opponent_observer.append(False)


# Ready observer
observerIMG = pygame.image.load("G:\WorkingData\Work @ Home\Humanity\GoldenRatioHorus.png")
observerX = -1
observerY = -1
observerWidth = observerIMG.get_width()
observerHeight = observerIMG.get_height()
observerXcentre = observerWidth // 2
observerYcentre = observerHeight // 2
observerXstep = 3
observerYstep = 3
observerXrate = 1
observerYrate = 1
oldobserverXrate = observerXrate
oldobserverYrate = observerYrate
observerwatching = False
observerScore = 0


def collision(object1X, object1Y, object2X, object2Y):
    distance = math.sqrt(
        math.pow( (object2X - object1X), 2) +
        math.pow( (object2Y - object1Y), 2)
        )
    return distance < 200

    
game_loop = True
while game_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
            pygame.quit()

        # Detect key pressed state
        if event.type == pygame.KEYDOWN:
            print (f"Key pressed at frame: {frame}")
            if event.key == pygame.K_LEFT:
                playerXrate = -1.1
                print (f"Moving LEFT: {playerX}") 
            elif event.key == pygame.K_RIGHT:
                playerXrate = 1.1
                print (f"Moving RIGHT: {playerX}")
            if event.key == pygame.K_UP:
                playerYrate = -1.1
                print (f"Moving UP: {playerY}") 
            elif event.key == pygame.K_DOWN:
                playerYrate = 1.1
                print (f"Moving DOWN: {playerY}")
            if event.key == pygame.K_RCTRL:
                if observerwatching == True:
                    observerwatching = False
                    observerX = -1
                    observerY = -1
                    oldobserverXrate = observerXrate
                    oldobserverYrate = observerYrate
                    observerXrate = 0
                    observerYrate = 0
                elif observerwatching == False:
                    observerwatching = True
                    observerX = random.randint(0, WIDTH)
                    observerY = random.randint(0, HEIGHT)
                    observerXrate = oldobserverXrate
                    observerYrate = oldobserverYrate
                print (f"observernwatching: {observerwatching}, {observerXrate}, {observerYrate}")

        # Detect key released state
        if event.type == pygame.KEYUP:
            print (f"Key released at frame: {frame}")
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerYrate = 0
                print (f"Holding vertical: {playerY}") 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXrate = 0
                print (f"Holding horizontal: {playerX}")

            
    # Random fill background
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    #screen.fill( (red, green, blue) )

    # Random circles
    circleX = random.randint(0, WIDTH)
    circleY = random.randint(0, HEIGHT)
    circleSize = random.randint(0, (playerWidth + playerHeight))
    #pygame.draw.circle(screen, (red, green, blue), (circleX, circleY), circleSize)

    # Background
    if (frame % 1) == 0:
        screen.blit(background, (0, 0) )

    # Object collision detection
    playerXhitbox = playerX + playerXcentre
    playerYhitbox = playerY + playerYcentre
    
    for opponent in range(opponents):
        opponentXhitbox[opponent] = opponentX[opponent] + opponentXcentre[opponent]
        opponentYhitbox[opponent] = opponentY[opponent] + opponentYcentre[opponent]
    
    observerXhitbox = observerX + observerXcentre
    observerYhitbox = observerY + observerYcentre
        
    for opponent in range(opponents):
        player_opponent[opponent] = collision(playerXhitbox, playerYhitbox, opponentXhitbox[opponent], opponentYhitbox[opponent])
        
    for opponent in range(opponents):
        opponent_observer[opponent] = collision(opponentXhitbox[opponent], opponentYhitbox[opponent], observerXhitbox, observerYhitbox)
        
    observer_player = collision(observerXhitbox, observerYhitbox, playerXhitbox, playerYhitbox)
    #for opponent in range(opponents):
    #    print (player_opponent[opponent], opponent_observer[opponent])
    #print (observer_player)

    # Object scoring
    for opponent in range(opponents):
        if player_opponent[opponent]:
            playerScore += 1
            opponentScore[opponent] -= 1
            opponentX[opponent] = random.randint(0, WIDTH)
            opponentY[opponent] = random.randint(0, HEIGHT)
            #print (playerScore, opponentScore, observerScore)

    for opponent in range(opponents):
        if opponent_observer[opponent]:
            opponentScore[opponent] += 1
            observerScore += 1
            opponentX[opponent] = random.randint(0, WIDTH)
            opponentY[opponent] = random.randint(0, HEIGHT)
            #print (playerScore, opponentScore, observerScore)
        
    if observerwatching == True:
        if observer_player:
            playerScore -= 1
            observerScore += 1
            observerX = random.randint(0, WIDTH)
            observerY = random.randint(0, HEIGHT)
            #respawn = mixer.Sound("G:\WorkingData\My Music\Portable\Skits\Reloaded.mp3")
            #respawn.play()
            #print (playerScore, opponentScore, observerScore)
    
    # Set opponent position
    for opponent in range(opponents):
        opponentX[opponent] += opponentXstep[opponent] * opponentXrate[opponent]
        opponentY[opponent] += opponentYstep[opponent] * opponentYrate[opponent]
        # Restrict opponent position within boundaries
        if opponentX[opponent] < 0:
            opponentXrate[opponent] = 0.9
        elif opponentX[opponent] > WIDTH - opponentWidth[opponent]:
            opponentXrate[opponent] = -0.9
        if opponentY[opponent] < 0:
            opponentYrate[opponent] = 0.9
        elif opponentY[opponent] > HEIGHT - opponentHeight[opponent]:
            opponentYrate[opponent] = -0.9
        # Display opponent state
        screen.blit(opponentIMG[opponent], (opponentX[opponent], opponentY[opponent]) )

    # Set observer position
    if observerwatching:
        observerX += observerXstep * observerXrate
        observerY += observerYstep * observerYrate
        # Restrict observer position within boundaries
        if observerX < 0:
            observerXrate = 1
        elif observerX > WIDTH - observerWidth:
            observerXrate = -1
        if observerY < 0:
            observerYrate = 1
        elif observerY > HEIGHT - observerHeight:
            observerYrate = -1
        # Display observer state
        if observerwatching == True:
            screen.blit(observerIMG, (observerX, observerY) )

    # Set player position
    playerX += playerXstep * playerXrate
    playerY += playerYstep * playerYrate
    # Restrict player position within boundaries
    if playerX < 0:
        playerX = 0
    elif playerX > WIDTH - playerWidth:
        playerX = WIDTH - playerWidth
    if playerY < 0:
        playerY = 0
    elif playerY > HEIGHT - playerHeight:
        playerY = HEIGHT - playerHeight
    # Display player state
    screen.blit(playerIMG, (playerX, playerY) )

    # Update score board
    scores = f"Player: {playerScore}, Opponents: {opponentScore}, Observer: {observerScore}"
    score_board = score_font.render(scores, True, (255, 255, 255))
    screen.blit(score_board, (scoreX, scoreY) )    

    # Update positions
    positions = f"Player: {playerX}:{playerY}, Observer: {observerX}:{observerY}"
    positions_board = score_font.render(positions, True, (255, 255, 255))
    screen.blit(positions_board, (scoreX, scoreY * 2) )    

    # Update canvas
    pygame.display.update()
    frame += 1
            

