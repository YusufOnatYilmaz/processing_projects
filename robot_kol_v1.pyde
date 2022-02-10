from Arm import Segment

#parameters
base_lenght = 70
gripper_lenght = 50
long_segment_lenght = 160
short_segment_lenght = base_lenght
short_segments_angle = radians(0)
gripper_angle = 0
big_elipse_w_h = 2*(gripper_lenght +long_segment_lenght + short_segment_lenght)
small_elipse_w_h = 2*sqrt(pow(long_segment_lenght,2) + pow(short_segment_lenght+gripper_lenght,2))

def setup():
    global fixed_base,seg2,seg3,gripper,seg4,seg5,seg6,seg7
    size(800, 800)
    fixed_base = Segment(height/2, width/2, base_lenght ,radians(-90), r=0, g=0, b=0)
    seg2 = Segment(100, 100, long_segment_lenght, radians(90), parent= fixed_base, r=255, g=0, b=0)
    seg3 = Segment(100, 100, short_segment_lenght, short_segments_angle, parent= seg2, r=0, g=255, b=0, full_free=True)
    gripper = Segment(100, 100, gripper_lenght, gripper_angle, parent= seg3, r=0, g=0, b=255,full_free=True, gripper=True)

    
def draw():
    background(200, 200, 40)
    ellipseMode(CENTER)
    ellipse(width/2, (height/2) - base_lenght, big_elipse_w_h, big_elipse_w_h) # BU CAP UNUTMA
    ellipse(width/2, (height/2) - base_lenght, small_elipse_w_h, small_elipse_w_h)
    fixed_base.show()
    seg2.show()
    seg3.show()
    gripper.show()
    seg2.update()
    seg3.update()
    gripper.update()
    
