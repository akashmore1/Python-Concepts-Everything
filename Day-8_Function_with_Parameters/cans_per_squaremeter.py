def paint_calc(height, width, cover):
    area = height * width
    if area % cover == 0:
        num_cans = int(area / cover)
    else:
        num_cans = int(area / cover) + 1
    print(f"You'll need {num_cans} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
