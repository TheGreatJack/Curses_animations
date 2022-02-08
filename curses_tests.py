import curses
import time


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

curses.wrapper(main)
