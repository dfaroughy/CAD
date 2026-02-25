# model used: anthropic/claude-3.5-sonnet
# Main body dimensions
length = 95.0
width = 20.0

# Create base cylinder
step1 = cq.Workplane("XY").circle(width/2).extrude(length)

# Create inner hole (appears to be ~1/3 of outer diameter)
step2 = step1.faces(">Z").workplane().circle(width/6).cutThruAll()

# Create slot feature near end
slot_width = width/3
slot_length = width/2
slot_depth = width/4
step3 = step2.faces(">Z").workplane(offset=-slot_depth)\
    .rect(slot_width, slot_length).cutBlind(-slot_depth)

result = step3
