# model used: meta-llama/llama-4-maverick
import cadquery as cq

# Define the dimensions
length = 80
width = 60
height = 20
circle_radius = 10
rect_width = 15
rect_length = 25

# Step 1: Create the base plate
step1 = cq.Workplane("XY").box(length, width, height)

# Step 2: Create the circle cutout
step2 = step1.faces(">Z").workplane().center(0, 0).circle(circle_radius).cutThruAll()

# Step 3: Create the rectangular cutouts
step3 = (
    step2.faces(">Z")
    .workplane()
    .center(-20, 0)
    .rect(rect_width, rect_length)
    .cutThruAll()
    .faces(">Z")
    .workplane()
    .center(20, 0)
    .rect(rect_width, rect_length)
    .cutThruAll()
)

# Assign the final geometry to 'result'
result = step3
