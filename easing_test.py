import easing


for number in range(1 ,1000):
    ease_factor = easing.easeInCirc(number, 1, 1, 1000) - 1
    ease_pos = 90 * ease_factor
    print(ease_pos)
