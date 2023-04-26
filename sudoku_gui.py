import pygame, sys

import sudoku_generator
from constants import *
from sudoku_generator import Board

def draw_game_easy(screen):  # creates the main menu that shows first
    #title font
    easy_title_font = pygame.font.Font(None, 80)
    button_font = pygame.font.Font(None, 70)

    #bg
    mainImage = pygame.image.load("sudokumenu.jpg")
    mainImage = pygame.transform.scale(mainImage, (600,675))
    screen.blit(mainImage, (0, 0))

    #init and draw title
    title_surface = easy_title_font.render("Welcome to Sudoku", 0, BLACK)
    title_rectangle = title_surface.get_rect(
        center = (WIDTH // 2, HEIGHT // 2 - 150))
    screen.blit(title_surface, title_rectangle)

    #init and draw game mode
    game_font = pygame.font.Font(None, 75)
    game_mode = game_font.render("Select Game Mode:", 0, BLACK)
    game_rectangle = game_mode.get_rect(
        center=(WIDTH - 300, HEIGHT - 150))
    screen.blit(game_mode, game_rectangle)

    #buttons
    #text first
    easy_text = button_font.render("Easy", 0 ,(255,255,255))
    medium_text = button_font.render("Medium", 0, (255,255,255))
    hard_text = button_font.render("Hard", 0 , (255,255,255))

    #button bg color & text
    # this is for the easy button
    easy_surface = pygame.Surface((easy_text.get_size()[0] + 20,
                                    easy_text.get_size()[1] + 20))
    easy_surface.fill(LINE_COLOR)
    easy_surface.blit(easy_text,(10,10))

    #  this is for the medium difficulty button
    medium_surface = pygame.Surface((medium_text.get_size()[0] + 20,
                                   medium_text.get_size()[1] + 20))
    medium_surface.fill(LINE_COLOR)
    medium_surface.blit(medium_text,(10,10))

    #  this is for the hard difficulty button
    hard_surface = pygame.Surface((hard_text.get_size()[0] + 20,
                                   hard_text.get_size()[1] + 20))
    hard_surface.fill(LINE_COLOR)
    hard_surface.blit(hard_text, (10, 10))

    #init button rect
    easy_rect = easy_surface.get_rect(
        center = (WIDTH // 2-200, HEIGHT //2 + 250))
    medium_rect = medium_surface.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 250))
    hard_rect = hard_surface.get_rect(
        center = (WIDTH // 2 + 200, HEIGHT // 2 +250))

    # Draw buttons
    screen.blit(easy_surface, easy_rect)
    screen.blit(medium_surface, medium_rect)
    screen.blit(hard_surface,hard_rect)

    #button funct
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_rect.collidepoint(event.pos):
                    #pick difficulty
                    return 30 # If the mouse is
                elif medium_rect.collidepoint(event.pos):
                    return 40
                elif hard_rect.collidepoint(event.pos):
                    return 50

        pygame.display.update()

    #game over screen
def draw_game_over(screen):
    #  Creates the screen for the Game Over/ Win screen
    game_over_font = pygame.font.Font(None, 80)
    mainImage = pygame.image.load("sudokumenu.jpg")  # this is the background image we use
    mainImage = pygame.transform.scale(mainImage, (600, 675))
    screen.blit(mainImage, (0, 0))
    if winner == 1:
        text = 'Game Won!'
    else:
        text = "Game Over :("

    #same logic as easy screen
    game_over_surf = game_over_font.render(text, 0, BLACK)
    game_over_rect = game_over_surf.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 - 100))
    screen.blit(game_over_surf, game_over_rect)
    # Restart button
    game_over_font = pygame.font.Font(None, 40)
    restart_text = game_over_font.render("Restart", 0, (BLACK))
    restart_surf = pygame.Surface((restart_text.get_size()[0] + 20,
                                   restart_text.get_size()[1] + 20))
    restart_rect = restart_surf.get_rect(
        center=(WIDTH // 2 - 200, HEIGHT // 2 + 350))
    restart_surf.fill(LINE_COLOR)
    restart_surf.blit(restart_text, (10, 10))
    screen.blit(restart_surf, restart_rect)


    # Added key to return to main menu
    # Exit button
    exit_text = game_over_font.render("Exit", 0, (BLACK))
    exit_surf = pygame.Surface((exit_text.get_size()[0] + 20,
                                exit_text.get_size()[1] + 20))
    exit_rect = exit_surf.get_rect(
        center=(WIDTH // 2 + 200, HEIGHT // 2 + 350))
    exit_surf.fill(LINE_COLOR)
    exit_surf.blit(exit_text, (10, 10))
    screen.blit(exit_surf, exit_rect)

    if event.type == pygame.MOUSEBUTTONDOWN:  # gathers where the mouse clicks on the screen to prompt the next action
        # only restart and exit because once the game is over, either exit or start a new game
        if exit_rect.collidepoint(event.pos):  # if the mouse clicks in the exit button, exits the game
            pygame.quit()
            sys.exit()
        elif restart_rect.collidepoint(event.pos):  # of the user clicks in the restart button
            draw_game_easy(screen)  # takes the user back to the main menu
            screen.fill(WHITE)
            board = Board(WIDTH, HEIGHT, screen, difficulty)
            board.draw()  #starts running through the function again and prompting the sudoku grid
            screen.blit(restart_surf, restart_rect)
            screen.blit(reset_surf, reset_rect)
            screen.blit(exit_surf, exit_rect)
    pygame.display.update()  # updates the display


if __name__ == '__main__':
    #starting variables
    game_over = False
    winner = False

    #init screen
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, GAME_HEIGHT))
    pygame.display.set_caption("Sudoku")

    #display start until button is clicked
    difficulty = draw_game_easy(screen)  # Calls function to draw easy screen

    #
    screen.fill(WHITE)
    board = Board(WIDTH, HEIGHT, screen, difficulty)
    board.draw()
    game_over_font = pygame.font.Font(None, 40)
    # Restart button with the rectangle
    restart_text = game_over_font.render("Restart", 0, (BLACK))
    restart_surf = pygame.Surface((restart_text.get_size()[0] + 20,
                                   restart_text.get_size()[1] + 20))
    restart_rect = restart_surf.get_rect(
        center=(WIDTH // 2 - 200, HEIGHT // 2 + 350))
    restart_surf.fill(LINE_COLOR)
    restart_surf.blit(restart_text, (10, 10))
    screen.blit(restart_surf, restart_rect)

    # reset button with the rectangle
    reset_text = game_over_font.render("Reset", 0, (BLACK))
    reset_surf = pygame.Surface((reset_text.get_size()[0] + 20,
                                 reset_text.get_size()[1] + 20))
    reset_rect = reset_surf.get_rect(
        center=(WIDTH // 2, HEIGHT // 2 + 350))
    reset_surf.fill(LINE_COLOR)
    reset_surf.blit(reset_text, (10, 10))
    screen.blit(reset_surf, reset_rect)

    # exit button with the rectangle
    exit_text = game_over_font.render("Exit", 0, (BLACK))
    exit_surf = pygame.Surface((exit_text.get_size()[0] + 20,
                                exit_text.get_size()[1] + 20))
    exit_rect = exit_surf.get_rect(
        center=(WIDTH // 2 + 200, HEIGHT // 2 + 350))
    exit_surf.fill(LINE_COLOR)
    exit_surf.blit(exit_text, (10, 10))
    screen.blit(exit_surf, exit_rect)
    pygame.display.flip()

    num = -1
    #  starts to run the program and go based on the users clicks
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                if reset_rect.collidepoint(event.pos):  # when the user clicks the reset button
                    board.reset_to_original()   # resets the sudoku grid to the beginning with the pre-filled numbers
                    board.draw()
                    screen.blit(restart_surf, restart_rect)
                    screen.blit(reset_surf, reset_rect)
                    screen.blit(exit_surf, exit_rect)
                    continue  # to continue playing
                elif exit_rect.collidepoint(event.pos):  # when the user clicks the exit button
                    pygame.quit()  # similar to the game over screen, exits the game
                    sys.exit()
                elif restart_rect.collidepoint(event.pos):   # when the user clicks on the restart button
                    draw_game_easy(screen)   # takes the user back to the maun menu
                    screen.fill(WHITE)  # similar to the restart button in teh game over screen
                    difficulty = draw_game_easy(screen)
                    board = Board(WIDTH, HEIGHT, screen, difficulty)
                    board.draw()
                    screen.blit(restart_surf, restart_rect)
                    screen.blit(reset_surf, reset_rect)
                    screen.blit(exit_surf, exit_rect)
                    continue  # continues to run through the game

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:  # this starts to gather what the user click in
                # in the grid and is going to place the number the user wants
                clicked_row = int(event.pos[1] / SQUARE_SIZE)
                clicked_col = int(event.pos[0] / SQUARE_SIZE)
                board.selected_row = clicked_row  # assigns the clicked row ro the board class
                board.selected_col = clicked_col
                board.cells[clicked_row][clicked_col].row = clicked_row  # assigns the new row and col to the cells
                # so that it can put it in the cells parameter
                board.cells[clicked_row][clicked_col].col = clicked_col

                # print(clicked_row, clicked_col)

                # coords is supposed to take x,y of pos and print the row and col that is selected
                #you can use these print functions to test if it works
            if event.type == pygame.KEYDOWN:  # this gathers the key that is pushed by the user

                if event.key == pygame.K_1:
                    num = 1
                    print("kdhb")
                    print(board.cells[clicked_row][clicked_col].set_cell_value(num))

                    board.draw()  # prints the number the user inputs on the new board
                    screen.blit(restart_surf, restart_rect)
                    screen.blit(reset_surf, reset_rect)
                    screen.blit(exit_surf, exit_rect)

                if event.key == pygame.K_2:
                    num = 2
                    board.cells[clicked_row][clicked_col].set_cell_value(num)
                    board.draw()   # prints the number the user inputs on the new board
                    screen.blit(restart_surf, restart_rect)
                    screen.blit(reset_surf, reset_rect)
                    screen.blit(exit_surf, exit_rect)

                if event.key == pygame.K_3:
                    num = 3

                    board.cells[clicked_row][clicked_col].set_cell_value(num)
                    board.draw()   # prints the number the user inputs on the new board
                    screen.blit(restart_surf, restart_rect)
                    screen.blit(reset_surf, reset_rect)
                    screen.blit(exit_surf, exit_rect)

                if event.key == pygame.K_4:
                    num = 4

                    board.cells[clicked_row][clicked_col].set_cell_value(num)
                    board.draw()  # prints the number the user inputs on the new board
                    screen.blit(restart_surf, restart_rect)
                    screen.blit(reset_surf, reset_rect)
                    screen.blit(exit_surf, exit_rect)

                if event.key == pygame.K_5:
                    num = 5

                    board.cells[clicked_row][clicked_col].set_cell_value(num)
                    board.draw()   # prints the number the user inputs on the new board
                    screen.blit(restart_surf, restart_rect)
                    screen.blit(reset_surf, reset_rect)
                    screen.blit(exit_surf, exit_rect)

                if event.key == pygame.K_6:
                    num = 6

                    board.cells[clicked_row][clicked_col].set_cell_value(num)
                    board.draw()   # prints the number the user inputs on the new board
                    screen.blit(restart_surf, restart_rect)
                    screen.blit(reset_surf, reset_rect)
                    screen.blit(exit_surf, exit_rect)

                if event.key == pygame.K_7:
                    num = 7

                    board.cells[clicked_row][clicked_col].set_cell_value(num)
                    board.draw()   # prints the number the user inputs on the new board
                    screen.blit(restart_surf, restart_rect)
                    screen.blit(reset_surf, reset_rect)
                    screen.blit(exit_surf, exit_rect)

                if event.key == pygame.K_8:
                    num = 8

                    board.cells[clicked_row][clicked_col].set_cell_value(num)
                    board.draw()   # prints the number the user inputs on the new board
                    screen.blit(restart_surf, restart_rect)
                    screen.blit(reset_surf, reset_rect)
                    screen.blit(exit_surf, exit_rect)

                if event.key == pygame.K_9:
                    num = 9

                    board.cells[clicked_row][clicked_col].set_cell_value(num)
                    board.draw()   # prints the number the user inputs on the new board
                    screen.blit(restart_surf, restart_rect)
                    screen.blit(reset_surf, reset_rect)
                    screen.blit(exit_surf, exit_rect)

                if event.key == pygame.K_RETURN and num <= 9:  # with the return key press it locks the number the user
                    # inputs in the position
                    board.place_number(num)


                if board.is_full() == True:  # everytime this checks to see if the board is full
                    if board.check_board() == True:  # if true then it will check if the board is correct it will
                        # update as True
                        winner = 1
                        game_over = True
                    else:   # if not, it will return True but will also include that the winner is 0
                        winner = 0
                        game_over = True
                if game_over == True:
                    pygame.display.update()
                    pygame.time.delay(1000)  # delays the screen to pop up
                    draw_game_over(screen)   # will draw game over screen according to the winner number
                    continue

            pygame.display.update()  # updates the display

