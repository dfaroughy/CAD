# model used: meta-llama/llama-4-maverick
python
import cadquery as cq

# Create the base plate
step1 = cq.Workplane("XY").box(100, 100, 10)

# Create the holes
hole_positions = [(25, 25), (-25, 25), (0, -25)]
step2 = step1.faces(">Z").workplane().pushPoints(hole_positions).circle(5).cutThruAll()

# Create the notch
step3 = step2.faces(">Z").workplane().moveTo(0, -50).radiusArc((25, -50), -25).radiusArc((-25, -50), -25).close().cutThruAll()

# Add fillets to the edges
step4 = step3.edges("|Z").fillet(5)

result = step4
```
