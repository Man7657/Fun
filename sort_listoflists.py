lists = []
N = int(input("No. of lists need to entered : "))
for i in range(N):
    element = list(map(int,input("Enter the values of list : ").split()))
    lists.append(element)
print(lists)
new_list = []
sorted_list = []

class Sorts:
    def sort_list(self,lst):
        for i in range(len(lists)):
            for j in range(len(lists[i])):
                new_list.append(lists[i][j])
        print(new_list)

        for i in range(len(new_list)):
            lowest = new_list[i]
            for j in range(i+1,len(new_list)):
                if lowest < new_list[j]:
                    pass
                else:
                    lowest, new_list[j] = new_list[j],lowest
            sorted_list.append(lowest)

        print(sorted_list)


obj = Sorts()
obj.sort_list(lists)