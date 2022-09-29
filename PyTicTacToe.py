import time


# define our clear function
def clear():
    """ Clears the runtime screen by placing 50 newline spaces"""
    print("\n" * 50)


# Variables + Lists to keep track
visited = []
x_visited = []
o_visited = []
counter = 0
x_score = 0
o_score = 0
# Layout of table
layout_hor1 = '|-----|-----|-----|'  # [3] ,[9], [15]
layout_hor2 = '|-----|-----|-----|'
layout_hor3 = '|-----|-----|-----|'

# Menu display
print("---MENU---")
print("Choose 1-9 to mark table, press 'q' to quit")
print('This is the table!')
print(layout_hor1)
print(layout_hor2)
print(layout_hor3)

# Default number to get into while loop
operation = '1'

while operation != 'q':
    # Sets boundaries to 1-9
    while operation == '1' or operation == '2' or operation == '3' or operation == '4' or operation == '5' or operation == '6' or \
            operation == '7' or operation == '8' or operation == '9' or operation == 'q':

        # Winning conditions
        # X winning conditions
        if ('1' in x_visited and '2' in x_visited and '3' in x_visited) or \
                ('1' in x_visited and '4' in x_visited and '7' in x_visited) or \
                ('1' in x_visited and '5' in x_visited and '9' in x_visited) or \
                ('2' in x_visited and '5' in x_visited and '8' in x_visited) or \
                ('3' in x_visited and '6' in x_visited and '9' in x_visited) or \
                ('3' in x_visited and '5' in x_visited and '7' in x_visited) or \
                ('4' in x_visited and '5' in x_visited and '6' in x_visited) or \
                ('7' in x_visited and '8' in x_visited and '9' in x_visited):
            x_score += 1
            print("X player WINS!!!")
            print("X.player: {} | O.player: {}".format(x_score, o_score))
            layout_hor1 = '|-----|-----|-----|'  # [3] ,[9], [15]
            layout_hor2 = '|-----|-----|-----|'
            layout_hor3 = '|-----|-----|-----|'
            visited.clear()
            x_visited.clear()
            o_visited.clear()
            counter = 0
            print('New table!')
            print(layout_hor1)
            print(layout_hor2)
            print(layout_hor3)
            print("***End game -> press 'q'***")

        # O winning conditions
        if ('1' in o_visited and '2' in o_visited and '3' in o_visited) or \
                ('1' in o_visited and '4' in o_visited and '7' in o_visited) or \
                ('1' in o_visited and '5' in o_visited and '9' in o_visited) or \
                ('2' in o_visited and '5' in o_visited and '8' in o_visited) or \
                ('3' in o_visited and '6' in o_visited and '9' in o_visited) or \
                ('3' in o_visited and '5' in o_visited and '7' in o_visited) or \
                ('4' in o_visited and '5' in o_visited and '6' in o_visited) or \
                ('7' in o_visited and '8' in o_visited and '9' in o_visited):
            o_score += 1
            print("O player WINS!!!")
            print("X.player: {} | O.player: {}".format(x_score, o_score))
            layout_hor1 = '|-----|-----|-----|'  # [3] ,[9], [15]
            layout_hor2 = '|-----|-----|-----|'
            layout_hor3 = '|-----|-----|-----|'
            visited.clear()
            x_visited.clear()
            o_visited.clear()
            counter = 0
            print('New table!')
            print(layout_hor1)
            print(layout_hor2)
            print(layout_hor3)
            print("***End game -> press 'q'***")

        # Takes account if table is full, resets table
        if '1' in visited and '2' in visited and '3' in visited and \
                '4' in visited and '5' in visited and '6' in visited and \
                '7' in visited and '8' in visited and '9' in visited:
            print("Table is full, Try again")
            print("X.player: {} | O.player: {}".format(x_score, o_score))
            layout_hor1 = '|-----|-----|-----|'  # [3] ,[9], [15]
            layout_hor2 = '|-----|-----|-----|'
            layout_hor3 = '|-----|-----|-----|'
            visited.clear()
            x_visited.clear()
            o_visited.clear()
            counter = 0
            print('New table!')
            print(layout_hor1)
            print(layout_hor2)
            print(layout_hor3)
            print("***End game -> press 'q'***")

        # counter keeps track who's turn it is
        if counter % 2 == 1:
            operation = input("Where to put O's?")
        else:
            operation = input("Where to put X's?")
        if operation == 'q':
            break

        # Keeps track if table is already marked
        if operation not in visited and (operation == '1' or operation == '2' or operation == '3' or operation == '4' or operation == '5' or operation == '6' or \
           operation == '7' or operation == '8' or operation == '9'):
            counter += 1

            # X turn if has a remainder
            if counter % 2 == 1:
                # Choices 1-9
                # Marks the table
                if operation == '1':
                    clear()
                    layout_hor1 = layout_hor1[:3] + 'X' + layout_hor1[4:]
                    visited.append(operation)
                    x_visited.append(operation)
                    print(layout_hor1)
                    print(layout_hor2)
                    print(layout_hor3)

                elif operation == '2':
                    clear()
                    layout_hor1 = layout_hor1[:9] + 'X' + layout_hor1[10:]
                    visited.append(operation)
                    x_visited.append(operation)
                    print(layout_hor1)
                    print(layout_hor2)
                    print(layout_hor3)

                elif operation == '3':
                    clear()
                    layout_hor1 = layout_hor1[:15] + 'X' + layout_hor1[16:]
                    visited.append(operation)
                    x_visited.append(operation)
                    print(layout_hor1)
                    print(layout_hor2)
                    print(layout_hor3)

                elif operation == '4':
                    clear()
                    layout_hor2 = layout_hor2[:3] + 'X' + layout_hor2[4:]
                    visited.append(operation)
                    x_visited.append(operation)
                    print(layout_hor1)
                    print(layout_hor2)
                    print(layout_hor3)

                elif operation == '5':
                    clear()
                    layout_hor2 = layout_hor2[:9] + 'X' + layout_hor2[10:]
                    visited.append(operation)
                    x_visited.append(operation)
                    print(layout_hor1)
                    print(layout_hor2)
                    print(layout_hor3)

                elif operation == '6':
                    clear()
                    layout_hor2 = layout_hor2[:15] + 'X' + layout_hor2[16:]
                    visited.append(operation)
                    x_visited.append(operation)
                    print(layout_hor1)
                    print(layout_hor2)
                    print(layout_hor3)

                elif operation == '7':
                    clear()
                    layout_hor3 = layout_hor3[:3] + 'X' + layout_hor3[4:]
                    visited.append(operation)
                    x_visited.append(operation)
                    print(layout_hor1)
                    print(layout_hor2)
                    print(layout_hor3)

                elif operation == '8':
                    clear()
                    layout_hor3 = layout_hor3[:9] + 'X' + layout_hor3[10:]
                    visited.append(operation)
                    x_visited.append(operation)
                    print(layout_hor1)
                    print(layout_hor2)
                    print(layout_hor3)

                elif operation == '9':
                    clear()
                    layout_hor3 = layout_hor3[:15] + 'X' + layout_hor3[16:]
                    visited.append(operation)
                    x_visited.append(operation)
                    print(layout_hor1)
                    print(layout_hor2)
                    print(layout_hor3)

            # Else is for O
            else:
                # Choices 1-9
                # Marks the table
                if operation == '1':
                    clear()
                    layout_hor1 = layout_hor1[:3] + 'O' + layout_hor1[4:]
                    visited.append(operation)
                    o_visited.append(operation)
                    print(layout_hor1)
                    print(layout_hor2)
                    print(layout_hor3)

                elif operation == '2':
                    clear()
                    layout_hor1 = layout_hor1[:9] + 'O' + layout_hor1[10:]
                    visited.append(operation)
                    o_visited.append(operation)
                    print(layout_hor1)
                    print(layout_hor2)
                    print(layout_hor3)

                elif operation == '3':
                    clear()
                    layout_hor1 = layout_hor1[:15] + 'O' + layout_hor1[16:]
                    visited.append(operation)
                    o_visited.append(operation)
                    print(layout_hor1)
                    print(layout_hor2)
                    print(layout_hor3)

                elif operation == '4':
                    clear()
                    layout_hor2 = layout_hor2[:3] + 'O' + layout_hor2[4:]
                    visited.append(operation)
                    o_visited.append(operation)
                    print(layout_hor1)
                    print(layout_hor2)
                    print(layout_hor3)

                elif operation == '5':
                    clear()
                    layout_hor2 = layout_hor2[:9] + 'O' + layout_hor2[10:]
                    visited.append(operation)
                    o_visited.append(operation)
                    print(layout_hor1)
                    print(layout_hor2)
                    print(layout_hor3)

                elif operation == '6':
                    clear()
                    layout_hor2 = layout_hor2[:15] + 'O' + layout_hor2[16:]
                    visited.append(operation)
                    o_visited.append(operation)
                    print(layout_hor1)
                    print(layout_hor2)
                    print(layout_hor3)

                elif operation == '7':
                    clear()
                    layout_hor3 = layout_hor3[:3] + 'O' + layout_hor3[4:]
                    visited.append(operation)
                    o_visited.append(operation)
                    print(layout_hor1)
                    print(layout_hor2)
                    print(layout_hor3)

                elif operation == '8':
                    clear()
                    layout_hor3 = layout_hor3[:9] + 'O' + layout_hor3[10:]
                    visited.append(operation)
                    o_visited.append(operation)
                    print(layout_hor1)
                    print(layout_hor2)
                    print(layout_hor3)

                elif operation == '9':
                    clear()
                    layout_hor3 = layout_hor3[:15] + 'O' + layout_hor3[16:]
                    visited.append(operation)
                    o_visited.append(operation)
                    print(layout_hor1)
                    print(layout_hor2)
                    print(layout_hor3)

        # The result if the space wanted to be mark was already marked
        # Prompts user to try again
        else:
            print("This is already marked")

    # Result if user inputted values other than 1-9
    else:
        print("You are out of bounds, choose only 1-9")
        operation = '1'

# Runs only when user wants to leave and quit the game
count_down = 3
print("Quitting")
while count_down:
    print(count_down)
    count_down -= 1
    # sleep is borrowed from time module, delay
    time.sleep(1)
print("Game terminated")
