
def find_chksum(iccid):
    """Find checksum by Luhn algorithm"""
    even = []
    x = 0
    for i in iccid:
        x += 1                      # Итератор
        if x % 2 == 0:              # Берем четные числа
            dub = str(int(i) * 2)   # Умножаем четное на 2
            if len(dub) > 1:        # Если число двухзначное
                a = int(dub[0])
                b = int(dub[1])
                even.append(a + b)
            else:                   # Если однозначное
                a = int(dub[0])
                b = 0
                even.append(a + b)
        else:
            even.append(int(i))

    sum = 0                         # Сумма всех чисел
    for e in even:
        sum = sum + e

    chk_sum = str(sum * 9)[-1]      # Контрольная сумма
    result = int(iccid + chk_sum)
    print(result)

    return result


file = open('iccid.csv', 'r')
all_iccid = []
for i in file:
    all_iccid.append(i[:18])
file.close()

out_file = open('out_file.csv', 'w')
out_file.write('iccid')
out_file.close()
for i in all_iccid:
    out_file_full = open('out_file.csv', 'a')
    out_file_full.write('\n{}'.format(find_chksum(i)))
    out_file_full.close()
