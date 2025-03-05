#!/usr/bin/python3
def uniq_add(my_list=[]):
    setty = set(my_list)
    n = 0
    for i in setty:
        n += i
    return n
root@4cedb538bf77:/alu-higher_level_programming/python-more_data_structures# cat 3-common_elements.py 
#!/usr/bin/python3
def common_elements(set_1, set_2):
    return set_1 & set_2
