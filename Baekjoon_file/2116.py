import copy
import sys
sys.setrecursionlimit(10**6)


n = int(input())
n_dice = []
total_dice = []
depth =0
summ_dice = 0
for i in range(n):
    n_dice.append(list(map(int,input().split())))

def sum_dice(idx,depth):
    global summ_dice
    # print(idx,depth)
    # print(summ_dice)
    # print(test_dice)
    if depth  >= n:
        print("yes")
        return summ_dice
    if idx == 0:
        new_idx = 5
        start_idx = test_dice[depth][idx]
        end_idx = test_dice[depth][new_idx]
        if depth +1 >= n:
            # print(depth)
            test_dice[depth].remove(start_idx)
            test_dice[depth].remove(end_idx)
            max_num = max(test_dice[depth])
            summ_dice += max_num
            return summ_dice
        target_idx = test_dice[depth+1].index(end_idx)
        # print(target_idx)
        test_dice[depth].remove(start_idx)
        test_dice[depth].remove(end_idx)
        max_num = max(test_dice[depth])
        summ_dice += max_num
        depth +=1
        # print(n_dice)
        # print(test_dice[depth].index(new_idx))
        return sum_dice(target_idx,depth)
    elif idx == 1:
        new_idx = 3
        start_idx = test_dice[depth][idx]
        end_idx = test_dice[depth][new_idx]
        if depth + 1 >= n:
            # print(depth)
            test_dice[depth].remove(start_idx)
            test_dice[depth].remove(end_idx)
            max_num = max(test_dice[depth])
            summ_dice += max_num
            return summ_dice
        target_idx = test_dice[depth+1].index(end_idx)
        test_dice[depth].remove(start_idx)
        test_dice[depth].remove(end_idx)
        max_num = max(test_dice[depth])
        summ_dice += max_num
        depth +=1

        return sum_dice(target_idx,depth)
    elif idx == 2:
        new_idx = 4
        start_idx = test_dice[depth][idx]
        end_idx = test_dice[depth][new_idx]
        if depth + 1 >= n:
            # print(depth)
            test_dice[depth].remove(start_idx)
            test_dice[depth].remove(end_idx)
            max_num = max(test_dice[depth])
            summ_dice += max_num
            return summ_dice
        target_idx = test_dice[depth+1].index(end_idx)
        test_dice[depth].remove(start_idx)
        test_dice[depth].remove(end_idx)
        max_num = max(test_dice[depth])
        summ_dice += max_num
        depth +=1

        return sum_dice(target_idx,depth)
    elif idx == 3:
        new_idx = 1
        start_idx = test_dice[depth][idx]
        end_idx = test_dice[depth][new_idx]
        if depth + 1 >= n:
            # print(depth)
            test_dice[depth].remove(start_idx)
            test_dice[depth].remove(end_idx)
            max_num = max(test_dice[depth])
            summ_dice += max_num
            return summ_dice
        target_idx = test_dice[depth+1].index(end_idx)
        test_dice[depth].remove(start_idx)
        test_dice[depth].remove(end_idx)
        max_num = max(test_dice[depth])
        summ_dice += max_num
        depth +=1

        return sum_dice(target_idx,depth)
    elif idx == 4:
        new_idx = 2
        start_idx = test_dice[depth][idx]
        end_idx = test_dice[depth][new_idx]
        if depth + 1 >= n:
            # print(depth)
            test_dice[depth].remove(start_idx)
            test_dice[depth].remove(end_idx)
            max_num = max(test_dice[depth])
            summ_dice += max_num
            return summ_dice
        target_idx = test_dice[depth+1].index(end_idx)
        test_dice[depth].remove(start_idx)
        test_dice[depth].remove(end_idx)
        max_num = max(test_dice[depth])
        summ_dice += max_num
        depth +=1

        return sum_dice(target_idx,depth)
    elif idx == 5:
        new_idx = 0
        start_idx = test_dice[depth][idx]
        end_idx = test_dice[depth][new_idx]
        if depth + 1 >= n:
            # print(depth)
            test_dice[depth].remove(start_idx)
            test_dice[depth].remove(end_idx)
            max_num = max(test_dice[depth])
            summ_dice += max_num
            return summ_dice
        target_idx = test_dice[depth+1].index(end_idx)
        test_dice[depth].remove(start_idx)
        test_dice[depth].remove(end_idx)
        max_num = max(test_dice[depth])
        summ_dice += max_num
        depth +=1

        return sum_dice(target_idx,depth)
for i in range(6):
    test_dice = copy.deepcopy(n_dice)
    depth = 0
    summ_dice = 0
    b = sum_dice(i,depth)
    total_dice.append(b)
# print(total_dice)
print(max(total_dice))