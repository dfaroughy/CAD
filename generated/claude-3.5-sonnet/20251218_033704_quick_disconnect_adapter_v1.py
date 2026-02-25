# model used: anthropic/claude-3.5-sonnet
# Base dimensions
width = 30.0
height = 20.0
depth = 20.0
wall = 2.0

# Create base hexagonal prism
step1 = (
    cq.Workplane("XY")
    .polygon(6, width/2)
    .extrude(depth)
)

# Hollow out interior
step2 = (
    step1
    .faces(">Z")
    .workplane()
    .polygon(6, (width/2)-wall)
    .cutThruAll()
)

# Add mounting tab
step3 = (
    step2
    .faces(">Z")
    .workplane()
    .center(0, height/2)
    .rect(width/3, wall)
    .extrude(wall)
)

# Add mounting hole
step4 = (
    step3 
    .faces(">Z")
    .workplane()
    .center(0, height/2)
    .hole(4)
)

# Add curved handle
step5 = (
    step4
    .faces(">Z")
    .workplane()
    .center(0, -height/4)
    .circle(width/2)
    .sweep(
        cq.Workplane("YZ")
        .center(0, depth/2)
        .threePointArc((width/4, depth/2 + width/4), (width/2, depth/2))
        .line(0, -wall)
        .threePointArc((width/4, depth/2 + width/4 - wall), (0, depth/2))
        .close()
    )
)

result = step5
