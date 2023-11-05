import array as arr

arr_data = arr.array('i',[12,13,14,15,16,17]) 

for i in arr_data[2::2]:
    print(i)
