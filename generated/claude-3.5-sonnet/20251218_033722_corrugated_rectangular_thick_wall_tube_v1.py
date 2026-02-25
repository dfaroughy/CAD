# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Main dimensions
length = 100.0
width = 60.0
thickness = 5.0
inner_offset = 10.0

# Create base plate
step1 = cq.Workplane("XY").box(length, width, thickness)

# Create raised border
step2 = step1.faces(">Z").workplane().box(length, width, thickness)

# Create inner cutout with rounded corner
step3 = (step2.faces(">Z").workplane()
         .center(-length/4, -width/4)  # Offset from center
         .rect(length/2, width/2)
         .extrude(-thickness)
         .edges("|Z and <X and <Y")
         .fillet(5.0))

result = step3
