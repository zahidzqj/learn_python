n = eval(input())
List = []
a = input()
while a != '':
    List.append(eval(a))
    a = input()
sum_up = 0
for i in List:
    if i >= n:
        sum_up += 1
if len(List) == 0:
    print('合格率为100.00%')
else:
    print('合格率为{:.2f}%'.format(100 * (sum_up / len(List))))