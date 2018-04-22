def quick_sort(a_list):
    if len(a_list) < 2:
        return a_list
    lesser = quick_sort([x for x in a_list[1:] if x <= a_list[0]])
    bigger = quick_sort([x for x in a_list[1:] if x >  a_list[0]])
    return sum([lesser, [a_list[0]], bigger], [])


l = [34,2,1,34,2,53,42,15,13,46,52,23,46,11,32,51]
print (quick_sort(l))


