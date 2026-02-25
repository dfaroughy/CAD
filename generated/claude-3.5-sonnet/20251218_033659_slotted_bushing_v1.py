# model used: anthropic/claude-3.5-sonnet
# Create cylindrical base
step1 = cq.Workplane("XY").circle(30/2).extrude(20)

# Create inner hole
step2 = step1.faces(">Z").workplane().circle(20/2).cutThruAll()

# Create slots
slot_width = 4
slot_depth = 5
slots = []
for angle in [0, 90, 180, 270]:
    slot = (cq.Workplane("XY")
            .transformed(rotate=(0,0,angle))
            .center(25/2,0)
            .rect(slot_width, slot_depth)
            .extrude(20))
    slots.append(slot)

# Cut slots from base
step3 = step1
for slot in slots:
    step3 = step3.cut(slot)

result = step3
