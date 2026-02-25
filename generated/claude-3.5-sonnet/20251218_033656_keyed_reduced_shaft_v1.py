# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Main cylinder dimensions
length = 50.0
diameter = 24.0
wall_thickness = 2.0
inner_diameter = diameter - (2 * wall_thickness)

# Small protruding tab dimensions 
tab_width = 6.0
tab_height = 2.0
tab_depth = 2.0
tab_position = length/2

# Create main hollow cylinder
step1 = (cq.Workplane("XY")
         .circle(diameter/2)
         .extrude(length)
         .faces(">Z")
         .circle(inner_diameter/2)
         .cutThruAll())

# Add protruding tab
step2 = (step1
         .faces("side")
         .workplane()
         .center(0, 0)
         .rect(tab_width, tab_height)
         .extrude(tab_depth))

result = step2
