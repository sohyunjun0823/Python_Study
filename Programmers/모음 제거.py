def solution(my_string):
    m = ['a', 'e', 'i', 'o', 'u']
    for item in m:
        my_string = my_string.replace(item, '')
        
    return my_string
