import sys
import subprocess
import locale
import re
from functools import reduce

def tune():
    args = parse_args()

    passphrase = args["passphrase"]
    service = args["service"]
    version = args["version"]
    mode = args["mode"]
    length = locale.atoi(args["length"])

    print("%s(%s)[%s;%d]" % (service, version, mode, length))

    characters = parse_characters(mode)

    digits = reduce(summary, [passphrase, service, version], 0) * length

    digits_len = len("%d" % digits)
    seed = "%d%d" % (digits, digits)

    result=""
    last=""

    characters_len = len(characters)

    for i in range(0, length*10):
        seed_index = i % digits_len

        seed_number = locale.atoi(seed[seed_index:seed_index+3])
        index = (seed_number * (i+1)) % characters_len

        char = characters[index]
        if char != last:
            result = result + char
            print(".", end="")
            if len(result) == length:
                break

        last = char

    if len(result) != length:
        print("")
        print("generate error")
    else:
        print("")
        print(result)

def parse_args():
    args = " ".join(reduce(gather_arg, range(1, len(sys.argv)), [])).split(",")

    return reduce(match_arg, args, {
        "passphrase": "",
        "service": "",
        "version": "",
        "mode": "",
        "length": "0",
    })

def gather_arg(acc, index):
    acc.append(sys.argv[index])
    return acc

def match_arg(acc, arg):
    acc["passphrase"] = match(acc["passphrase"], ".*pass.*:(.*)", arg)
    acc["service"] = match(acc["service"], ".*se?rv.*:(.*)", arg)
    acc["version"] = match(acc["version"], ".*ver.*:(.*)", arg)
    acc["mode"] = match(acc["mode"], ".*mode.*:(.*)", arg)
    acc["length"] = match(acc["length"], ".*len.*:(.*)", arg)
    return acc

def match(acc, pattern, arg):
    result = re.match(pattern, arg)
    if result:
        return result.group(1).strip()
    return acc

def parse_characters(mode):
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
