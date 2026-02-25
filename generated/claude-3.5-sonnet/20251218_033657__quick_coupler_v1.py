# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Base dimensions
width = 40.0
height = 51.252
depth = 20.0
base_height = 35.0

# Create base rectangular body
step1 = cq.Workplane("XY").box(width, depth, base_height)

# Create cylindrical top
cylinder_dia = 20.0
cylinder_height = height - base_height
step2 = (cq.Workplane("XY")
         .transformed(offset=(0, 0, base_height/2 + cylinder_height/2))
         .cylinder(cylinder_height, cylinder_dia/2))

# Create handle arc
arc_radius = 10.0
arc_thickness = 3.0
step3 = (cq.Workplane("XY")
         .transformed(offset=(0, 0, height-2))
         .moveTo(-arc_radius, 0)
         .threePointArc((0, arc_radius), (arc_radius, 0))
         .extrude(arc_thickness))

# Create handle slot
slot_width = 2.0
slot_height = 8.0
step4 = (cq.Workplane("XY")
         .transformed(offset=(0, 0, height-slot_height/2))
         .slot2D(slot_width, slot_height)
         .extrude(arc_thickness))

# Combine all features
result = step1.union(step2).union(step3).cut(step4)
