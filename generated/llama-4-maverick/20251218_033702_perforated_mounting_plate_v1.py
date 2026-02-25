# model used: meta-llama/llama-4-maverick
import cadquery as cq

# Create the base plate
step1 = cq.Workplane("XY").box(80, 60, 5)

# Create the pocket
step2 = step1.faces(">Z").workplane().rect(50, 30).cutBlind(-2)

# Create the fillets on the pocket
step3 = step2.faces(">Z").edges().fillet(2)

# Create the holes
step4 = step3.faces(">Z").workplane().pushPoints([(-30, -20), (30, -20), (-30, 20), (30, 20)]).circle(4).cutThruAll()

result = step4
