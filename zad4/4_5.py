def odwracanie(L, left, right):
    if (right + 1 - left) % 2 == 0:
        while right + 1 != left:
            temp = L[left]
            L[left] = L[right]
            L[right] = temp
            left = left + 1
            right = right - 1
    else:
        while left != right:
            temp = L[left]
            L[left] = L[right]
            L[right] = temp
            left = left + 1
            right = right - 1

fruits = ['apple', 'banana', 'cherry', 'melon', 'keks', 'jogurt', 'kanapka', 'pasztet','ogorek kiszony', 'majonez']
print(fruits)

odwracanie(fruits, 3,8)
print(fruits)
