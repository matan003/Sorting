import draw_information

def selection_sort(draw_info, ascending=True):
    lst = draw_info.lst
    for i in range(len(lst)):
        min_unsorted_lst = lst[i]
        min_index = i
        for j in range(i, len(lst)):
            if(lst[j] < min_unsorted_lst and ascending) or (lst[j] > min_unsorted_lst and not ascending):
                min_unsorted_lst = lst[j]
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
        draw_info.draw_list({min_index: draw_info.GREEN, i: draw_info.RED}, True)
        yield True

    return lst
