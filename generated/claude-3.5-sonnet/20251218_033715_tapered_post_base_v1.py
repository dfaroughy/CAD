# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base dimensions
width = 90.0
length = 90.0
height = 70.0
wall = 5.0

# Create base box with walls
step1 = (cq.Workplane("XY")
         .box(width, length, height)
         .faces(">Z")
         .shell(-wall)
)

# Create tapered inner cavity
step2 = (step1
         .faces(">Z")
         .workplane()
         .rect(70, 70)
         .extrude(-height+wall, taper=10)
)

# Add mounting holes in corners
step3 = (step2
         .faces("<Z")
         .workplane()
         .pushPoints([
             (width/2-10, length/2-10),
             (width/2-10, -length/2+10),
             (-width/2+10, length/2-10),
             (-width/2+10, -length/2+10)
         ])
         .hole(5)
)

# Add reinforcement ribs
step4 = (step3
         .faces(">Z")
         .workplane()
         .rect(70, wall)
         .extrude(-height/2)
)

step5 = (step4
         .faces(">Z")
         .workplane()
         .rect(wall, 70)
         .extrude(-height/2)
)

result = step5
