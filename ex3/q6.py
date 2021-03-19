try:
    raise IOError
except IOError:
    print("IOError")

try:
    raise SystemExit
except SystemExit:
    print("SystemExit")

try:
    raise OverflowError
except OverflowError:
    print("OverflowError")

try:
    raise EOFError
except EOFError:
    print("EOFError")
