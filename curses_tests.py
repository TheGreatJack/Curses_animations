import curses
import time
import random



def main(stdscr):
    stdscr.clear()

    #window_size=str(curses.LINES - 1)+","+str(curses.COLS - 1)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    #stdscr.addstr(10,40,window_size,curses.color_pair(2))
    #stdscr.addstr(10,41,window_size,curses.color_pair(2))
    


    for col in range(curses.COLS-1):
        for line in range(curses.LINES-1):
            #stdscr.getch()
            # 
            modulo_l = line % 2
            modulo_c = col % 2
            if modulo_l == 1 and modulo_c == 1:        
                stdscr.addstr(line,col,"1",curses.color_pair(2))
                time.sleep(0.001)
            elif modulo_l == 1 and modulo_c == 0:        
                stdscr.addstr(line,col,"0",curses.color_pair(2))
                time.sleep(0.001)
            elif modulo_l == 0 and modulo_c == 1:        
                stdscr.addstr(line,col,"0",curses.color_pair(2))
                time.sleep(0.001)
            elif modulo_l == 0 and modulo_c == 0:
                stdscr.addstr(line,col,"1",curses.color_pair(2))
                time.sleep(0.001)

            stdscr.refresh()


    #stdscr.refresh()
    stdscr.getch()
    #print(curses.LINES - 1, curses.COLS - 1)

def column_updater(column,value):
    #translation of column values
    size = len(column)
    for x in range(1,size):
        column[size-x] = column[size-x-1]
    column[0] = value

def update_value(state_matrix,col,lines,empty_freq):
    is_shown = state_matrix[col][1]
    if is_shown == 1:
        value = str(random.randint(0,1))
    elif is_shown == 0:
        value = " "

    #se actualiza la matriz de status
    
    state_matrix[col][0] = state_matrix[col][0] - 1

    if state_matrix[col][0] <= 0:
        #Se cambia el satatus de forma ponderada aleatoria
        #if is_shown == 1:
        #    state_matrix[col][1] = 0
        #elif is_shown == 0:
        #    state_matrix[col][1] = 1
        state_matrix[col][1] = random.choices([0,1],[empty_freq,1-empty_freq])[0]
        state_matrix[col][0] = random.randint(0,lines//2)
    return value


def window_matrix_updater(window_matrix,state_list,cols,lines,empty_freq):
    for col in range(cols):
        value = update_value(state_list,col,lines,empty_freq)
        column_updater(window_matrix[col],value)


def main_2(stdscr):

    stdscr.clear()
    cols = curses.COLS-1
    lines = curses.LINES-1
    empty_freq = 0.2
    
    

    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

    window_matrix = [[" "]*lines for col in range(cols)]
    state_list=[[random.randint(0,lines//2),random.choice([0,1])] for col in range(cols)]



    window_matrix_updater(window_matrix,state_list,cols,lines,empty_freq)
    #for x in range(200):
    while True:
        for col in range(curses.COLS-1):
            for line in range(curses.LINES-1):
                value = window_matrix[col][line]
                stdscr.addstr(line,col,value,curses.color_pair(2))
        stdscr.refresh()
        time.sleep(0.05)    
        window_matrix_updater(window_matrix,state_list,cols,lines,empty_freq)


    #stdscr.refresh()
    stdscr.getch()    
    
curses.wrapper(main_2)
