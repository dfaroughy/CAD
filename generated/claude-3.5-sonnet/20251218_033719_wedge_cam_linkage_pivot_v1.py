# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Main dimensions
length = 28.586
width = 8.000
thickness = 1.000

# Create base plate
step1 = cq.Workplane("XY").box(length, width, thickness)

# Create raised border
border_width = 0.5
border_height = 1.0
step2 = step1.faces(">Z").workplane().rect(length-border_width, width-border_width).extrude(border_height)

# Create center divider
divider_width = 0.5
divider_height = 1.0
step3 = step2.faces(">Z").workplane().center(0,0).rect(divider_width, width-border_width).extrude(divider_height)

# Create circular cutout
circle_diameter = 3.0
step4 = step3.faces(">Z").workplane().center(length/4,0).circle(circle_diameter/2).cutThruAll()

result = step4
