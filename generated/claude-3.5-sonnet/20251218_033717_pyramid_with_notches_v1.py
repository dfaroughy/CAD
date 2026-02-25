# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Create base profile
step1 = cq.Workplane("XY").rect(50.0, 50.0)

# Extrude base
step2 = step1.extrude(25.0)

# Create diagonal cut planes
cut_angle = 45
cut_height = 25.0
cut_width = 50.0

# Cut diagonal faces
step3 = step2.cut(
    cq.Workplane("XY")
    .transformed(rotate=(0, cut_angle, 0))
    .rect(cut_width*1.5, cut_height*1.5)
    .extrude(cut_height*2)
)

step4 = step3.cut(
    cq.Workplane("XY")
    .transformed(rotate=(0, -cut_angle, 0))
    .rect(cut_width*1.5, cut_height*1.5)
    .extrude(cut_height*2)
)

result = step4
