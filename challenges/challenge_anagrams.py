def merge_sort(letters):
    if len(letters) <= 1:
        return letters

    mid = len(letters) // 2
    left = letters[:mid]
    right = letters[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result


def is_anagram(first_string, second_string):
    if not first_string and not second_string:
        return ('', '', False)

    def sorted_string(s):
        return "".join(merge_sort(list(s.lower())))

    sorted_str1 = sorted_string(first_string)
    sorted_str2 = sorted_string(second_string)

    return (sorted_str1, sorted_str2, sorted_str1 == sorted_str2)
