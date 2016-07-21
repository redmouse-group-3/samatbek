def power(*args):
    print(args[0])
    i = 1
    while i < len(args):
        print ("%d" % args[i] ** args[i - 1])
        i += 1

power(1, 2, 3, 4)
