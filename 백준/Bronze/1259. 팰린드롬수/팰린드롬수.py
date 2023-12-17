while True:
    arr = list(map(str, input()))

    if arr == ['0']:
        break
    else:
        original_arr = arr.copy()

        arr.reverse()

        if original_arr == arr:
            print('yes')
        else:
            print('no')