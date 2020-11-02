
def adder(orig_list):
    max_finder = 0
    for i in orig_list:
        if isinstance(i, list):
            adder(i)
        else:
            max_finder = int(i)

    orig_list.append(max_finder+1)


tester_list = [1, 2, [3, 4, [5, 6, [7, 8, [9,10,11],10], 7, 8], 5], 3, 4]

print(tester_list)
adder(tester_list)
print(tester_list)