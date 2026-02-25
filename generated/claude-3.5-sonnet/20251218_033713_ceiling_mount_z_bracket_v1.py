# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base dimensions
LENGTH = 50.0
WIDTH = 15.0
HEIGHT = 50.0
THICKNESS = 5.0

# Create base plate
step1 = cq.Workplane("XY").box(LENGTH, WIDTH, THICKNESS)

# Create vertical post
step2 = step1.union(
    cq.Workplane("XY")
    .box(WIDTH, WIDTH, HEIGHT)
    .translate((LENGTH/2 - WIDTH/2, 0, HEIGHT/2))
)

# Create horizontal arm
step3 = step2.union(
    cq.Workplane("XY")
    .box(WIDTH, LENGTH, THICKNESS) 
    .translate((LENGTH/2 - WIDTH/2, LENGTH/2 - WIDTH/2, HEIGHT-THICKNESS/2))
)

# Add fillets to corners
step4 = step3.edges("|Z").fillet(2.0)

result = step4
