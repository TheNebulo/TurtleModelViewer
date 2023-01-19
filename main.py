import math, time, obj_interp
from turtle import Turtle

t = Turtle()
t.speed(0)
t.hideturtle()
t.color("white")
screen = t.getscreen()
screen.tracer(0, 0)
screen.bgcolor((0.05, 0.05, 0.1))

verts = obj_interp.read_verts("teapot.obj") # used to get the vertices of the model
faces = obj_interp.read_faces("teapot.obj") # used to get face indexes of the model


# Rotation Stuff
def rotateX(VERTS, theta):  #rotates entire vertex array
    sinTheata = math.sin(theta)
    cosTheata = math.cos(theta)
    for a in range(len(VERTS)):
        y = VERTS[a][1]
        z = VERTS[a][2]
        VERTS[a][1] = y * cosTheata - z * sinTheata
        VERTS[a][2] = z * cosTheata + y * sinTheata


def rotateY(VERTS, theta):  #rotates entire vertex array
    sinTheata = math.sin(theta)
    cosTheata = math.cos(theta)
    for a in range(len(VERTS)):
        x = VERTS[a][0]
        z = VERTS[a][2]
        VERTS[a][0] = x * cosTheata + z * sinTheata
        VERTS[a][2] = z * cosTheata - x * sinTheata

def rotateZ(VERTS, theta):  #rotates entire vertex array
    sinTheata = math.sin(theta)
    cosTheata = math.cos(theta)
    for a in range(len(VERTS)):
        x = VERTS[a][0]
        y = VERTS[a][1]
        VERTS[a][0] = x * cosTheata - y * sinTheata
        VERTS[a][1] = y * cosTheata + x * sinTheata


#Math function thing, google it
def sigmoid(x, mi, mx):
    return mi + (mx - mi) * (lambda t:
                             (1 + 200**(-t + 0.5))**(-1))((x - mi) / (mx - mi))

# Rendering functions
def wire(POS, VERTS, FACES):
    t.penup()

    for FACE in range(len(FACES)):
        for targ_vert in range(len(FACES[FACE])):
            t.goto(VERTS[FACES[FACE][targ_vert] - 1][0] + POS[0],
                   VERTS[FACES[FACE][targ_vert] - 1][1] + POS[1])
            t.pendown()
        t.penup()


def face(POS, VERTS, FACES): # Renders filled faces
    face_colors = get_order(VERTS, FACES) # Refer to function below
    t.penup()
    for FACE in range(len(FACES)): # For every face in the FACES input
        # Get the index of the current face in the colors array
        indx = face_colors[FACE]["indx"]

        # Goto the first vert of this face to begin fill
        t.goto(VERTS[FACES[indx][0] - 1][0] + POS[0],
               VERTS[FACES[indx][0] - 1][1] + POS[1])
        t.begin_fill()
        for targ_vert in range(1, len(FACES[indx])): # For every vert after the first
            # Goto the vert
            t.goto(
                VERTS[FACES[indx][targ_vert] - 1][0] + POS[0],
                VERTS[FACES[indx][targ_vert] - 1][1] + POS[1])
        c = face_colors[FACE]["avg"] # get the shading of this face
        t.color((c, c, c)) # set it
        t.end_fill() # end fill, finished drawing this face

def point(POS, VERTS, _):
    t.penup() # so we dont make any random lines
    for VERT in range(len(VERTS)): # For every vertex from VERT
        t.goto(VERTS[VERT][0] + POS[0], VERTS[VERT][1] + POS[1]) # goto it
        t.dot() # place a dot

def sort_func(e):  # for face ordering
    return e["avg"] # order faces by the "avg" part of the dictionary

def get_order(VERTS, FACES): # This is for properly drawing the faces in order
    face_colors = [] # Create an empty array
    for FACE in range(len(FACES)): # For every face in FACES
        #To calculate the color of this face, we average its Z values together
        face_avg = 0 
        face_avg += VERTS[FACES[FACE][0] - 1][2] # Add the first vertex Z value
        t.begin_fill()
        for targ_vert in range(1, len(FACES[FACE])): # For the rest of the vertices
            face_avg += VERTS[FACES[FACE][targ_vert] - 1][2] # add to the average

        # We use a sigmoid to squish the average between 0.0 -> 1.0
        face_col = sigmoid((face_avg / len(FACES[FACE])+550), 1, 1000) * 0.001

        # Add the face color, as well as the face index to the face_colors array
        face_colors.append({"avg" : face_col, "indx" : FACE})

    # Sort the face_colors array by the color of the faces
    # the reasoning for this is so we can draw the faces in the correct order
    # basically a bodged together depth buffer
    face_colors.sort(key=sort_func)
    return face_colors # All done!


time_passed = 0
last_time = time.time()
deltaTime = 0.1 
# Delta time is the time between frames, by multiplying values by it
# we can keep a constant change between framerates
# for example, if the project lags for 2 seconds, deltaTime will equal 2
# so if you were rotating by 1 unit every frame multiplied by delta time
# it would now be 2 units. (Dumbed down example but you get the idea)



offset = [-3.0, -47.0] # used for offsetting the model

def func(i, j):
    global offset
    offset = [i, j]
screen.onclick(func) # Bind the click function

while True:
    rotateX(verts, 0.1 * deltaTime) # Rotate the vertices, fun!
    rotateY(verts, 0.5 * deltaTime) # More rotating!
    rotateZ(verts, 0.02 * deltaTime) # MORE!!

    #If you want to use the other rendering modes, just swap the below function
    #Or if you would like, add more rendering passes
    if(time_passed < 2):
      point(offset, verts, faces)
    elif(time_passed < 4):
      wire(offset, verts, faces)
    elif(time_passed < 6):
      face(offset, verts, faces)
    else:
      time_passed = 0
      t.color("white")
  
    #face(offset, verts, faces)

    # why screen.update? if you look at line 9, you will see
    # screen.tracer(0,0) this makes it so the results of the turtles
    # drawings will only display on screen.update(), this is really
    # useful as you wont see frames halfway drawn, and it speeds up drawing ALOT
    screen.update() 

    t.clear() # we should prep for the next frame, 
              #this clear wont be seen till screen.update() is called again
  
    cur_time = time.time()
    deltaTime = cur_time - last_time
    last_time = cur_time
    time_passed += deltaTime
    #time.sleep(0.03333) #30 FPS limit if you would like