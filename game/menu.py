# f = open('score.txt', 'r')
# l = [line.strip() for line in f]
#
# s = l
# d = l
#
# for i in range(len(l)):
#     l[i] = int(l[i])    # 0 1 2 3 4
#     s[i] = int(s[i])    # 0 1 2 3 4
#     d[i] = int(i)       # 1 2 3 4 5
#
# l.sort(reverse=True)    # 4 3 2 1 0
#
# for i in range(len(l)):
#     for j in range(len(l)):
#         if s[j] == l[i]:
#             d[j] = j
#
# s = open('player.txt', 'r')
# h = open('topPlayer.txt', 'r')
# s = [line.strip() for line in f]
# top = ['0', '0', '0', '0', '0']
#
# for i in range(len(s)):
#     for j in range(len(s)):
#         top[j] = s[i]
#         h.write(top[j])
#
# f.close()
# s.close()
# h.close()
#


