from distress_signal import Distress

distress_signal = Distress()
# print(distress_signal)

# print(distress_signal.water_level([2,3,4], 4))
# print(distress_signal.water_level([[[]]], [[]]))
# print(distress_signal.water_level([9], [[[[8,7,6]]]]))
print(distress_signal.water_level([1,[2,[3,[4,[5,6,7]]]],8,9], [1,[2,[3,[4,[5,6,0]]]],8,9]))