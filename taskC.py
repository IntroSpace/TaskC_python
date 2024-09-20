t = int(input())
PULT_NUMS = "012345.6789*#"
len_pult_nums = len(PULT_NUMS)


def minimal_distance(cur_num, next_num):
    cur_index, next_index = PULT_NUMS.find(cur_num), PULT_NUMS.find(next_num)
    if next_index > cur_index:
        return min(cur_index + len_pult_nums - next_index, next_index - cur_index)
    else:
        return min(next_index + len_pult_nums - cur_index, cur_index - next_index)


def sum_of_distances_of_num(full_num):
    cur_num = "."
    result_sum = 0
    for next_num in full_num:
        result_sum += minimal_distance(cur_num, next_num) + 1
        cur_num = next_num
    return result_sum


for _ in range(t):
    print(sum_of_distances_of_num(input()))
