# model used: anthropic/claude-3.5-sonnet
import cadquery as cq

# Create hexagonal bolt
step1 = (cq.Workplane("XY")
         .polygon(6, 10.0)  # Hex head with 10mm width across flats
         .extrude(8.0))     # Head height of 8mm

# Create bolt shaft
step2 = (cq.Workplane("XY")
         .circle(5.0)       # 10mm diameter shaft
         .extrude(26.0))    # Total length 26mm

# Combine head and shaft
step3 = step1.union(step2)

result = step3
