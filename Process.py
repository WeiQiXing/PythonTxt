# -*- coding: utf-8 -*-
class PCB(object):  # 定义一个进程控制块类
    def __init__(self, name, need, turn):
        self.name = name
        self.need = need
        self.turn = turn


clock = 0
Finish = []  # 最后的输出队列
p = PCB('P', 0, 0)
p1 = PCB('P1', 16, 6)
p2 = PCB('P2', 11, 5)
p3 = PCB('P3', 14, 4)
p4 = PCB('P4', 13, 3)
p5 = PCB('P5', 15, 2)
RQ1 = [p1, p2, p3, p4, p5]  # 添加进程到队列RQ1中
p6 = PCB('P6', 21, 1)
p7 = PCB('P7', 18, 2)
p8 = PCB('P8', 10, 3)
p9 = PCB('P9', 7, 4)
p10 = PCB('P10', 14, 5)
RQ2 = [p6, p7, p8, p9, p10]  # 添加进程到队列RQ2中
while len(RQ1) != 0:  # 开始从RQ1开始选取进程p1准备运行，时间片为7
    t = 0
    i = 0
    if RQ1[i].need >= 7:  # 判断并计算该进程运行的时间
        t = 7
        RQ1[i].need -= 7
    else:
        t = RQ1[i].need
        RQ1[i].need = 0
    clock += t
    if RQ1[i].need == 0:  # 判断该进程是否运行完毕，若完毕则加入Finish,否则加入RQ1的队尾
        RQ1[i].turn += clock
        Finish.append(RQ1[i])
        RQ1.pop(i)
    else:
        p = RQ1[i]
        RQ1.pop(i)
        RQ1.append(p)
while len(RQ2) != 0:  # 开始从RQ2中选取进程准备运行，采用短进程优先调度
    i = 0
    a = 50
    x = 0
    while x < len(RQ2):  # 从RQ2中找出运行时间最短进程的进程，并加入输出对列中
        if RQ2[x].need < a:
            a = RQ2[x].need
            i = x
        x = x + 1
    clock += RQ2[i].need
    RQ2[i].turn += clock
    Finish.append(RQ2[i])
    RQ2.pop(i)
print("各进程运行时间如下：")
for f in Finish:  # 输出已完成进程的名字和周转时间
    print(f.name, f.turn)

