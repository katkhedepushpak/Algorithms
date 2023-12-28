def best(max_weight, arr):
    best_values = [0 for i in range(max_weight+1)]
    count_items_back = []
    
    for i in range(len(best_values)):
        temp = []
        temp_val = []
        
        for j in arr:
            if j[0] <= i:
                temp.append(best_values[i-j[0]]+j[1])
                temp_val.append(j[1])

        if temp != []:
            temp_best = max(temp)
            best_values[i] = temp_best
            index = temp.index(temp_best)
            for i in range(len(arr)):
                if arr[i][1] == temp_val[index]:
                    count_items_back.append(i+1)
                    break
        else:
            count_items_back.append(0)
    i = max_weight
    final_count = [0] * len(arr)
    while count_items_back[i] > 0:
        final_count[count_items_back[i] - 1] += 1
        i = i - arr[count_items_back[i] - 1][0]

    return (best_values[-1], final_count)


print(best(3, [(1, 5), (1, 5)]))