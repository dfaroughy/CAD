# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Create U-channel profile
step1 = (cq.Workplane("XY")
         .rect(6.0, 20.0)
         .extrude(1.0)
         .faces(">Z")
         .shell(-1.0)
)

# Create the full length by extruding
result = step1.translate((0,0,0))
