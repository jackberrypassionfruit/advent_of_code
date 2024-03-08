from distress_signal import Distress

distress_signal = Distress()
# print(distress_signal)

print(distress_signal.order_check([ "[[8,[[7]]]]", "[[[[8],2]]]" ])) # should be Correct
# distress_signal.order_check_all()