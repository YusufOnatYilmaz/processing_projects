from Segment import Short,Long

message = "12   1   2    3   4   5   6   7   8   9  10 11 "
r = 200

def setup():
    global f, akrep, yelkovan, ghost
    size(800, 800)
    f = createFont("Georgia",80,True)
    textFont(f)
    # The text must be centered!
    textAlign(CENTER)
    smooth()
    akrep = Short(width/2,height/2,60,radians(-90), 0.001)
    ghost = Short(width/2,height/2, 170,radians(-90), 0.012)
    yelkovan = Long(akrep, ghost)

def draw():
    global r, f, akrep, yelkovan, ghost
    background(255)
    akrep.show()
    akrep.update()
    ghost.update()
    yelkovan.show()
    #yelkovan.update()
    # Start in the center and draw the circle
    translate(width / 2, height / 2)
    noFill()
    stroke(0)
    ellipse(0, 0, r*2, r*2)

    # We must keep track of our position along the curve
    arclength = 270

    # For every box
    for i in xrange(len(message)):

        # Instead of a constant width, we check the width of each character.
        currentChar = message[i]
        w = textWidth(currentChar)

        # Each box is centered so we move half the width
        arclength += w/2
        # Angle in radians is the arclength divided by the radius
        # Starting on the left side of the circle by adding PI
        theta = PI + arclength / r   

        pushMatrix();
        # Polar to cartesian coordinate conversion
        translate(r*cos(theta), r*sin(theta))
        # Rotate the box
        rotate(theta+PI/2)   # rotation is offset by 90 degrees
        # Display the character
        fill(0)
        text(currentChar,0,0)
        popMatrix()
        # Move halfway again
        arclength += w/2 
