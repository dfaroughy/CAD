# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Create hexagonal nut
step1 = (cq.Workplane("XY")
         .polygon(6, 17.32)  # Hexagon with 17.32 diameter
         .extrude(3.0))      # Extrude 3mm

# Create center hole
step2 = (step1
         .faces(">Z")
         .workplane()
         .hole(10))  # 10mm diameter hole

result = step2
