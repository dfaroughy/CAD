# model used: anthropic/claude-3.5-sonnet
# Create hollow square tube with rounded corners
size = 50.0
wall_thickness = 5.0
radius = 5.0

step1 = cq.Workplane("XY").rect(size, size).extrude(size)

step2 = (cq.Workplane("XY")
         .rect(size-2*wall_thickness, size-2*wall_thickness)
         .extrude(size-wall_thickness)
         .translate((0,0,wall_thickness)))

step3 = (step1
         .edges("|Z")
         .fillet(radius)
         .cut(step2))

result = step3
