g_arr = [10,20,40,60,30,25,55,45,50]
target = 70


def pair_of_elements(i_arr):
    for i in range(len(i_arr)):
        for j in range(i+1,len(i_arr)):
            if i_arr[i] + i_arr[j] == target:
                print((i,j),end=",")
            else:
                pass

pair_of_elements((g_arr))