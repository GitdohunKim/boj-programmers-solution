def euler_phi(target_number: int) -> int:
    result = target_number
    check_number = 2

    while check_number * check_number <= target_number:
        if target_number % check_number == 0:
            while target_number % check_number == 0:
                target_number //= check_number
            result -= result // check_number
        check_number += 1

    if target_number > 1:
        result -= result // target_number

    return result


target = int(input())
print(euler_phi(target))
