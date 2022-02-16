from modules import a_encrypt_cesar as ec, b_word_and_pattern as wap, c_pra_pra_pra_yandex as yandex, \
    d_run_length_encoding as rle, e_list_pow as lp, f_happy_birthday as happy_birth, g_transpose_matrix as transpose
from modules import h_callback as callback, i_cached_fib as cached_fib, j_dot_on_area as doa, k_summator_1 as summator_1
from modules import l_summator_2 as summator_2


def mod_1():
    return ec.encrypt_cesar_1()


def mod_2():
    return wap.word_and_pattern_2()


def mod_3():
    return yandex.pra_pra_pra_yandex_3()


def mod_4():
    return rle.run_length_encoding_4()


def mod_5():
    return lp.list_pow_5()


def mod_6():
    return happy_birth.happy_birhday()


def mod_7():
    return transpose.transpose_matrix()


def mod_8():
    return callback.main()


def mod_9():
    return cached_fib.main()


def mod_10():
    return doa.main()


def mod_11():
    return summator_1.main()


def mod_12():
    return summator_2.main()


if __name__ == "__main__":
    print("Введите номер задачи: ", end=" ")
    mod_num = int(input())
    if mod_num == 1:
        print(mod_1())
    elif mod_num == 2:
        print(mod_2())
    elif mod_num == 3:
        print(mod_3(), end=" ")
    elif mod_num == 4:
        print(mod_4(), end=" ")
    elif mod_num == 5:
        print(mod_5())
    elif mod_num == 6:
        print(mod_6, end=" ")
    elif mod_num == 7:
        print(mod_7())
    elif mod_num == 8:
        print(mod_8())
    elif mod_num == 9:
        print(mod_9())
    elif mod_num == 10:
        for res in mod_10():
            print(res)
    elif mod_num == 11:
        arr = mod_11()
        print(arr[0])
        print(arr[1])
    elif mod_num == 12:
        arr = mod_12()
        print(arr[0])
        print(arr[1])
        print(arr[2])
    else:
        print("Модуля под таким номером не существует!")
