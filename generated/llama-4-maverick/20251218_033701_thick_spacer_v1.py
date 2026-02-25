# model used: meta-llama/llama-4-maverick
import cadquery as cq

# Create the base cylinder
step1 = cq.Workplane("XY").circle(20).extrude(15)

# Create the inner hole
step2 = step1.faces(">Z").workplane().circle(10).cutThruAll()

# Create the notches
notch = cq.Workplane("XY").rect(5, 2).extrude(15)
notches = (
    cq.Workplane("XY")
    .polarArray(20, 0, 360, 4)
    .each(lambda loc: notch.val().moved(loc))
)
step3 = step2.cut(notches)

# Add fillets to the edges
step4 = step3.edges("|Z").fillet(1)

result = step4
