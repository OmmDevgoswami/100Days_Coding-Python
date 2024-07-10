#Hurdle_4 : 
# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
def turn_right():
    turn_left();  #built-in functions of the site
    turn_left();  #built-in functions of the site
    turn_left();  #built-in functions of the site
    
def jump():
    turn_left();
    while wall_on_right() == True:  #built-in functions of the site
        move();    #built-in functions of the site
    turn_right();
    move();        #built-in functions of the site
    turn_right();
    while front_is_clear() == True:  #built-in functions of the site
        move();    #built-in functions of the site
    turn_left();   #built-in functions of the site

while at_goal() != True:    #built-in functions of the site
    if front_is_clear() == True:    #built-in functions of the site
        move();    #built-in functions of the site
    elif wall_in_front() == True:   #built-in functions of the site
        jump();
        
        
#Maze:
#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
def turn_right():
    turn_left();  #built-in functions of the site
    turn_left();  #built-in functions of the site
    turn_left();  #built-in functions of the site

while at_goal() != True:    #built-in functions of the site
    if front_is_clear() == True:    #built-in functions of the site
        move();   #built-in functions of the site
    elif right_is_clear() == True:  #built-in functions of the site
        turn_right();   
        move();   #built-in functions of the site
    else:
        turn_left();        #built-in functions of the site