def binary(n, isZeor, binaArr=[], num=''):
    if(isZeor):
        num += binaArr[0]
    else:
        num += binaArr[1]
    if(len(num) == n):
        memo.append(num)
        num = ''
        return
    binary(n, True,  binaArr, num)
    binary(n, False, binaArr, num)

with open('input.txt', 'r') as inp:
    with open('output.txt', 'w') as out:
        var = inp.read()
        n = int(var[:])
        inp.close()
        memo = []
        binary(n, True, ['0', '1'], '')
        binary(n, True, ['1', '0'], '')
        out.write(str( len(memo)))
        out.write("\n")
        for i in range(len(memo)):
            out.write(memo[i])
            out.write("\n")
    out.close()
inp.close()
