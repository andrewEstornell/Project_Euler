import itertools as itr


def is_valid(n):
    return int(n[1:4]) % 2 == 0 and int(n[2:5]) % 3 == 0 and int(n[3:6]) % 5 == 0 and int(n[4:7]) % 7 == 0 \
       and int(n[5:8]) % 11 == 0 and int(n[6:9]) % 13 == 0 and int(n[7:10]) % 17 == 0


perms = itr.permutations([i for i in range(10)], 10)
perms = [''.join([str(i) for i in perm]) for perm in perms]
perms = filter(is_valid, perms)
print(sum(map(int, perms)))




