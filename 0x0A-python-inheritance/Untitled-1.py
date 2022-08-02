class MyList(list):
    def print_sorted(self):
        print(sorted(self))


const = MyList()
const.append(1)
const.append(2)
const.append(0)
const.append(11)
const.append(3)
print(const)
const.print_sorted()
print()
