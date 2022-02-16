def __pattern_check(pattern, wrd, start, end, attr):
    vowel_ru = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
    res = []
    i = start
    while i != end:
        if pattern[i] == "1" and (wrd[i + attr] not in vowel_ru):
            res.append(wrd[i + attr])
        elif pattern[i] == "0" and (wrd[i + attr] in vowel_ru):
            res.append(wrd[i + attr])
        elif pattern[i] == "?":
            res.append(wrd[i + attr])
        else:
            pass
        i += 1
    return res


def word_and_pattern_2():
    pattern = input()
    vowel_ru = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
    error_text = "Нет результата!"
    result = []
    result_word = []
    dif_len = 0
    delta = 0
    ind = 0

    while True:
        word = str(input())
        if len(word) == 0:
            break
        elif len(word) - len(pattern) < -1:
            continue
        else:
            if "*" in pattern:
                if pattern[len(pattern) - 1] != "*":
                    while ind != (pattern.index("*")) + 1:
                        if pattern[ind] == "1" and word[ind] not in vowel_ru:
                            result_word.append(word[ind])
                        elif pattern[ind] == "0" and word[ind] in vowel_ru:
                            result_word.append(word[ind])
                        elif pattern[ind] == "?":
                            result_word.append(word[ind])
                        else:
                            dif_len = len(word) - len(pattern)
                            if dif_len == 0:
                                delta = 0
                                result_word.append(word[ind])
                                break
                            elif dif_len > 0:
                                result_word.append(word[ind:(ind + dif_len + 1)])
                                delta = 1
                                break
                            else:
                                delta = -1
                                break
                        ind += 1

                    if delta == 0:
                        result_word = __pattern_check(
                            pattern, word, ind, len(pattern), 0)
                    elif delta == -1:
                        result_word = __pattern_check(
                            pattern, word, ind, len(pattern), -1)
                    else:
                        result_word.append(
                            ''.join(__pattern_check(pattern, word, ind + 1, len(pattern), dif_len)))

                    ind = 0
                else:
                    result_word = __pattern_check(pattern, word, 0, len(pattern) - 1, 0)
                    ind = len(pattern) - 1
                    while ind != len(word):
                        result_word.append(word[ind])
                        ind += 1
                    ind = 0
            else:
                if len(word) == len(pattern):
                    result_word = __pattern_check(pattern, word, 0, len(pattern), 0)
                else:
                    continue

            if ''.join(result_word) == word:
                result.append(''.join(result_word))
            result_word.clear()

    if len(result) != 0:
        for word in result:
            return word
    else:
        return error_text
