import curses 

screen = curses.initscr() 
#curses.noecho() 
curses.curs_set(0) 
screen.keypad(1) 
curses.mousemask(1)

screen.addstr("Example\n\n") 

while True:
    event = screen.getch() 
    if event == ord("q"): 
        break 
    if event == curses.KEY_MOUSE:
        _, mx, my, _, _ = curses.getmouse()
        screen.addstr( '%d %d\n' % (mx, my) )

curses.endwin()
