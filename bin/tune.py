import subprocess
import locale
from functools import reduce

def tune():
    passphrase = input("passphrase : ")
    service = input("service : ")
    version = input("version : ")
    mode = input("mode : ")

    if mode == "0":
        characters="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-/:;()&@.,?!'[]{}#%^*+=_|<>$"
    else:
        if mode == "1":
            characters="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@#&*%!?@#&*%!?@#&*%!?"
        else:
            if mode == "2":
                characters="0123456789abcdefghijklmnopqrstuvwxyz"
            else:
                print("choose mode in [ 0, 1, 2 ]")
                return

    length = locale.atoi(input("length : "))

    digits = reduce(summary, [passphrase, service, version], 0) * length

    digits_len = len("%d" % digits)
    seed = "%d%d" % (digits, digits)

    result=""
    last=""

    characters_len = len(characters)

    for i in range(0, length):
        seed_index = i % digits_len

        seed_number = locale.atoi(seed[seed_index:seed_index+3])
        index = (seed_number * (i+1)) % characters_len

        char = characters[index]
        if char != last:
            result = result + char

            print(".", end="")

        last = char

    print("")
    print("password : " + result)

def characters(mode):
    if mode == "0":
        return "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-/:;()&@.,?!'[]{}#%^*+=_|<>$"

    if mode == "1":
        return "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ@#&*%!?@#&*%!?@#&*%!?"

    if mode == "2":
        return "0123456789abcdefghijklmnopqrstuvwxyz"

    print("choose mode in [ 0, 1, 2 ]")
    exit()

def summary(acc, string):
    return reduce(summary_char, string, acc)

def summary_char(acc, char):
    ps = subprocess.Popen(("echo", char), stdout=subprocess.PIPE)
    output = subprocess.check_output("cksum", stdin=ps.stdout)
    ps.wait()
    tip = output.decode("utf-8").split()[0]
    return acc + locale.atoi(tip)

tune()
