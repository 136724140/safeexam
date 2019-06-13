import tkinter as tk
from tkinter import *
import time
import pygame
import random
pygame.mixer.init()
def anquan():
    window2 = tk.Tk()
    window2.geometry('800x600')
    window2.title('采矿厂2019年安全生产知识竞赛')
    def bida():
        root = tk.Tk()
        root.geometry('800x600')
        root.title('采矿厂2019年安全生产知识竞赛必答题')
        global currentpage
        global pagecount
        currentpage = 0
        pagecount = 0
        v = StringVar()
        # Label(root, textvariable=v).place(x=20, y=10)
        v.set(str(currentpage))

        def topic0():
            topic0.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：第一声预告信号、第二声起爆信号、第三声解除警戒信号。', ).place(x=50, y=350)
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('ountdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='1、采场内三声爆破信号分别代表什么含义。', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic1():
            topic1.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：2.5米。', ).place(x=50, y=350)
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='2、钻机稳车时，与台阶坡顶线须保持足够的安全距离。千斤顶中心至台阶坡顶线的最小距离为多少米？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic2():
            topic2.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：6级', ).place(x=50, y=350)
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='3、多少级大风天气禁止临边作业？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic3():
            topic3.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：深孔爆破300m，潜孔爆破200m。', ).place(x=50, y=350)
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='4、爆破时个别飞石对人员的安全距离为？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic4():
            topic4.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：5分钟。', ).place(x=50, y=350)
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='5、露天深孔爆破，爆后应超过几分钟后，方准检查人员进入爆区？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic5():
            topic5.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：应不小于其最大挖掘半径的3倍，且应不小于50m。', ).place(x=50, y=350)
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='6、两台以上的挖掘机在同一平台上作业时，挖掘机的间距？ ', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic6():
            topic6.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：应配备完好的绝缘手套、绝缘靴、绝缘工具和器材等。', ).place(x=50, y=350)
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='7、电力驱动的挖掘机和电铲内应配备？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic7():
            topic7.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：车辆驾驶室。', ).place(x=50, y=350)
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='8、挖掘机装车作业时，铲斗不可以从车辆什么上方通过？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic8():
            topic8.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：30米。', ).place(x=50, y=350)
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='9、运输车辆作业时能见度不足多少米应停止作业？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic9():
            topic9.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：50米。', ).place(x=50, y=350)
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='10、冰雪或多雨季节道路较滑时，应有防滑措施并减速行驶,前后车距应不小于多少米？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic10():
            topic10.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：20米。', ).place(x=50, y=350)
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='11、正常作业条件下，同类车不应超车，前后车应保持多少米以上的安全距离？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic11():
            topic11.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：钢丝绳四根以上、大卸扣四个以上、4个35kg推车式干粉灭火器。', ).place(x=50, y=350)
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='12、排土作业区必须配备足够数量且质量合格的什么？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic12():
            topic12.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：平行坡顶线。', ).place(x=50, y=350)
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='13、推土时，在排土场边缘严禁推土机沿什么方向推土？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic13():
            topic13.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：8小时。', ).place(x=50, y=350)
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='14、严禁酒后几小时内上岗？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic14():
            topic14.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：20米。', ).place(x=50, y=350)
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='15、禁止距运行设备多少米以内的地方逗留或通行，需要接近时，应事先与司机联系好。', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic15():
            topic15.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：同时施工、同时投入生产和使用。', ).place(x=50, y=350)
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='16、什么是“三同时”？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic16():
            topic16.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：先使触电者脱离电源，再对伤者进行急救。', ).place(x=50, y=350)
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='17、有人低压触电时怎么办?   ', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic17():
            topic17.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：是指袖口紧、领口紧、下摆紧。', ).place(x=50, y=350)
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='18、工人操作机械时穿着的“三紧”工作服是哪“三紧”？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic18():
            topic18.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：凡在坠落高度基准面2m以上（含2m）有可能坠落的高处进行作业，都称为高处作业。', ).place(x=50, y=350)
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='19、按照国家标准规定，高处作业是指坠落高度基准在几米以上的作业？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic19():
            topic19.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：因为工具易于坠落伤人。', ).place(x=50, y=350)
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='20、为什么手用工具不应放在工作台边缘？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic20():
            topic20.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：可燃物、助燃物、火源。', ).place(x=50, y=350)
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='21、火灾发生时主要表现是燃烧，发生燃烧的三个条件是什么？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic21():
            topic21.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答:主要适用于扑救易燃液体、可燃气体和电气火灾。', ).place(x=50, y=350)
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='20、干粉灭火剂适合扑救哪些物质的火灾? ', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic22():
            topic22.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答:办理动火许可证。   ', ).place(x=50, y=350)
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='21、在非动火区进行动火作业,应该办理什么手续?', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic23():
            topic23.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='   答:应及时报废,不能继续使用。', ).place(x=50, y=350)
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='22、受过一次强冲击的安全帽能否继续使用?', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic24():
            topic24.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='   答:气候干燥的冬季。', ).place(x=50, y=350)
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='23、什么季节容易发生静电引起的爆炸和火灾?', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic25():
            topic25.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='   答：潮湿的环境和雨季。', ).place(x=50, y=350)
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='24、什么季节容易发生触电事故？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic26():
            topic26.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='   答： 止血、包扎、固定，送医院。', ).place(x=50, y=350)
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='25、外伤的急救步骤是什么?   ', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic27():
            topic27.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='   答：削减二氧化硫和化学需氧量的排放。', ).place(x=50, y=350)
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='26、节能减排中减排的主要指标有哪些？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic28():
            topic28.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='   答：是指废水、废气和固体废弃物。', ).place(x=50, y=350)
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='27、工业“三废”指的是哪“三废”？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic29():
            topic29.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='   答：过去、现在、将来。', ).place(x=50, y=350)
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='28、识别环境因素有哪三种时态？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic30():
            topic30.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='   答：正常、异常、紧急。', ).place(x=50, y=350)
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='29、识别环境因素有哪三种状态？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic31():
            topic31.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='   答：防风险、除隐患、遏事故。', ).place(x=50, y=350)
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='30、2019年全国安全生产月活动的主题是什么？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic32():
            topic32.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='   答：预防为主，防治结合。', ).place(x=50, y=350)
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='31、我国职业病防治工作方针是什么？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic33():
            topic33.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='   答：自用工之日起即与劳动者建立劳动关系。', ).place(x=50, y=350)
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='32、用人单位自什么时候起即与劳动者建立劳动关系。', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic34():
            topic34.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='   答:呼吸道、皮肤、消化道。', ).place(x=50, y=350)
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='33、在工业生产中,毒物主要经过什么途径进入体内?', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic35():
            topic35.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='   答:一般不得超过36伏。', ).place(x=50, y=350)
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='34、机床上使用的局部照明灯,电压有什么要求?', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic36():
            topic36.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='   答:不可以，只有36V以下的用电设备可以免装漏电保护器。', ).place(x=50, y=350)
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='35、110V以下的用电设备是否可以免装漏电保护器? ', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic37():
            topic37.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：每小时三十公里。', ).place(x=50, y=350)
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='36、采场内限行车限速每小时多少公里？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic38():
            topic38.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：轮胎直径的二分之一。', ).place(x=50, y=350)
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='37、排土场规定挡墙高度是多少？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic39():
            topic39.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：2%~5%。', ).place(x=50, y=350)
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='38、排土场规定反坡是多少？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic40():
            topic40.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：8年', ).place(x=50, y=350)
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='39、干粉灭火器的强制报废期限是？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        topic0 = Button(root,text='第1题', padx=50, pady=20, command=topic0)
        topic0.pack()
        topic0.place(x=0, y=10)
        topic0.config(state=NORMAL)
        topic1 = Button(root,text='第2题', padx=50, pady=20, command=topic1)
        topic1.pack()
        topic1.place(x=120, y=10)
        topic1.config(state=NORMAL)
        topic2 = Button(root,text='第3题', padx=50, pady=20, command=topic2)
        topic2.pack()
        topic2.place(x=240, y=10)
        topic2.config(state=NORMAL)
        topic3 = Button(root,text='第4题', padx=50, pady=20, command=topic3)
        topic3.pack()
        topic3.place(x=360, y=10)
        topic3.config(state=NORMAL)
        topic4 = Button(root,text='第5题', padx=53, pady=20, command=topic4)
        topic4.pack()
        topic4.place(x=480, y=10)
        topic4.config(state=NORMAL)
        topic5 = Button(root,text='第6题', padx=50, pady=20, command=topic5)
        topic5.pack()
        topic5.place(x=0, y=80)
        topic5.config(state=NORMAL)
        topic6 = Button(root,text='第7题', padx=50, pady=20, command=topic6)
        topic6.pack()
        topic6.place(x=120, y=80)
        topic6.config(state=NORMAL)
        topic7 = Button(root,text='第8题', padx=50, pady=20, command=topic7)
        topic7.pack()
        topic7.place(x=240, y=80)
        topic7.config(state=NORMAL)
        topic8 = Button(root,text='第9题', padx=50, pady=20, command=topic8)
        topic8.pack()
        topic8.place(x=360, y=80)
        topic8.config(state=NORMAL)
        topic9 = Button(root,text='第10题', padx=50, pady=20, command=topic9)
        topic9.pack()
        topic9.place(x=480, y=80)
        topic9.config(state=NORMAL)
        topic10 = Button(root,text='第11题', padx=50, pady=20, command=topic10)
        topic10.pack()
        topic10.place(x=0, y=150)
        topic10.config(state=NORMAL)
        topic11 = Button(root,text='第12题', padx=50, pady=20, command=topic11)
        topic11.pack()
        topic11.place(x=120, y=150)
        topic11.config(state=NORMAL)
        topic12 = Button(root,text='第13题', padx=50, pady=20, command=topic12)
        topic12.pack()
        topic12.place(x=240, y=150)
        topic12.config(state=NORMAL)
        topic13 = Button(root,text='第14题', padx=50, pady=20, command=topic13)
        topic13.pack()
        topic13.place(x=360, y=150)
        topic13.config(state=NORMAL)
        topic14 = Button(root,text='第15题', padx=50, pady=20, command=topic14)
        topic14.pack()
        topic14.place(x=480, y=150)
        topic14.config(state=NORMAL)
        topic15 = Button(root,text='第16题', padx=50, pady=20, command=topic15)
        topic15.pack()
        topic15.place(x=0, y=220)
        topic15.config(state=NORMAL)
        topic16 = Button(root,text='第17题', padx=50, pady=20, command=topic16)
        topic16.pack()
        topic16.place(x=120, y=220)
        topic16.config(state=NORMAL)
        topic17 = Button(root,text='第18题', padx=50, pady=20, command=topic17)
        topic17.pack()
        topic17.place(x=240, y=220)
        topic17.config(state=NORMAL)
        topic18 = Button(root,text='第19题', padx=50, pady=20, command=topic18)
        topic18.pack()
        topic18.place(x=360, y=220)
        topic18.config(state=NORMAL)
        topic19 = Button(root,text='第20题', padx=50, pady=20, command=topic19)
        topic19.pack()
        topic19.place(x=480, y=220)
        topic19.config(state=NORMAL)
        topic20 = Button(root,text='第21题', padx=50, pady=20, command=topic20)
        topic20.pack()
        topic20.place(x=0, y=290)
        topic20.config(state=NORMAL)
        topic21 = Button(root,text='第22题', padx=50, pady=20, command=topic21)
        topic21.pack()
        topic21.place(x=120, y=290)
        topic21.config(state=NORMAL)
        topic22 = Button(root,text='第23题', padx=50, pady=20, command=topic22)
        topic22.pack()
        topic22.place(x=240, y=290)
        topic22.config(state=NORMAL)
        topic23 = Button(root,text='第24题', padx=50, pady=20, command=topic23)
        topic23.pack()
        topic23.place(x=360, y=290)
        topic23.config(state=NORMAL)
        topic24 = Button(root,text='第25题', padx=50, pady=20, command=topic24)
        topic24.pack()
        topic24.place(x=480, y=290)
        topic24.config(state=NORMAL)
        topic25 = Button(root,text='第26题', padx=50, pady=20, command=topic25)
        topic25.pack()
        topic25.place(x=0, y=360)
        topic25.config(state=NORMAL)
        topic26 = Button(root,text='第27题', padx=50, pady=20, command=topic26)
        topic26.pack()
        topic26.place(x=120, y=360)
        topic26.config(state=NORMAL)
        topic27 = Button(root,text='第28题', padx=50, pady=20, command=topic27)
        topic27.pack()
        topic27.place(x=240, y=360)
        topic27.config(state=NORMAL)
        topic28 = Button(root,text='第29题', padx=50, pady=20, command=topic28)
        topic28.pack()
        topic28.place(x=360, y=360)
        topic28.config(state=NORMAL)
        topic29 = Button(root,text='第30题', padx=50, pady=20, command=topic29)
        topic29.pack()
        topic29.place(x=480, y=360)
        topic29.config(state=NORMAL)
        topic30 = Button(root,text='第31题', padx=50, pady=20, command=topic30)
        topic30.pack()
        topic30.place(x=0, y=430)
        topic30.config(state=NORMAL)
        topic31 = Button(root,text='第32题', padx=50, pady=20, command=topic31)
        topic31.pack()
        topic31.place(x=120, y=430)
        topic31.config(state=NORMAL)
        topic32 = Button(root,text='第33题', padx=50, pady=20, command=topic32)
        topic32.pack()
        topic32.place(x=240, y=430)
        topic32.config(state=NORMAL)
        topic33 = Button(root,text='第34题', padx=50, pady=20, command=topic33)
        topic33.pack()
        topic33.place(x=360, y=430)
        topic33.config(state=NORMAL)
        topic34 = Button(root,text='第35题', padx=50, pady=20, command=topic34)
        topic34.pack()
        topic34.place(x=480, y=430)
        topic34.config(state=NORMAL)
        topic35 = Button(root,text='第36题', padx=50, pady=20, command=topic35)
        topic35.pack()
        topic35.place(x=0, y=500)
        topic35.config(state=NORMAL)
        topic36 = Button(root,text='第37题', padx=50, pady=20, command=topic36)
        topic36.pack()
        topic36.place(x=120, y=500)
        topic36.config(state=NORMAL)
        topic37 = Button(root,text='第38题', padx=50, pady=20, command=topic37)
        topic37.pack()
        topic37.place(x=240, y=500)
        topic37.config(state=NORMAL)
        topic38 = Button(root,text='第39题', padx=50, pady=20, command=topic38)
        topic38.pack()
        topic38.place(x=360, y=500)
        topic38.config(state=NORMAL)
        topic39 = Button(root,text='第40题', padx=50, pady=20, command=topic39)
        topic39.pack()
        topic39.place(x=480, y=500)
        topic39.config(state=NORMAL)

        def page_down():
            """
            add 1 to displayed number,
            disable Btn2 button when currentpage reaches pagecount
            """
            global currentpage, pagecount

            currentpage += 1
            topic0.config(state=NORMAL, relief=RAISED)
            topic1.config(state=NORMAL, relief=RAISED)
            topic2.config(state=NORMAL, relief=RAISED)
            topic3.config(state=NORMAL, relief=RAISED)
            topic4.config(state=NORMAL, relief=RAISED)
            topic5.config(state=NORMAL, relief=RAISED)
            topic6.config(state=NORMAL, relief=RAISED)
            topic7.config(state=NORMAL, relief=RAISED)
            topic8.config(state=NORMAL, relief=RAISED)
            topic9.config(state=NORMAL, relief=RAISED)
            topic10.config(state=NORMAL, relief=RAISED)
            topic11.config(state=NORMAL, relief=RAISED)
            topic12.config(state=NORMAL, relief=RAISED)
            topic13.config(state=NORMAL, relief=RAISED)
            topic14.config(state=NORMAL, relief=RAISED)
            topic15.config(state=NORMAL, relief=RAISED)
            topic16.config(state=NORMAL, relief=RAISED)
            topic17.config(state=NORMAL, relief=RAISED)
            topic18.config(state=NORMAL, relief=RAISED)
            topic19.config(state=NORMAL, relief=RAISED)
            topic20.config(state=NORMAL, relief=RAISED)
            topic21.config(state=NORMAL, relief=RAISED)
            topic22.config(state=NORMAL, relief=RAISED)
            topic23.config(state=NORMAL, relief=RAISED)
            topic24.config(state=NORMAL, relief=RAISED)
            topic25.config(state=NORMAL, relief=RAISED)
            topic26.config(state=NORMAL, relief=RAISED)
            topic27.config(state=NORMAL, relief=RAISED)
            topic28.config(state=NORMAL, relief=RAISED)
            topic29.config(state=NORMAL, relief=RAISED)
            topic30.config(state=NORMAL, relief=RAISED)
            topic31.config(state=NORMAL, relief=RAISED)
            topic32.config(state=NORMAL, relief=RAISED)
            topic33.config(state=NORMAL, relief=RAISED)
            topic34.config(state=NORMAL, relief=RAISED)
            topic35.config(state=NORMAL, relief=RAISED)
            topic36.config(state=NORMAL, relief=RAISED)
            topic37.config(state=NORMAL, relief=RAISED)
            topic38.config(state=NORMAL, relief=RAISED)
            topic39.config(state=NORMAL, relief=RAISED)

            v.set(str(currentpage))

        Btn0 = Button(root,text="恢复", padx=8, pady=6, command=page_down)
        Btn0.pack()
        Btn0.place(x=650, y=500)

        root.mainloop()
    def xuanda():
        root = tk.Tk()
        root.geometry('800x750')
        root.title('挖掘机驾驶员安全知识竞赛选答题')
        global currentpage
        global pagecount
        currentpage = 0
        pagecount = 0
        v = StringVar()
        # Label(root, textvariable=v).place(x=20, y=10)
        v.set(str(currentpage))

        def topic0():
            topic0.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答：20米', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='1、在遇到高压电线断落地面时，导线断落点几米内，禁止人员进入。', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic1():
            topic1.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答：疲劳无力', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='2、长期在高频电磁场作用下，操作者会有什么不良反应?', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic2():
            topic2.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答：单相触电、两相触电、跨步电压触电', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='3、通常情况下，人体触电有三种情况，分别是哪三种情况？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic3():
            topic3.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答：3类', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='4、手持电动工具按触电保护一般可分为几类？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic4():
            topic4.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答：强制执行', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='5、按照国际通用标准，红色一般表示禁止或停止，黄色表示注意危险绿色表示安全，那么蓝色表示什么？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic5():
            topic5.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答：用木棍或其他绝缘物挑开触电者身上的电线或电器，关闭总电源开关。', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='6、电击伤如何切断电源？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic6():
            topic6.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='答：减压和稳压', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='7、气体焊接作业时，氧气减压器的作用是什么？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic7():
            topic7.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='    答：应停止继续超车。', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='8、驾驶人在超车时遇前方车辆不减速、不让道该怎么做？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic8():
            topic8.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答:没有动火证不动火;防火措施不落实不动火;监火人不在现场不动火。', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='9、禁火区动火作业的"三不动火"是指什么?', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic9():
            topic9.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答:防尘用具，防烫用具，眼部防护用具。', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='10、在操作打磨工具时,必须使用哪类个人防护用具?', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic10():
            topic10.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答:装设漏电保护器。', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='11、在使用手电钻、电砂轮等手持电动工具时,为保证安全,应采取什么措施?', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic11():
            topic11.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答:12伏。', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='12、在金属容器内、管道内、铁平台上、隧道内、潮湿环境等较恶劣环境中，允许使用的安全电压额定值是多少伏?', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic12():
            topic12.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答：将有害物质从产生处抽走。', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='13、局部通风的主要目的是什么？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic13():
            topic13.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答：是一种很有开发价值的资源。', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='14、垃圾是否有开发价值？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic14():
            topic14.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答：可吸入颗粒物是城区环境空气首要污染因子。', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='15、什么是城区环境空气首要污染因子？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic15():
            topic15.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答：森林有环境、社会、经济三大效益。', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='16、森林有哪三大效益？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic16():
            topic16.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答：减量化、再利用、再循环。', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='17、循环经济的3R原则是什么？ ', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic17():
            topic17.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答：管理途径、技术途径、结构途径。', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='18、节能的三大途径是什么？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic18():
            topic18.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答：节约能源，减少污物气体排放量。', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='19、“节能减排”定义是什么？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic19():
            topic19.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答：5米、10米', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='20、为防止发生火灾和爆炸事故，在气体焊接作业时氧气瓶和乙炔瓶的间距以及气瓶与火源的间距分别是多少？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic20():
            topic20.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答：用人单位的主要负责人对本单位的职业病防治工作全面负责。', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='21、用人单位的主要负责人对本单位的职业病防治工作负什么责任？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic21():
            topic21.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答：适用于中华人民共和国领域内的职业病防治活动。', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='22、职业病防治法的适用范围是什么？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic22():
            topic22.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答：工作场所，是指劳动者进行职业活动的所有地点，包括建设单位施工场所。', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='23、什么是工作场所？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic23():
            topic23.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答：指劳动者上岗前、在岗期间、离岗时、应急的职业健康检查和职业健康监护档案管理。', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='24、什么是职业健康监护？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic24():
            topic24.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答：地市级以上气象主管部门所属气象台站发布的日最高气温35℃以上的天气。', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='25、什么是高温天气？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic25():
            topic25.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='    答：明火、电能火源、化学火源、炽热物体火源。', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='26、着火源分为哪几类？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic26():
            topic26.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答：安全文化；安全法制；安全责任；安全科技；安全投入。', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='27、什么是安全生产“五要素”？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic27():
            topic27.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答：消防工作贯彻“预防为主、防消结合”的方针。', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='28、消防工作的方针是什么？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic28():
            topic28.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答：机动车上道行驶，应当悬挂机动车号牌，放置检验合格标志、保险标志、并随车携带机动车行驶证。', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='29、机动车上道路行驶应具备哪些条件？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic29():
            topic29.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答：“禁止合闸，有人工作”', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='30、停电检修时，在一经合闸即可送电到工作地点的开关或刀闸的操作把手上，应悬挂哪种标示牌?     ', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic30():
            topic30.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答：2016年7月2日 ', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='31、新修订的《职业病防治法》于何时公布实施？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic31():
            topic31.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答：企业、事业单位、个体经济组织', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='32、《职业病防治法》中所称用人单位是指哪些？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic32():
            topic32.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答：工会代表职工与企业协商', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='33、企业中签订集体合同的协商双方是什么？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic33():
            topic33.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答：临时性、辅助性、替代性', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='34、劳务派遣一般在什么性质的工作岗位上实施？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic34():
            topic34.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答：协商、调解、仲裁、诉讼', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='35、劳动争议的处理方式应该是？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic35():
            topic35.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答：创新、协调、绿色、开放、共享  ', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='36、发展是解决我国一切问题的基础和关键，发展必须是科学发展，必须坚定不移贯彻什么的发展理念？   ', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic36():
            topic36.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答：决胜期', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='37、从现在到二〇二〇年，是全面建成小康社会什么期？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic37():
            topic37.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答：建立健全绿色低碳循环发展的经济体系。', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='38、加快建立绿色生产和消费的法律制度和政策导向，应当建立健全什么的经济体系？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic38():
            topic38.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答：职业病危害及其后果职业病防护措施和待遇', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='39、用人单位与劳动者订立劳动合同时，应当将工作过程中可能产生的（ ）如实告知劳动者，并在劳动合同中写明，不得隐瞒或者欺骗。', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic39():
            topic39.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='答：实现共产主义', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='40、党的最高理想和最终目标是什么？。', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic40():
            topic40.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='答：全心全意为人民服务', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='   41、中国共产党的根本宗旨是什么？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic41():
            topic41.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答：富强、民主、文明、和谐,自由、平等、公正、法治, 爱国、敬业、诚信、友善。', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='42、二十四字核心价值观是什么？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic42():
            topic42.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答：①劳动报酬  ②休息休假  ③工作时间  ④劳动安全卫生  ⑤保险福利', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='43、集体合同的主要内容有哪些？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic43():
            topic43.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答：厂（分公司）级教育、车间教育、班组教育', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='44、按照国家规定，新职工入厂首先要接受“三级安全教育”，分别是哪三级教育？ ', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic44():
            topic44.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答：我不伤害自己、我不伤害别人、我不被别人伤害', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='45、什么是“三不伤害”？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic45():
            topic45.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答：预防、预备、响应和恢复四个阶段。', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='46、事故应急管理包括哪些阶段？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic46():
            topic46.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答：国家的法律、规定和技术标准', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='47、安全管理以什么为依据,采取各种手段,对企业安全状况实施有效制约的一切活动。', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic47():
            topic47.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答：保护接地或保护接零', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='48、国际电工委员会规定，为防止间接触电事故的发生，应采取什么技术措施？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic48():
            topic48.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答：5年', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window,
                     text='49、生产经营单位主要负责人，因未履行《安全生产法》规定的安全生产管理职责，导致发生重大安全生产事故，而受到刑事处罚或撤职处分的，几年内不能担任任何生产经营单位主要负责人？', ).place(
                x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        def topic49():
            topic49.config(state=DISABLED, relief='sunken')
            global currentpage, pagecount

            def answer():
                tk.Label(window, text='   答：违章指挥、违章作业、违反劳动纪律', ).place(x=50, y=350)
                pygame.mixer.music.stop()()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            tk.Label(window, text='50、什么是“三违”？', ).place(x=50, y=50)
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        topic0 = Button(root,text='第1题', padx=50, pady=20, command=topic0)
        topic0.pack()
        topic0.place(x=0, y=10)
        topic0.config(state=NORMAL)
        topic1 = Button(root,text='第2题', padx=50, pady=20, command=topic1)
        topic1.pack()
        topic1.place(x=120, y=10)
        topic1.config(state=NORMAL)
        topic2 = Button(root,text='第3题', padx=50, pady=20, command=topic2)
        topic2.pack()
        topic2.place(x=240, y=10)
        topic2.config(state=NORMAL)
        topic3 = Button(root,text='第4题', padx=50, pady=20, command=topic3)
        topic3.pack()
        topic3.place(x=360, y=10)
        topic3.config(state=NORMAL)
        topic4 = Button(root,text='第5题', padx=53, pady=20, command=topic4)
        topic4.pack()
        topic4.place(x=480, y=10)
        topic4.config(state=NORMAL)
        topic5 = Button(root,text='第6题', padx=50, pady=20, command=topic5)
        topic5.pack()
        topic5.place(x=0, y=80)
        topic5.config(state=NORMAL)
        topic6 = Button(root,text='第7题', padx=50, pady=20, command=topic6)
        topic6.pack()
        topic6.place(x=120, y=80)
        topic6.config(state=NORMAL)
        topic7 = Button(root,text='第8题', padx=50, pady=20, command=topic7)
        topic7.pack()
        topic7.place(x=240, y=80)
        topic7.config(state=NORMAL)
        topic8 = Button(root,text='第9题', padx=50, pady=20, command=topic8)
        topic8.pack()
        topic8.place(x=360, y=80)
        topic8.config(state=NORMAL)
        topic9 = Button(root,text='第10题', padx=50, pady=20, command=topic9)
        topic9.pack()
        topic9.place(x=480, y=80)
        topic9.config(state=NORMAL)
        topic10 = Button(root,text='第11题', padx=50, pady=20, command=topic10)
        topic10.pack()
        topic10.place(x=0, y=150)
        topic10.config(state=NORMAL)
        topic11 = Button(root,text='第12题', padx=50, pady=20, command=topic11)
        topic11.pack()
        topic11.place(x=120, y=150)
        topic11.config(state=NORMAL)
        topic12 = Button(root,text='第13题', padx=50, pady=20, command=topic12)
        topic12.pack()
        topic12.place(x=240, y=150)
        topic12.config(state=NORMAL)
        topic13 = Button(root,text='第14题', padx=50, pady=20, command=topic13)
        topic13.pack()
        topic13.place(x=360, y=150)
        topic13.config(state=NORMAL)
        topic14 = Button(root,text='第15题', padx=50, pady=20, command=topic14)
        topic14.pack()
        topic14.place(x=480, y=150)
        topic14.config(state=NORMAL)
        topic15 = Button(root,text='第16题', padx=50, pady=20, command=topic15)
        topic15.pack()
        topic15.place(x=0, y=220)
        topic15.config(state=NORMAL)
        topic16 = Button(root,text='第17题', padx=50, pady=20, command=topic16)
        topic16.pack()
        topic16.place(x=120, y=220)
        topic16.config(state=NORMAL)
        topic17 = Button(root,text='第18题', padx=50, pady=20, command=topic17)
        topic17.pack()
        topic17.place(x=240, y=220)
        topic17.config(state=NORMAL)
        topic18 = Button(root,text='第19题', padx=50, pady=20, command=topic18)
        topic18.pack()
        topic18.place(x=360, y=220)
        topic18.config(state=NORMAL)
        topic19 = Button(root,text='第20题', padx=50, pady=20, command=topic19)
        topic19.pack()
        topic19.place(x=480, y=220)
        topic19.config(state=NORMAL)
        topic20 = Button(root,text='第21题', padx=50, pady=20, command=topic20)
        topic20.pack()
        topic20.place(x=0, y=290)
        topic20.config(state=NORMAL)
        topic21 = Button(root,text='第22题', padx=50, pady=20, command=topic21)
        topic21.pack()
        topic21.place(x=120, y=290)
        topic21.config(state=NORMAL)
        topic22 = Button(root,text='第23题', padx=50, pady=20, command=topic22)
        topic22.pack()
        topic22.place(x=240, y=290)
        topic22.config(state=NORMAL)
        topic23 = Button(root,text='第24题', padx=50, pady=20, command=topic23)
        topic23.pack()
        topic23.place(x=360, y=290)
        topic23.config(state=NORMAL)
        topic24 = Button(root,text='第25题', padx=50, pady=20, command=topic24)
        topic24.pack()
        topic24.place(x=480, y=290)
        topic24.config(state=NORMAL)
        topic25 = Button(root,text='第26题', padx=50, pady=20, command=topic25)
        topic25.pack()
        topic25.place(x=0, y=360)
        topic25.config(state=NORMAL)
        topic26 = Button(root,text='第27题', padx=50, pady=20, command=topic26)
        topic26.pack()
        topic26.place(x=120, y=360)
        topic26.config(state=NORMAL)
        topic27 = Button(root,text='第28题', padx=50, pady=20, command=topic27)
        topic27.pack()
        topic27.place(x=240, y=360)
        topic27.config(state=NORMAL)
        topic28 = Button(root,text='第29题', padx=50, pady=20, command=topic28)
        topic28.pack()
        topic28.place(x=360, y=360)
        topic28.config(state=NORMAL)
        topic29 = Button(root,text='第30题', padx=50, pady=20, command=topic29)
        topic29.pack()
        topic29.place(x=480, y=360)
        topic29.config(state=NORMAL)
        topic30 = Button(root,text='第31题', padx=50, pady=20, command=topic30)
        topic30.pack()
        topic30.place(x=0, y=430)
        topic30.config(state=NORMAL)
        topic31 = Button(root,text='第32题', padx=50, pady=20, command=topic31)
        topic31.pack()
        topic31.place(x=120, y=430)
        topic31.config(state=NORMAL)
        topic32 = Button(root,text='第33题', padx=50, pady=20, command=topic32)
        topic32.pack()
        topic32.place(x=240, y=430)
        topic32.config(state=NORMAL)
        topic33 = Button(root,text='第34题', padx=50, pady=20, command=topic33)
        topic33.pack()
        topic33.place(x=360, y=430)
        topic33.config(state=NORMAL)
        topic34 = Button(root,text='第35题', padx=50, pady=20, command=topic34)
        topic34.pack()
        topic34.place(x=480, y=430)
        topic34.config(state=NORMAL)
        topic35 = Button(root,text='第36题', padx=50, pady=20, command=topic35)
        topic35.pack()
        topic35.place(x=0, y=500)
        topic35.config(state=NORMAL)
        topic36 = Button(root,text='第37题', padx=50, pady=20, command=topic36)
        topic36.pack()
        topic36.place(x=120, y=500)
        topic36.config(state=NORMAL)
        topic37 = Button(root,text='第38题', padx=50, pady=20, command=topic37)
        topic37.pack()
        topic37.place(x=240, y=500)
        topic37.config(state=NORMAL)
        topic38 = Button(root,text='第39题', padx=50, pady=20, command=topic38)
        topic38.pack()
        topic38.place(x=360, y=500)
        topic38.config(state=NORMAL)
        topic39 = Button(root,text='第40题', padx=50, pady=20, command=topic39)
        topic39.pack()
        topic39.place(x=480, y=500)
        topic39.config(state=NORMAL)
        topic40 = Button(root,text='第41题', padx=50, pady=20, command=topic40)
        topic40.pack()
        topic40.place(x=0, y=570)
        topic40.config(state=NORMAL)
        topic41 = Button(root,text='第42题', padx=50, pady=20, command=topic41)
        topic41.pack()
        topic41.place(x=120, y=570)
        topic41.config(state=NORMAL)
        topic42 = Button(root,text='第43题', padx=50, pady=20, command=topic42)
        topic42.pack()
        topic42.place(x=240, y=570)
        topic42.config(state=NORMAL)
        topic43 = Button(root,text='第44题', padx=50, pady=20, command=topic43)
        topic43.pack()
        topic43.place(x=360, y=570)
        topic43.config(state=NORMAL)
        topic44 = Button(root,text='第45题', padx=50, pady=20, command=topic44)
        topic44.pack()
        topic44.place(x=480, y=570)
        topic44.config(state=NORMAL)
        topic45 = Button(root,text='第46题', padx=50, pady=20, command=topic45)
        topic45.pack()
        topic45.place(x=0, y=640)
        topic45.config(state=NORMAL)
        topic46 = Button(root,text='第47题', padx=50, pady=20, command=topic46)
        topic46.pack()
        topic46.place(x=120, y=640)
        topic46.config(state=NORMAL)
        topic47 = Button(root,text='第48题', padx=50, pady=20, command=topic47)
        topic47.pack()
        topic47.place(x=240, y=640)
        topic47.config(state=NORMAL)
        topic48 = Button(root,text='第49题', padx=50, pady=20, command=topic48)
        topic48.pack()
        topic48.place(x=360, y=640)
        topic48.config(state=NORMAL)
        topic49 = Button(root,text='第50题', padx=50, pady=20, command=topic49)
        topic49.pack()
        topic49.place(x=480, y=640)
        topic49.config(state=NORMAL)

        def page_down():
            """
            add 1 to displayed number,
            disable Btn2 button when currentpage reaches pagecount
            """
            global currentpage, pagecount

            currentpage += 1
            topic0.config(state=NORMAL, relief=RAISED)
            topic1.config(state=NORMAL, relief=RAISED)
            topic2.config(state=NORMAL, relief=RAISED)
            topic3.config(state=NORMAL, relief=RAISED)
            topic4.config(state=NORMAL, relief=RAISED)
            topic5.config(state=NORMAL, relief=RAISED)
            topic6.config(state=NORMAL, relief=RAISED)
            topic7.config(state=NORMAL, relief=RAISED)
            topic8.config(state=NORMAL, relief=RAISED)
            topic9.config(state=NORMAL, relief=RAISED)
            topic10.config(state=NORMAL, relief=RAISED)
            topic11.config(state=NORMAL, relief=RAISED)
            topic12.config(state=NORMAL, relief=RAISED)
            topic13.config(state=NORMAL, relief=RAISED)
            topic14.config(state=NORMAL, relief=RAISED)
            topic15.config(state=NORMAL, relief=RAISED)
            topic16.config(state=NORMAL, relief=RAISED)
            topic17.config(state=NORMAL, relief=RAISED)
            topic18.config(state=NORMAL, relief=RAISED)
            topic19.config(state=NORMAL, relief=RAISED)
            topic20.config(state=NORMAL, relief=RAISED)
            topic21.config(state=NORMAL, relief=RAISED)
            topic22.config(state=NORMAL, relief=RAISED)
            topic23.config(state=NORMAL, relief=RAISED)
            topic24.config(state=NORMAL, relief=RAISED)
            topic25.config(state=NORMAL, relief=RAISED)
            topic26.config(state=NORMAL, relief=RAISED)
            topic27.config(state=NORMAL, relief=RAISED)
            topic28.config(state=NORMAL, relief=RAISED)
            topic29.config(state=NORMAL, relief=RAISED)
            topic30.config(state=NORMAL, relief=RAISED)
            topic31.config(state=NORMAL, relief=RAISED)
            topic32.config(state=NORMAL, relief=RAISED)
            topic33.config(state=NORMAL, relief=RAISED)
            topic34.config(state=NORMAL, relief=RAISED)
            topic35.config(state=NORMAL, relief=RAISED)
            topic36.config(state=NORMAL, relief=RAISED)
            topic37.config(state=NORMAL, relief=RAISED)
            topic38.config(state=NORMAL, relief=RAISED)
            topic39.config(state=NORMAL, relief=RAISED)
            topic40.config(state=NORMAL, relief=RAISED)
            topic41.config(state=NORMAL, relief=RAISED)
            topic42.config(state=NORMAL, relief=RAISED)
            topic43.config(state=NORMAL, relief=RAISED)
            topic44.config(state=NORMAL, relief=RAISED)
            topic45.config(state=NORMAL, relief=RAISED)
            topic46.config(state=NORMAL, relief=RAISED)
            topic47.config(state=NORMAL, relief=RAISED)
            topic48.config(state=NORMAL, relief=RAISED)
            topic49.config(state=NORMAL, relief=RAISED)

            v.set(str(currentpage))

        Btn0 = Button(root,text="恢复", padx=8, pady=6, command=page_down)
        Btn0.pack()
        Btn0.place(x=650, y=500)

        root.mainloop()
    topic0_window2 = Button(window2,text='必答题', padx=200, pady=20, command=bida)
    topic0_window2.pack()
    topic0_window2.place(x=0, y=10)
    topic0_window2.config(state=NORMAL)
    topic0_window2 = Button(window2,text='选答题', padx=200, pady=20, command=xuanda)
    topic0_window2.pack()
    topic0_window2.place(x=0, y=80)
    topic0_window2.config(state=NORMAL)
    topic0_window2 = Button(window2,text='风险题', padx=200, pady=20, command=bida)
    topic0_window2.pack()
    topic0_window2.place(x=0, y=150)
    topic0_window2.config(state=NORMAL)
def baopo():
    window2 = tk.Tk()
    window2.geometry('800x600')
    window2.title('采矿厂2019年安全生产知识竞赛--爆破员')
    def bida():
        root = tk.Tk()
        root.geometry('800x750')
        root.title('采矿厂2019年安全生产知识竞赛--爆破员必答题')
        global currentpage
        global pagecount
        currentpage = 0
        pagecount = 0
        v = StringVar()
        # Label(root, textvariable=v).place(x=20, y=10)
        v.set(str(currentpage))

        def topic0():
            topic0.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：行政许可，罚款，追究行政与刑事责任。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='1．政府主管部门在民用爆炸物品安全管理中经常使用哪些措施？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic1():
            topic1.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：一氧化碳，氮的氧化物。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='2.炸药爆炸产生的有毒有害气体大部分是什么？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic2():
            topic2.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：硝酸盐水溶液，油包水型乳化剂。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='3.乳化炸药由以下哪些组分构成？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic3():
            topic3.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：乳化炸药，水胶炸药。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='4.哪些炸药可直接用于有水的深孔爆破和浅孔爆破作业？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic4():
            topic4.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：管壳，加强帽，装药，电引火头。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='5．电雷管由哪些部分组成？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic5():
            topic5.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：专用起爆器，导爆索，雷管。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='6. 哪些器材可以引爆导爆管？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic6():
            topic6.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：操作简单，可靠性高，安全性好。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='7．导爆索起爆网路具有哪些等优点？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic7():
            topic7.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：管壳，装药，电子电路。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='8．电子雷管由哪些部分组成？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic8():
            topic8.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：毫秒延期雷管，半秒延期雷管，秒延期雷管，瞬发雷管。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='9. 导爆管雷管按照延期时间分为哪四种？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic9():
            topic9.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：其中硝酸铵占94.0％－95.0％，柴油占5.0％－6.0％。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='10.常用的多孔粒状铵油炸药由多孔粒状硝酸铵和柴油组成，其中硝酸铵与柴油分别占多少百分比？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic10():
            topic10.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：爆炸气体压力作用理论、爆炸应力波反射作用理论、应力波与爆炸气体综合作用理论。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='11．目前，公认的岩石爆炸破坏理论有哪三种？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic11():
            topic11.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：压缩空腔，粉碎区，裂隙区，振动区。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='12．炸药在岩石内部爆炸作用时，由炸药近区向远区分别形成哪些区？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic12():
            topic12.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：爆破飞石，爆破毒气，爆破噪音。  ', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='13．下面哪些是爆破有害效应？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic13():
            topic13.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：预裂缝的作用主要是减弱主爆区爆破时对保留岩体的破坏并形成平整轮廓面。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='14. 预裂爆破是一种控制爆破，形成的预裂缝起何作用？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic14():
            topic14.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：有无盲炮，有无危石，有无塌方等情况。 ', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='15. 爆后安全检查的主要内容有？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic15():
            topic15.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：安全员，爆破员。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='16. 爆破作业单位运输爆炸物品车辆的押运工作可以由谁负责？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic16():
            topic16.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：化学反应过程大量放热，反应过程极快，生成大量气体产物。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='17. 炸药爆炸三要素是什么？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic17():
            topic17.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：热能、机械能和爆炸能。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='18. 炸药起爆能有几种形式？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic18():
            topic18.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：炸药在外界能量作用下，发生爆炸反应的难易程度称为炸药感度。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='19. 什么叫炸药的感度？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic19():
            topic19.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：物理爆炸，化学爆炸，核爆炸。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='20．根据爆炸产生的原因及特征，爆炸现象可分为哪几类？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic20():
            topic20.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：三年以上十年以下有期徒刑。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='21. 对于非法买卖、储存3公斤炸药的人员，可以处几年有期徒刑？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        topic0 = Button(root,text='第1题', padx=50, pady=50, command=topic0)
        topic0.pack()
        topic0.place(x=0, y=10)
        topic0.config(state=NORMAL)
        topic1 = Button(root,text='第2题', padx=50, pady=50, command=topic1)
        topic1.pack()
        topic1.place(x=120, y=10)
        topic1.config(state=NORMAL)
        topic2 = Button(root,text='第3题', padx=50, pady=50, command=topic2)
        topic2.pack()
        topic2.place(x=240, y=10)
        topic2.config(state=NORMAL)
        topic3 = Button(root,text='第4题', padx=50, pady=50, command=topic3)
        topic3.pack()
        topic3.place(x=360, y=10)
        topic3.config(state=NORMAL)
        topic4 = Button(root,text='第5题', padx=53, pady=50, command=topic4)
        topic4.pack()
        topic4.place(x=480, y=10)
        topic4.config(state=NORMAL)
        topic5 = Button(root,text='第6题', padx=50, pady=50, command=topic5)
        topic5.pack()
        topic5.place(x=0, y=120)
        topic5.config(state=NORMAL)
        topic6 = Button(root,text='第7题', padx=50, pady=50, command=topic6)
        topic6.pack()
        topic6.place(x=120, y=120)
        topic6.config(state=NORMAL)
        topic7 = Button(root,text='第8题', padx=50, pady=50, command=topic7)
        topic7.pack()
        topic7.place(x=240, y=120)
        topic7.config(state=NORMAL)
        topic8 = Button(root,text='第9题', padx=50, pady=50, command=topic8)
        topic8.pack()
        topic8.place(x=360, y=120)
        topic8.config(state=NORMAL)
        topic9 = Button(root,text='第10题', padx=50, pady=50, command=topic9)
        topic9.pack()
        topic9.place(x=480, y=120)
        topic9.config(state=NORMAL)
        topic10 = Button(root,text='第11题', padx=50, pady=50, command=topic10)
        topic10.pack()
        topic10.place(x=0, y=230)
        topic10.config(state=NORMAL)
        topic11 = Button(root,text='第12题', padx=50, pady=50, command=topic11)
        topic11.pack()
        topic11.place(x=120, y=230)
        topic11.config(state=NORMAL)
        topic12 = Button(root,text='第13题', padx=50, pady=50, command=topic12)
        topic12.pack()
        topic12.place(x=240, y=230)
        topic12.config(state=NORMAL)
        topic13 = Button(root,text='第14题', padx=50, pady=50, command=topic13)
        topic13.pack()
        topic13.place(x=360, y=230)
        topic13.config(state=NORMAL)
        topic14 = Button(root,text='第15题', padx=50, pady=50, command=topic14)
        topic14.pack()
        topic14.place(x=480, y=230)
        topic14.config(state=NORMAL)
        topic15 = Button(root,text='第16题', padx=50, pady=50, command=topic15)
        topic15.pack()
        topic15.place(x=0, y=340)
        topic15.config(state=NORMAL)
        topic16 = Button(root,text='第17题', padx=50, pady=50, command=topic16)
        topic16.pack()
        topic16.place(x=120, y=340)
        topic16.config(state=NORMAL)
        topic17 = Button(root,text='第18题', padx=50, pady=50, command=topic17)
        topic17.pack()
        topic17.place(x=240, y=340)
        topic17.config(state=NORMAL)
        topic18 = Button(root,text='第19题', padx=50, pady=50, command=topic18)
        topic18.pack()
        topic18.place(x=360, y=340)
        topic18.config(state=NORMAL)
        topic19 = Button(root,text='第20题', padx=50, pady=50, command=topic19)
        topic19.pack()
        topic19.place(x=480, y=340)
        topic19.config(state=NORMAL)

        def page_down():
            """
            add 1 to displayed number,
            disable Btn2 button when currentpage reaches pagecount
            """
            global currentpage, pagecount

            currentpage += 1
            topic0.config(state=NORMAL, relief=RAISED)
            topic1.config(state=NORMAL, relief=RAISED)
            topic2.config(state=NORMAL, relief=RAISED)
            topic3.config(state=NORMAL, relief=RAISED)
            topic4.config(state=NORMAL, relief=RAISED)
            topic5.config(state=NORMAL, relief=RAISED)
            topic6.config(state=NORMAL, relief=RAISED)
            topic7.config(state=NORMAL, relief=RAISED)
            topic8.config(state=NORMAL, relief=RAISED)
            topic9.config(state=NORMAL, relief=RAISED)
            topic10.config(state=NORMAL, relief=RAISED)
            topic11.config(state=NORMAL, relief=RAISED)
            topic12.config(state=NORMAL, relief=RAISED)
            topic13.config(state=NORMAL, relief=RAISED)
            topic14.config(state=NORMAL, relief=RAISED)
            topic15.config(state=NORMAL, relief=RAISED)
            topic16.config(state=NORMAL, relief=RAISED)
            topic17.config(state=NORMAL, relief=RAISED)
            topic18.config(state=NORMAL, relief=RAISED)
            topic19.config(state=NORMAL, relief=RAISED)

            v.set(str(currentpage))

        Btn0 = Button(root,text="恢复", padx=8, pady=6, command=page_down)
        Btn0.pack()
        Btn0.place(x=650, y=500)

        root.mainloop()
    def xuanda():
        root = tk.Tk()
        root.geometry('800x750')
        root.title('采矿厂2019年安全生产知识竞赛--爆破员选答题')
        global currentpage
        global pagecount
        currentpage = 0
        pagecount = 0
        v = StringVar()
        # Label(root, textvariable=v).place(x=20, y=10)
        v.set(str(currentpage))

        def topic0():
            topic0.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：行政许可，罚款，追究行政与刑事责任。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='1．政府主管部门在民用爆炸物品安全管理中经常使用哪些措施？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic1():
            topic1.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：一氧化碳，氮的氧化物。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='2.炸药爆炸产生的有毒有害气体大部分是什么？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic2():
            topic2.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：硝酸盐水溶液，油包水型乳化剂。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='3.乳化炸药由以下哪些组分构成？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic3():
            topic3.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：乳化炸药，水胶炸药。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='4.哪些炸药可直接用于有水的深孔爆破和浅孔爆破作业？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic4():
            topic4.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：管壳，加强帽，装药，电引火头。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='5．电雷管由哪些部分组成？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic5():
            topic5.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：专用起爆器，导爆索，雷管。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='6. 哪些器材可以引爆导爆管？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic6():
            topic6.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：操作简单，可靠性高，安全性好。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='7．导爆索起爆网路具有哪些等优点？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic7():
            topic7.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：管壳，装药，电子电路。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='8．电子雷管由哪些部分组成？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic8():
            topic8.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：毫秒延期雷管，半秒延期雷管，秒延期雷管，瞬发雷管。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='9. 导爆管雷管按照延期时间分为哪四种？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic9():
            topic9.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：其中硝酸铵占94.0％－95.0％，柴油占5.0％－6.0％。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='10.常用的多孔粒状铵油炸药由多孔粒状硝酸铵和柴油组成，其中硝酸铵与柴油分别占多少百分比？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic10():
            topic10.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：爆炸气体压力作用理论、爆炸应力波反射作用理论、应力波与爆炸气体综合作用理论。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='11．目前，公认的岩石爆炸破坏理论有哪三种？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic11():
            topic11.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：压缩空腔，粉碎区，裂隙区，振动区。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='12．炸药在岩石内部爆炸作用时，由炸药近区向远区分别形成哪些区？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic12():
            topic12.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：爆破飞石，爆破毒气，爆破噪音。  ', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='13．下面哪些是爆破有害效应？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic13():
            topic13.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：预裂缝的作用主要是减弱主爆区爆破时对保留岩体的破坏并形成平整轮廓面。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='14. 预裂爆破是一种控制爆破，形成的预裂缝起何作用？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic14():
            topic14.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：有无盲炮，有无危石，有无塌方等情况。 ', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='15. 爆后安全检查的主要内容有？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic15():
            topic15.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：安全员，爆破员。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='16. 爆破作业单位运输爆炸物品车辆的押运工作可以由谁负责？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic16():
            topic16.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：化学反应过程大量放热，反应过程极快，生成大量气体产物。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='17. 炸药爆炸三要素是什么？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic17():
            topic17.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：热能、机械能和爆炸能。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='18. 炸药起爆能有几种形式？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic18():
            topic18.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：炸药在外界能量作用下，发生爆炸反应的难易程度称为炸药感度。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='19. 什么叫炸药的感度？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic19():
            topic19.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：物理爆炸，化学爆炸，核爆炸。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='20．根据爆炸产生的原因及特征，爆炸现象可分为哪几类？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic20():
            topic20.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：三年以上十年以下有期徒刑。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='21. 对于非法买卖、储存3公斤炸药的人员，可以处几年有期徒刑？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic21():
            topic21.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：处十年以上有期徒刑、无期徒刑或者死刑。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='22.对于非法买卖、储存6公斤炸药的人员，可以处几年有期徒刑？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic22():
            topic22.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：三年以上十年以下有期徒刑。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='23.对于非法买卖、储存50枚雷管的人员，可以处几年有期徒刑？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic23():
            topic23.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：管内断药超过20cm；管壁破裂口大于lcm；管内有水、异物或涂药结节。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='24. 导爆管拒爆的主要原因有哪些？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic24():
            topic24.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：有铵油炸药和含水炸药（浆状炸药、水胶炸药和乳化炸药）。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='25.工程上常用的硝铵类炸药有哪几种？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic25():
            topic25.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：具有良好的抗水性能和传爆性能，可用8号雷管直接起爆。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='26.乳化炸药的特点是什么？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic26():
            topic26.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：操作简单，容易掌握；安全性好，不受外来电流影响；易于多段延期爆破。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='27.导爆管起爆网路有何优点？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic27():
            topic27.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：一个药包（卷）爆炸后，引起与它不相接触的邻近药包（卷）爆炸的现象。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='28．什么叫殉爆？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic28():
            topic28.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：当装药直径小于炮孔直径时，炮孔直径与装药直径的比值称为装药不耦合系数。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='29. 请说出装药不耦合系数的含义？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic29():
            topic29.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：相邻炮孔或药包群之间的起爆时间间隔以毫秒计的延期爆破。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='30. 何为毫秒爆破？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        topic0 = Button(root,text='第1题', padx=50, pady=20, command=topic0)
        topic0.pack()
        topic0.place(x=0, y=10)
        topic0.config(state=NORMAL)
        topic1 = Button(root,text='第2题', padx=50, pady=20, command=topic1)
        topic1.pack()
        topic1.place(x=120, y=10)
        topic1.config(state=NORMAL)
        topic2 = Button(root,text='第3题', padx=50, pady=20, command=topic2)
        topic2.pack()
        topic2.place(x=240, y=10)
        topic2.config(state=NORMAL)
        topic3 = Button(root,text='第4题', padx=50, pady=20, command=topic3)
        topic3.pack()
        topic3.place(x=360, y=10)
        topic3.config(state=NORMAL)
        topic4 = Button(root,text='第5题', padx=50, pady=20, command=topic4)
        topic4.pack()
        topic4.place(x=480, y=10)
        topic4.config(state=NORMAL)
        topic5 = Button(root,text='第6题', padx=50, pady=20, command=topic5)
        topic5.pack()
        topic5.place(x=0, y=80)
        topic5.config(state=NORMAL)
        topic6 = Button(root,text='第7题', padx=50, pady=20, command=topic6)
        topic6.pack()
        topic6.place(x=120, y=80)
        topic6.config(state=NORMAL)
        topic7 = Button(root,text='第8题', padx=50, pady=20, command=topic7)
        topic7.pack()
        topic7.place(x=240, y=80)
        topic7.config(state=NORMAL)
        topic8 = Button(root,text='第9题', padx=50, pady=20, command=topic8)
        topic8.pack()
        topic8.place(x=360, y=80)
        topic8.config(state=NORMAL)
        topic9 = Button(root,text='第10题', padx=50, pady=20, command=topic9)
        topic9.pack()
        topic9.place(x=480, y=80)
        topic9.config(state=NORMAL)
        topic10 = Button(root,text='第11题', padx=50, pady=20, command=topic10)
        topic10.pack()
        topic10.place(x=0, y=150)
        topic10.config(state=NORMAL)
        topic11 = Button(root,text='第12题', padx=50, pady=20, command=topic11)
        topic11.pack()
        topic11.place(x=120, y=150)
        topic11.config(state=NORMAL)
        topic12 = Button(root,text='第13题', padx=50, pady=20, command=topic12)
        topic12.pack()
        topic12.place(x=240, y=150)
        topic12.config(state=NORMAL)
        topic13 = Button(root,text='第14题', padx=50, pady=20, command=topic13)
        topic13.pack()
        topic13.place(x=360, y=150)
        topic13.config(state=NORMAL)
        topic14 = Button(root,text='第15题', padx=50, pady=20, command=topic14)
        topic14.pack()
        topic14.place(x=480, y=150)
        topic14.config(state=NORMAL)
        topic15 = Button(root,text='第16题', padx=50, pady=20, command=topic15)
        topic15.pack()
        topic15.place(x=0, y=220)
        topic15.config(state=NORMAL)
        topic16 = Button(root,text='第17题', padx=50, pady=20, command=topic16)
        topic16.pack()
        topic16.place(x=120, y=220)
        topic16.config(state=NORMAL)
        topic17 = Button(root,text='第18题', padx=50, pady=20, command=topic17)
        topic17.pack()
        topic17.place(x=240, y=220)
        topic17.config(state=NORMAL)
        topic18 = Button(root,text='第19题', padx=50, pady=20, command=topic18)
        topic18.pack()
        topic18.place(x=360, y=220)
        topic18.config(state=NORMAL)
        topic19 = Button(root,text='第20题', padx=50, pady=20, command=topic19)
        topic19.pack()
        topic19.place(x=480, y=220)
        topic19.config(state=NORMAL)
        topic20 = Button(root,text='第21题', padx=50, pady=20, command=topic20)
        topic20.pack()
        topic20.place(x=0, y=290)
        topic20.config(state=NORMAL)
        topic21 = Button(root,text='第22题', padx=50, pady=20, command=topic21)
        topic21.pack()
        topic21.place(x=120, y=290)
        topic21.config(state=NORMAL)
        topic22 = Button(root,text='第23题', padx=50, pady=20, command=topic22)
        topic22.pack()
        topic22.place(x=240, y=290)
        topic22.config(state=NORMAL)
        topic23 = Button(root,text='第24题', padx=50, pady=20, command=topic23)
        topic23.pack()
        topic23.place(x=360, y=290)
        topic23.config(state=NORMAL)
        topic24 = Button(root,text='第25题', padx=50, pady=20, command=topic24)
        topic24.pack()
        topic24.place(x=480, y=290)
        topic24.config(state=NORMAL)
        topic25 = Button(root,text='第26题', padx=50, pady=20, command=topic25)
        topic25.pack()
        topic25.place(x=0, y=360)
        topic25.config(state=NORMAL)
        topic26 = Button(root,text='第27题', padx=50, pady=20, command=topic26)
        topic26.pack()
        topic26.place(x=120, y=360)
        topic26.config(state=NORMAL)
        topic27 = Button(root,text='第28题', padx=50, pady=20, command=topic27)
        topic27.pack()
        topic27.place(x=240, y=360)
        topic27.config(state=NORMAL)
        topic28 = Button(root,text='第29题', padx=50, pady=20, command=topic28)
        topic28.pack()
        topic28.place(x=360, y=360)
        topic28.config(state=NORMAL)
        topic29 = Button(root,text='第30题', padx=50, pady=20, command=topic29)
        topic29.pack()
        topic29.place(x=480, y=360)
        topic29.config(state=NORMAL)

        def page_down():
            """
            add 1 to displayed number,
            disable Btn2 button when currentpage reaches pagecount
            """
            global currentpage, pagecount

            currentpage += 1
            topic0.config(state=NORMAL, relief=RAISED)
            topic1.config(state=NORMAL, relief=RAISED)
            topic2.config(state=NORMAL, relief=RAISED)
            topic3.config(state=NORMAL, relief=RAISED)
            topic4.config(state=NORMAL, relief=RAISED)
            topic5.config(state=NORMAL, relief=RAISED)
            topic6.config(state=NORMAL, relief=RAISED)
            topic7.config(state=NORMAL, relief=RAISED)
            topic8.config(state=NORMAL, relief=RAISED)
            topic9.config(state=NORMAL, relief=RAISED)
            topic10.config(state=NORMAL, relief=RAISED)
            topic11.config(state=NORMAL, relief=RAISED)
            topic12.config(state=NORMAL, relief=RAISED)
            topic13.config(state=NORMAL, relief=RAISED)
            topic14.config(state=NORMAL, relief=RAISED)
            topic15.config(state=NORMAL, relief=RAISED)
            topic16.config(state=NORMAL, relief=RAISED)
            topic17.config(state=NORMAL, relief=RAISED)
            topic18.config(state=NORMAL, relief=RAISED)
            topic19.config(state=NORMAL, relief=RAISED)
            topic20.config(state=NORMAL, relief=RAISED)
            topic21.config(state=NORMAL, relief=RAISED)
            topic22.config(state=NORMAL, relief=RAISED)
            topic23.config(state=NORMAL, relief=RAISED)
            topic24.config(state=NORMAL, relief=RAISED)
            topic25.config(state=NORMAL, relief=RAISED)
            topic26.config(state=NORMAL, relief=RAISED)
            topic27.config(state=NORMAL, relief=RAISED)
            topic28.config(state=NORMAL, relief=RAISED)
            topic29.config(state=NORMAL, relief=RAISED)
            v.set(str(currentpage))
        Btn0 = Button(root,text="恢复", padx=8, pady=6, command=page_down)
        Btn0.pack()
        Btn0.place(x=650, y=500)

        root.mainloop()
    topic0_window2 = Button(window2,text='必答题', padx=200, pady=20, command=bida)
    topic0_window2.pack()
    topic0_window2.place(x=0, y=10)
    topic0_window2.config(state=NORMAL)
    topic0_window2 = Button(window2,text='选答题', padx=200, pady=20, command=xuanda)
    topic0_window2.pack()
    topic0_window2.place(x=0, y=80)
    topic0_window2.config(state=NORMAL)
    topic0_window2 = Button(window2,text='风险题', padx=200, pady=20, command=bida)
    topic0_window2.pack()
    topic0_window2.place(x=0, y=150)
    topic0_window2.config(state=NORMAL)
def wajueji():
    window2 = tk.Tk()
    window2.geometry('800x600')
    window2.title('采矿厂2019年安全生产知识竞赛--挖掘机驾驶员')
    def bida():
        root = tk.Tk()
        root.geometry('800x750')
        root.title('采矿厂2019年安全生产知识竞赛--挖掘机驾驶员必答题')
        global currentpage
        global pagecount
        currentpage = 0
        pagecount = 0
        v = StringVar()
        # Label(root, textvariable=v).place(x=20, y=10)
        v.set(str(currentpage))

        def topic0():
            topic0.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：上方', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='1. 挖掘机铲斗不可以从车辆驾驶室哪里通过？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic1():
            topic1.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：信号', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='2. 挖掘机汽笛或警报器应完好。进行各种操作时，均应发出？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic2():
            topic2.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：0.5米。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='3. 装车时铲斗不应压碰汽车车帮，铲斗卸矿高度应不超过多少？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic3():
            topic3.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：立即停止作业并撤离。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='4. 挖掘机作业时，发现悬浮岩块或崩塌征兆、盲炮等情况，应如何操作？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic4():
            topic4.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：翻车。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='5. 挖机将巨大岩块装入车的一端，可能引起什么事故？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic5():
            topic5.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：20米。 ', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='6.  在遇到高压电线断落地面时，导线断落点多少米之内，禁止人员进入？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic6():
            topic6.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：统一指挥。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='7. 什么是应急机制的基础，也是整个应急体系的基础？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic7():
            topic7.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：禁止或停止', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='8. 按照国际通用标准，红色一般表示？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic8():
            topic8.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：注意危险。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='9．按照国际通用标准，黄色表示？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic9():
            topic9.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：安全。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='10.按照国际通用标准，绿色表示？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic10():
            topic10.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：强制执行。 ', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='11. 按照国际通用标准，蓝色表示？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic11():
            topic11.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：潮湿环境。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='12. 什么环境容易发生触电事故？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic12():
            topic12.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：120分贝。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='13.人如果长时间暴露在多少分贝噪声环境中会产生永久性的听力损伤？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic13():
            topic13.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：空斗引车、铲斗不跨越驾驶室作业，否则不作业。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='14.采矿厂保命条款中的装车作业内容是什么？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic14():
            topic14.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：使触电者脱离电源。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='15.有人低压触电时，应先对伤者进行？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic15():
            topic15.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：50米。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='26.同一平台两台挖掘机作业时需保持多少米以上距离？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic16():
            topic16.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：下坡方向。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='17.挖掘机上下坡时，驱动轴应始终处于什么方向？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic17():
            topic17.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：支顶稳固可靠的措施。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='18.必须在铲斗升起时检修车辆，则应对铲斗采取什么措施？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic18():
            topic18.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：挖掘操作。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='19.挖机在回转未终止时，不得进行什么操作？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic19():
            topic19.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：36伏。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='20. 多少伏以下的用电设备可以免装漏电保护器？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        topic0 = Button(root,text='第1题', padx=50, pady=50, command=topic0)
        topic0.pack()
        topic0.place(x=0, y=10)
        topic0.config(state=NORMAL)
        topic1 = Button(root,text='第2题', padx=50, pady=50, command=topic1)
        topic1.pack()
        topic1.place(x=120, y=10)
        topic1.config(state=NORMAL)
        topic2 = Button(root,text='第3题', padx=50, pady=50, command=topic2)
        topic2.pack()
        topic2.place(x=240, y=10)
        topic2.config(state=NORMAL)
        topic3 = Button(root,text='第4题', padx=50, pady=50, command=topic3)
        topic3.pack()
        topic3.place(x=360, y=10)
        topic3.config(state=NORMAL)
        topic4 = Button(root,text='第5题', padx=50, pady=50, command=topic4)
        topic4.pack()
        topic4.place(x=480, y=10)
        topic4.config(state=NORMAL)
        topic5 = Button(root,text='第6题', padx=50, pady=50, command=topic5)
        topic5.pack()
        topic5.place(x=0, y=110)
        topic5.config(state=NORMAL)
        topic6 = Button(root,text='第7题', padx=50, pady=50, command=topic6)
        topic6.pack()
        topic6.place(x=120, y=110)
        topic6.config(state=NORMAL)
        topic7 = Button(root,text='第8题', padx=50, pady=50, command=topic7)
        topic7.pack()
        topic7.place(x=240, y=110)
        topic7.config(state=NORMAL)
        topic8 = Button(root,text='第9题', padx=50, pady=50, command=topic8)
        topic8.pack()
        topic8.place(x=360, y=110)
        topic8.config(state=NORMAL)
        topic9 = Button(root,text='第10题', padx=50, pady=50, command=topic9)
        topic9.pack()
        topic9.place(x=480, y=110)
        topic9.config(state=NORMAL)
        topic10 = Button(root,text='第11题', padx=50, pady=50, command=topic10)
        topic10.pack()
        topic10.place(x=0, y=210)
        topic10.config(state=NORMAL)
        topic11 = Button(root,text='第12题', padx=50, pady=50, command=topic11)
        topic11.pack()
        topic11.place(x=120, y=210)
        topic11.config(state=NORMAL)
        topic12 = Button(root,text='第13题', padx=50, pady=50, command=topic12)
        topic12.pack()
        topic12.place(x=240, y=210)
        topic12.config(state=NORMAL)
        topic13 = Button(root,text='第14题', padx=50, pady=50, command=topic13)
        topic13.pack()
        topic13.place(x=360, y=210)
        topic13.config(state=NORMAL)
        topic14 = Button(root,text='第15题', padx=50, pady=50, command=topic14)
        topic14.pack()
        topic14.place(x=480, y=210)
        topic14.config(state=NORMAL)
        topic15 = Button(root,text='第16题', padx=50, pady=50, command=topic15)
        topic15.pack()
        topic15.place(x=0, y=320)
        topic15.config(state=NORMAL)
        topic16 = Button(root,text='第17题', padx=50, pady=50, command=topic16)
        topic16.pack()
        topic16.place(x=120, y=320)
        topic16.config(state=NORMAL)
        topic17 = Button(root,text='第18题', padx=50, pady=50, command=topic17)
        topic17.pack()
        topic17.place(x=240, y=320)
        topic17.config(state=NORMAL)
        topic18 = Button(root,text='第19题', padx=50, pady=50, command=topic18)
        topic18.pack()
        topic18.place(x=360, y=320)
        topic18.config(state=NORMAL)
        topic19 = Button(root,text='第20题', padx=50, pady=50, command=topic19)
        topic19.pack()
        topic19.place(x=480, y=320)
        topic19.config(state=NORMAL)

        def page_down():
            """
            add 1 to displayed number,
            disable Btn2 button when currentpage reaches pagecount
            """
            global currentpage, pagecount

            currentpage += 1
            topic0.config(state=NORMAL, relief=RAISED)
            topic1.config(state=NORMAL, relief=RAISED)
            topic2.config(state=NORMAL, relief=RAISED)
            topic3.config(state=NORMAL, relief=RAISED)
            topic4.config(state=NORMAL, relief=RAISED)
            topic5.config(state=NORMAL, relief=RAISED)
            topic6.config(state=NORMAL, relief=RAISED)
            topic7.config(state=NORMAL, relief=RAISED)
            topic8.config(state=NORMAL, relief=RAISED)
            topic9.config(state=NORMAL, relief=RAISED)
            topic10.config(state=NORMAL, relief=RAISED)
            topic11.config(state=NORMAL, relief=RAISED)
            topic12.config(state=NORMAL, relief=RAISED)
            topic13.config(state=NORMAL, relief=RAISED)
            topic14.config(state=NORMAL, relief=RAISED)
            topic15.config(state=NORMAL, relief=RAISED)
            topic16.config(state=NORMAL, relief=RAISED)
            topic17.config(state=NORMAL, relief=RAISED)
            topic18.config(state=NORMAL, relief=RAISED)
            topic19.config(state=NORMAL, relief=RAISED)

            v.set(str(currentpage))

        Btn0 = Button(root,text="恢复", padx=8, pady=6, command=page_down)
        Btn0.pack()
        Btn0.place(x=650, y=500)

        root.mainloop()
    def xuanda():
        root = tk.Tk()
        root.geometry('800x750')
        root.title('采矿厂2019年安全生产知识竞赛--挖掘机驾驶员选答题')
        global currentpage
        global pagecount
        currentpage = 0
        pagecount = 0
        v = StringVar()
        # Label(root, textvariable=v).place(x=20, y=10)
        v.set(str(currentpage))

        def topic0():
            topic0.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：防风险、除隐患、遏事故。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='1.2019年全国安全生产月活动的主题是什么？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic1():
            topic1.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：坚持安全第一、预防为主、综合治理。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='2.安全生产工作方针？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic2():
            topic2.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：坚持预防为主、防治结合。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='3.职业病防治工作的方针？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic3():
            topic3.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：应每2年进行1次。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='4.职工的的健康检查频率？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic4():
            topic4.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：检查、确认后启动；不检查、不确认不启动。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='5.采矿厂零伤害条款中设备启动作业是什么？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic5():
            topic5.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：回转半径内无人员、工作帮无危石作业，否则不作业。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='6.采矿厂保命条款中的挖掘作业内容是什么？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic6():
            topic6.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：止血、包扎、固定，送医院。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='7.外伤的急救步骤是什么？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic7():
            topic7.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：一般事故、较大事故、重大事故、特别重大事故。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='8.安全生产事故主要分为哪几个等级？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic8():
            topic8.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：违章作业、违章指挥和违反劳动纪律。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='9.安全生产领域“三违”是指？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic9():
            topic9.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：管行业必须管安全，管业务必须管安全，管生产经营必须管安全。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='10.确定安全生产监督职责的三个“必须”是指？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic10():
            topic10.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：可燃物、助燃物、着火源统称为火灾三要素。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='11.什么是火灾的三要素？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic11():
            topic11.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：边坡滑落、触电、机械伤害、电气火灾。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='12. 铲装作业风险有？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic12():
            topic12.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：适用于中华人民共和国领域内的职业病防治活动。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='13. 职业病防治法的适用范围是什么？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic13():
            topic13.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：主要负责人', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='14. 《安全生产法》中明确生产经营单位的安全生产由谁负责？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic14():
            topic14.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：违反劳动纪律、违反操作程序和冒险、违禁的方法', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='15. 生产经营活动中不安全行为的定义是什么？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic15():
            topic15.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：经专门的安全作业培训，取得特种作业操作资格证书，方可上岗作业。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='16.《安全生产法》对生产经营单位特种作业人员有什么要求？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic16():
            topic16.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：预防、预备、响应和恢复四个阶段', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='17. 事故应急管理包括哪些阶段？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic17():
            topic17.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：12伏。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='18. 在金属容器内、管道内、铁平台上、隧道内、潮湿环境等较恶劣环境中，允许使用的安全电压额定值是多少伏?', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic18():
            topic18.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：办理动火证', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='19. 在非动火区进行动火作业,应该办理什么手续?', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic19():
            topic19.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答案：35℃。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='20.高温天气是指地市级以上气象主管部门所属气象台站向公众发布的日最高气温多少℃以上的天气？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic20():
            topic20.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：80。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='21.我国规定工作地点噪声容许标准为多少分贝？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic21():
            topic21.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：20。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='22.在遇到高压电线断落地面时，导线断落点多少米之内，禁止人员进入？A', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic22():
            topic22.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：二氧化氮和化学需氧量。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='23.节能减排中减排的主要指标有哪些？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic23():
            topic23.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='A.潮湿和下雨的二、三季度。 ', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='24.什么季节容易发生触电事故？A', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic24():
            topic24.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：120', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='25.人如果长时间暴露在（  ）分贝噪声环境中会产生永久性的听力损伤。D', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic25():
            topic25.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：矽肺病。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='26.我国13种法定尘肺病中致病危害最严重的是哪一种？D', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic26():
            topic26.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：诱发事故、伤害自己、伤害他人、传染他人。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='27.习惯性违章行为的危害有？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic27():
            topic27.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：事故原因未查清不放过，责任人未受到处理不放过，整改措施未落实不放过，有关人员未受到教育不放过。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='28.安全生产事故调查中的“四不放过”原则是？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic28():
            topic28.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='指违章作业、违章指挥和违反劳动纪律。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='29.安全生产领域“三违”是?', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic29():
            topic29.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：我不伤害自己、我不伤害别人、我不被别人伤害。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='30.“三不伤害”是?', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic30():
            topic30.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：明火、电能火源、化学火源、炽热物体火源。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='31.着火源分为哪几类？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic31():
            topic31.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答；可燃物、助燃物、火源。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='32.火灾发生时主要表现是燃烧，发生燃烧的三个条件是？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic32():
            topic32.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：32学时。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='33. 生产经营单位主要负责人和安全生产管理人员初次安全培训时间不得少于学时？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic33():
            topic33.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：锤头是否牢固可靠。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='34. 使用手锤作业时应先检查？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic34():
            topic34.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：用人单位承担.', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='35. 劳动者被诊断为职业病的，但用人单位没有依法参加工伤保险，其医疗和生活保障由该由谁承担', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic35():
            topic35.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：撞伤、压伤、轧伤、卷缠等。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='36. 运转中的机械设备对人的伤害主要有？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic36():
            topic36.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：袖口紧、领口紧、下摆紧。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='37. 工人操作机械时穿着工作服的“三紧”是指?', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic37():
            topic37.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：固定式防护装置和活动式防护装置两类。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='38. 常见的防护装置有防护罩、网、屏障、栅栏等形式，可分为哪两种？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic38():
            topic38.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：易燃液体、可燃气体和电气火灾。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='39. 干粉灭火剂适合扑救什么类型火灾？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic39():
            topic39.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：呼吸道、皮肤、消化道三种途径进入体内。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='40. 在工业生产中,毒物主要经过什么途径进入身体？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        topic0 = Button(root,text='第1题', padx=50, pady=20, command=topic0)
        topic0.pack()
        topic0.place(x=0, y=10)
        topic0.config(state=NORMAL)
        topic1 = Button(root,text='第2题', padx=50, pady=20, command=topic1)
        topic1.pack()
        topic1.place(x=120, y=10)
        topic1.config(state=NORMAL)
        topic2 = Button(root,text='第3题', padx=50, pady=20, command=topic2)
        topic2.pack()
        topic2.place(x=240, y=10)
        topic2.config(state=NORMAL)
        topic3 = Button(root,text='第4题', padx=50, pady=20, command=topic3)
        topic3.pack()
        topic3.place(x=360, y=10)
        topic3.config(state=NORMAL)
        topic4 = Button(root,text='第5题', padx=50, pady=20, command=topic4)
        topic4.pack()
        topic4.place(x=480, y=10)
        topic4.config(state=NORMAL)
        topic5 = Button(root,text='第6题', padx=50, pady=20, command=topic5)
        topic5.pack()
        topic5.place(x=0, y=80)
        topic5.config(state=NORMAL)
        topic6 = Button(root,text='第7题', padx=50, pady=20, command=topic6)
        topic6.pack()
        topic6.place(x=120, y=80)
        topic6.config(state=NORMAL)
        topic7 = Button(root,text='第8题', padx=50, pady=20, command=topic7)
        topic7.pack()
        topic7.place(x=240, y=80)
        topic7.config(state=NORMAL)
        topic8 = Button(root,text='第9题', padx=50, pady=20, command=topic8)
        topic8.pack()
        topic8.place(x=360, y=80)
        topic8.config(state=NORMAL)
        topic9 = Button(root,text='第10题', padx=50, pady=20, command=topic9)
        topic9.pack()
        topic9.place(x=480, y=80)
        topic9.config(state=NORMAL)
        topic10 = Button(root,text='第11题', padx=50, pady=20, command=topic10)
        topic10.pack()
        topic10.place(x=0, y=150)
        topic10.config(state=NORMAL)
        topic11 = Button(root,text='第12题', padx=50, pady=20, command=topic11)
        topic11.pack()
        topic11.place(x=120, y=150)
        topic11.config(state=NORMAL)
        topic12 = Button(root,text='第13题', padx=50, pady=20, command=topic12)
        topic12.pack()
        topic12.place(x=240, y=150)
        topic12.config(state=NORMAL)
        topic13 = Button(root,text='第14题', padx=50, pady=20, command=topic13)
        topic13.pack()
        topic13.place(x=360, y=150)
        topic13.config(state=NORMAL)
        topic14 = Button(root,text='第15题', padx=50, pady=20, command=topic14)
        topic14.pack()
        topic14.place(x=480, y=150)
        topic14.config(state=NORMAL)
        topic15 = Button(root,text='第16题', padx=50, pady=20, command=topic15)
        topic15.pack()
        topic15.place(x=0, y=220)
        topic15.config(state=NORMAL)
        topic16 = Button(root,text='第17题', padx=50, pady=20, command=topic16)
        topic16.pack()
        topic16.place(x=120, y=220)
        topic16.config(state=NORMAL)
        topic17 = Button(root,text='第18题', padx=50, pady=20, command=topic17)
        topic17.pack()
        topic17.place(x=240, y=220)
        topic17.config(state=NORMAL)
        topic18 = Button(root,text='第19题', padx=50, pady=20, command=topic18)
        topic18.pack()
        topic18.place(x=360, y=220)
        topic18.config(state=NORMAL)
        topic19 = Button(root,text='第20题', padx=50, pady=20, command=topic19)
        topic19.pack()
        topic19.place(x=480, y=220)
        topic19.config(state=NORMAL)
        topic20 = Button(root,text='第21题', padx=50, pady=20, command=topic20)
        topic20.pack()
        topic20.place(x=0, y=290)
        topic20.config(state=NORMAL)
        topic21 = Button(root,text='第22题', padx=50, pady=20, command=topic21)
        topic21.pack()
        topic21.place(x=120, y=290)
        topic21.config(state=NORMAL)
        topic22 = Button(root,text='第23题', padx=50, pady=20, command=topic22)
        topic22.pack()
        topic22.place(x=240, y=290)
        topic22.config(state=NORMAL)
        topic23 = Button(root,text='第24题', padx=50, pady=20, command=topic23)
        topic23.pack()
        topic23.place(x=360, y=290)
        topic23.config(state=NORMAL)
        topic24 = Button(root,text='第25题', padx=50, pady=20, command=topic24)
        topic24.pack()
        topic24.place(x=480, y=290)
        topic24.config(state=NORMAL)
        topic25 = Button(root,text='第26题', padx=50, pady=20, command=topic25)
        topic25.pack()
        topic25.place(x=0, y=360)
        topic25.config(state=NORMAL)
        topic26 = Button(root,text='第27题', padx=50, pady=20, command=topic26)
        topic26.pack()
        topic26.place(x=120, y=360)
        topic26.config(state=NORMAL)
        topic27 = Button(root,text='第28题', padx=50, pady=20, command=topic27)
        topic27.pack()
        topic27.place(x=240, y=360)
        topic27.config(state=NORMAL)
        topic28 = Button(root,text='第29题', padx=50, pady=20, command=topic28)
        topic28.pack()
        topic28.place(x=360, y=360)
        topic28.config(state=NORMAL)
        topic29 = Button(root,text='第30题', padx=50, pady=20, command=topic29)
        topic29.pack()
        topic29.place(x=480, y=360)
        topic29.config(state=NORMAL)
        topic30 = Button(root,text='第31题', padx=50, pady=20, command=topic30)
        topic30.pack()
        topic30.place(x=0, y=430)
        topic30.config(state=NORMAL)
        topic31 = Button(root,text='第32题', padx=50, pady=20, command=topic31)
        topic31.pack()
        topic31.place(x=120, y=430)
        topic31.config(state=NORMAL)
        topic32 = Button(root,text='第33题', padx=50, pady=20, command=topic32)
        topic32.pack()
        topic32.place(x=240, y=430)
        topic32.config(state=NORMAL)
        topic33 = Button(root,text='第34题', padx=50, pady=20, command=topic33)
        topic33.pack()
        topic33.place(x=360, y=430)
        topic33.config(state=NORMAL)
        topic34 = Button(root,text='第35题', padx=50, pady=20, command=topic34)
        topic34.pack()
        topic34.place(x=480, y=430)
        topic34.config(state=NORMAL)
        topic35 = Button(root,text='第36题', padx=50, pady=20, command=topic35)
        topic35.pack()
        topic35.place(x=0, y=500)
        topic35.config(state=NORMAL)
        topic36 = Button(root,text='第37题', padx=50, pady=20, command=topic36)
        topic36.pack()
        topic36.place(x=120, y=500)
        topic36.config(state=NORMAL)
        topic37 = Button(root,text='第38题', padx=50, pady=20, command=topic37)
        topic37.pack()
        topic37.place(x=240, y=500)
        topic37.config(state=NORMAL)
        topic38 = Button(root,text='第39题', padx=50, pady=20, command=topic38)
        topic38.pack()
        topic38.place(x=360, y=500)
        topic38.config(state=NORMAL)
        topic39 = Button(root,text='第40题', padx=50, pady=20, command=topic39)
        topic39.pack()
        topic39.place(x=480, y=500)
        topic39.config(state=NORMAL)

        def page_down():
            """
            add 1 to displayed number,
            disable Btn2 button when currentpage reaches pagecount
            """
            global currentpage, pagecount

            currentpage += 1
            topic0.config(state=NORMAL, relief=RAISED)
            topic1.config(state=NORMAL, relief=RAISED)
            topic2.config(state=NORMAL, relief=RAISED)
            topic3.config(state=NORMAL, relief=RAISED)
            topic4.config(state=NORMAL, relief=RAISED)
            topic5.config(state=NORMAL, relief=RAISED)
            topic6.config(state=NORMAL, relief=RAISED)
            topic7.config(state=NORMAL, relief=RAISED)
            topic8.config(state=NORMAL, relief=RAISED)
            topic9.config(state=NORMAL, relief=RAISED)
            topic10.config(state=NORMAL, relief=RAISED)
            topic11.config(state=NORMAL, relief=RAISED)
            topic12.config(state=NORMAL, relief=RAISED)
            topic13.config(state=NORMAL, relief=RAISED)
            topic14.config(state=NORMAL, relief=RAISED)
            topic15.config(state=NORMAL, relief=RAISED)
            topic16.config(state=NORMAL, relief=RAISED)
            topic17.config(state=NORMAL, relief=RAISED)
            topic18.config(state=NORMAL, relief=RAISED)
            topic19.config(state=NORMAL, relief=RAISED)
            topic20.config(state=NORMAL, relief=RAISED)
            topic21.config(state=NORMAL, relief=RAISED)
            topic22.config(state=NORMAL, relief=RAISED)
            topic23.config(state=NORMAL, relief=RAISED)
            topic24.config(state=NORMAL, relief=RAISED)
            topic25.config(state=NORMAL, relief=RAISED)
            topic26.config(state=NORMAL, relief=RAISED)
            topic27.config(state=NORMAL, relief=RAISED)
            topic28.config(state=NORMAL, relief=RAISED)
            topic29.config(state=NORMAL, relief=RAISED)
            topic30.config(state=NORMAL, relief=RAISED)
            topic31.config(state=NORMAL, relief=RAISED)
            topic32.config(state=NORMAL, relief=RAISED)
            topic33.config(state=NORMAL, relief=RAISED)
            topic34.config(state=NORMAL, relief=RAISED)
            topic35.config(state=NORMAL, relief=RAISED)
            topic36.config(state=NORMAL, relief=RAISED)
            topic37.config(state=NORMAL, relief=RAISED)
            topic38.config(state=NORMAL, relief=RAISED)
            topic39.config(state=NORMAL, relief=RAISED)

            v.set(str(currentpage))

        Btn0 = Button(root,text="恢复", padx=8, pady=6, command=page_down)
        Btn0.pack()
        Btn0.place(x=650, y=500)

        root.mainloop()
    topic0_window2 = Button(window2,text='必答题', padx=200, pady=20, command=bida)
    topic0_window2.pack()
    topic0_window2.place(x=0, y=10)
    topic0_window2.config(state=NORMAL)
    topic0_window2 = Button(window2,text='选答题', padx=200, pady=20, command=xuanda)
    topic0_window2.pack()
    topic0_window2.place(x=0, y=80)
    topic0_window2.config(state=NORMAL)
    topic0_window2 = Button(window2,text='风险题', padx=200, pady=20, command=bida)
    topic0_window2.pack()
    topic0_window2.place(x=0, y=150)
    topic0_window2.config(state=NORMAL)
def zixieche():
    window2 = tk.Tk()
    window2.geometry('800x600')
    window2.title('采矿厂2019年安全生产知识竞赛--自卸车驾驶员')
    def bida():
        root = tk.Tk()
        root.geometry('800x750')
        root.title('采矿厂2019年安全生产知识竞赛--自卸车驾驶员')
        global currentpage
        global pagecount
        currentpage = 0
        pagecount = 0
        v = StringVar()
        # Label(root, textvariable=v).place(x=20, y=10)
        v.set(str(currentpage))

        def topic0():
            topic0.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：靠右暂停行驶，并不得熄灭车前、车后的警示灯。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='雾天和烟尘弥漫影响能见度时，视距不足20米时，应怎么做？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic1():
            topic1.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：每小时三十公里。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='采场内限行车限速每小时多少公里？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic2():
            topic2.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：轮胎直径的一半。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='排土场规定挡墙高度是多少？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic3():
            topic3.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：2%-5%。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='排土场规定反坡是多少？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic4():
            topic4.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：启动前要预热至少20秒', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='寒冷天气对车辆运行前有什么要求？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic5():
            topic5.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：需要', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='检查传动油是否需要启动发动机？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic6():
            topic6.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：超过2米属于高空作业；', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='平台作业超过几米属于高空作业？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic7():
            topic7.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：三违是违章指挥、违章作业和违反劳动纪律；', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='请具体阐述安全生产领域“三违”指什么？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic8():
            topic8.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：帽壳、帽衬、下领带。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='安全帽由哪几部分组成？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic9():
            topic9.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：空档滑行。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='禁止采用溜车方式发动车辆，下坡行驶严禁什么驾驶方式。', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic10():
            topic10.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：转弯处，坡道，同类型车。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='什么情况禁止超车？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic11():
            topic11.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：40米。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='冰雪或多雨季节道路较滑时，应有防滑措施并减速行驶；前后车距应不小于多少米？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic12():
            topic12.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：20米。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='视距不足多少米时，应靠右暂停行驶，并不应熄灭车前、车后的警示灯？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic13():
            topic13.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：减速嘹望，确认安全方可通过。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='车辆通过道口之前，驾驶员应如何操作？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic14():
            topic14.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：不应检查、维护车辆。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='装车时，驾驶员不应离开驾驶室，还不应做什么？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic15():
            topic15.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：应每2年进行1次。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='职工的的健康检查频率？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic16():
            topic16.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：18周岁', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='17 特种作业人员应当年多少岁？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic17():
            topic17.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：初中及以上文化程度。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='18 特种作业人员具有什么程度的文化水平？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic18():
            topic18.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：6年。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='19 特种作业操作证有效期为？。', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic19():
            topic19.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：每3年。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='20 特种作业操作证多久复审1次？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        topic0 = Button(root,text='第1题', padx=50, pady=50, command=topic0)
        topic0.pack()
        topic0.place(x=0, y=10)
        topic0.config(state=NORMAL)
        topic1 = Button(root,text='第2题', padx=50, pady=50, command=topic1)
        topic1.pack()
        topic1.place(x=120, y=10)
        topic1.config(state=NORMAL)
        topic2 = Button(root,text='第3题', padx=50, pady=50, command=topic2)
        topic2.pack()
        topic2.place(x=240, y=10)
        topic2.config(state=NORMAL)
        topic3 = Button(root,text='第4题', padx=50, pady=50, command=topic3)
        topic3.pack()
        topic3.place(x=360, y=10)
        topic3.config(state=NORMAL)
        topic4 = Button(root,text='第5题', padx=50, pady=50, command=topic4)
        topic4.pack()
        topic4.place(x=480, y=10)
        topic4.config(state=NORMAL)
        topic5 = Button(root,text='第6题', padx=50, pady=50, command=topic5)
        topic5.pack()
        topic5.place(x=0, y=110)
        topic5.config(state=NORMAL)
        topic6 = Button(root,text='第7题', padx=50, pady=50, command=topic6)
        topic6.pack()
        topic6.place(x=120, y=110)
        topic6.config(state=NORMAL)
        topic7 = Button(root,text='第8题', padx=50, pady=50, command=topic7)
        topic7.pack()
        topic7.place(x=240, y=110)
        topic7.config(state=NORMAL)
        topic8 = Button(root,text='第9题', padx=50, pady=50, command=topic8)
        topic8.pack()
        topic8.place(x=360, y=110)
        topic8.config(state=NORMAL)
        topic9 = Button(root,text='第10题', padx=50, pady=50, command=topic9)
        topic9.pack()
        topic9.place(x=480, y=110)
        topic9.config(state=NORMAL)
        topic10 = Button(root,text='第11题', padx=50, pady=50, command=topic10)
        topic10.pack()
        topic10.place(x=0, y=210)
        topic10.config(state=NORMAL)
        topic11 = Button(root,text='第12题', padx=50, pady=50, command=topic11)
        topic11.pack()
        topic11.place(x=120, y=210)
        topic11.config(state=NORMAL)
        topic12 = Button(root,text='第13题', padx=50, pady=50, command=topic12)
        topic12.pack()
        topic12.place(x=240, y=210)
        topic12.config(state=NORMAL)
        topic13 = Button(root,text='第14题', padx=50, pady=50, command=topic13)
        topic13.pack()
        topic13.place(x=360, y=210)
        topic13.config(state=NORMAL)
        topic14 = Button(root,text='第15题', padx=50, pady=50, command=topic14)
        topic14.pack()
        topic14.place(x=480, y=210)
        topic14.config(state=NORMAL)
        topic15 = Button(root,text='第16题', padx=50, pady=50, command=topic15)
        topic15.pack()
        topic15.place(x=0, y=320)
        topic15.config(state=NORMAL)
        topic16 = Button(root,text='第17题', padx=50, pady=50, command=topic16)
        topic16.pack()
        topic16.place(x=120, y=320)
        topic16.config(state=NORMAL)
        topic17 = Button(root,text='第18题', padx=50, pady=50, command=topic17)
        topic17.pack()
        topic17.place(x=240, y=320)
        topic17.config(state=NORMAL)
        topic18 = Button(root,text='第19题', padx=50, pady=50, command=topic18)
        topic18.pack()
        topic18.place(x=360, y=320)
        topic18.config(state=NORMAL)
        topic19 = Button(root,text='第20题', padx=50, pady=50, command=topic19)
        topic19.pack()
        topic19.place(x=480, y=320)
        topic19.config(state=NORMAL)

        def page_down():
            """
            add 1 to displayed number,
            disable Btn2 button when currentpage reaches pagecount
            """
            global currentpage, pagecount

            currentpage += 1
            topic0.config(state=NORMAL, relief=RAISED)
            topic1.config(state=NORMAL, relief=RAISED)
            topic2.config(state=NORMAL, relief=RAISED)
            topic3.config(state=NORMAL, relief=RAISED)
            topic4.config(state=NORMAL, relief=RAISED)
            topic5.config(state=NORMAL, relief=RAISED)
            topic6.config(state=NORMAL, relief=RAISED)
            topic7.config(state=NORMAL, relief=RAISED)
            topic8.config(state=NORMAL, relief=RAISED)
            topic9.config(state=NORMAL, relief=RAISED)
            topic10.config(state=NORMAL, relief=RAISED)
            topic11.config(state=NORMAL, relief=RAISED)
            topic12.config(state=NORMAL, relief=RAISED)
            topic13.config(state=NORMAL, relief=RAISED)
            topic14.config(state=NORMAL, relief=RAISED)
            topic15.config(state=NORMAL, relief=RAISED)
            topic16.config(state=NORMAL, relief=RAISED)
            topic17.config(state=NORMAL, relief=RAISED)
            topic18.config(state=NORMAL, relief=RAISED)
            topic19.config(state=NORMAL, relief=RAISED)

            v.set(str(currentpage))

        Btn0 = Button(root,text="恢复", padx=8, pady=6, command=page_down)
        Btn0.pack()
        Btn0.place(x=650, y=500)

        root.mainloop()
    def xuanda():
        root = tk.Tk()
        root.geometry('800x750')
        root.title('采矿厂2019年安全生产知识竞赛--自卸车驾驶员选答题')
        global currentpage
        global pagecount
        currentpage = 0
        pagecount = 0
        v = StringVar()
        # Label(root, textvariable=v).place(x=20, y=10)
        v.set(str(currentpage))

        def topic0():
            topic0.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：防风险、除隐患、遏事故。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='1.2019年全国安全生产月活动的主题是什么？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic1():
            topic1.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：坚持安全第一、预防为主、综合治理。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='2.安全生产工作方针？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic2():
            topic2.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：坚持预防为主、防治结合。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='3.职业病防治工作的方针？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic3():
            topic3.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：应每2年进行1次。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='4.职工的的健康检查频率？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic4():
            topic4.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：检查、确认后启动；不检查、不确认不启动。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='5.采矿厂零伤害条款中设备启动作业是什么？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic5():
            topic5.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：回转半径内无人员、工作帮无危石作业，否则不作业。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='6.采矿厂保命条款中的挖掘作业内容是什么？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic6():
            topic6.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：止血、包扎、固定，送医院。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='7.外伤的急救步骤是什么？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic7():
            topic7.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：一般事故、较大事故、重大事故、特别重大事故。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='8.安全生产事故主要分为哪几个等级？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic8():
            topic8.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：违章作业、违章指挥和违反劳动纪律。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='9.安全生产领域“三违”是指？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic9():
            topic9.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：管行业必须管安全，管业务必须管安全，管生产经营必须管安全。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='10.确定安全生产监督职责的三个“必须”是指？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic10():
            topic10.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：可燃物、助燃物、着火源统称为火灾三要素。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='11.什么是火灾的三要素？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic11():
            topic11.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：边坡滑落、触电、机械伤害、电气火灾。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='12. 铲装作业风险有？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic12():
            topic12.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：适用于中华人民共和国领域内的职业病防治活动。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='13. 职业病防治法的适用范围是什么？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic13():
            topic13.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：主要负责人', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='14. 《安全生产法》中明确生产经营单位的安全生产由谁负责？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic14():
            topic14.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：违反劳动纪律、违反操作程序和冒险、违禁的方法', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='15. 生产经营活动中不安全行为的定义是什么？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic15():
            topic15.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：经专门的安全作业培训，取得特种作业操作资格证书，方可上岗作业。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='16.《安全生产法》对生产经营单位特种作业人员有什么要求？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic16():
            topic16.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：预防、预备、响应和恢复四个阶段', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='17. 事故应急管理包括哪些阶段？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic17():
            topic17.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：12伏。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='18. 在金属容器内、管道内、铁平台上、隧道内、潮湿环境等较恶劣环境中，允许使用的安全电压额定值是多少伏?', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic18():
            topic18.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：办理动火证', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='19. 在非动火区进行动火作业,应该办理什么手续?', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic19():
            topic19.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答案：35℃。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='20.高温天气是指地市级以上气象主管部门所属气象台站向公众发布的日最高气温多少℃以上的天气？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic20():
            topic20.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：80。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='21.我国规定工作地点噪声容许标准为多少分贝？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic21():
            topic21.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：20。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='22.在遇到高压电线断落地面时，导线断落点多少米之内，禁止人员进入？A', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic22():
            topic22.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：二氧化氮和化学需氧量。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='23.节能减排中减排的主要指标有哪些？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic23():
            topic23.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='A.潮湿和下雨的二、三季度。 ', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='24.什么季节容易发生触电事故？A', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic24():
            topic24.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：120', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='25.人如果长时间暴露在（  ）分贝噪声环境中会产生永久性的听力损伤。D', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic25():
            topic25.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：矽肺病。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='26.我国13种法定尘肺病中致病危害最严重的是哪一种？D', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic26():
            topic26.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：诱发事故、伤害自己、伤害他人、传染他人。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='27.习惯性违章行为的危害有？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic27():
            topic27.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：事故原因未查清不放过，责任人未受到处理不放过，整改措施未落实不放过，有关人员未受到教育不放过。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='28.安全生产事故调查中的“四不放过”原则是？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic28():
            topic28.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='指违章作业、违章指挥和违反劳动纪律。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='29.安全生产领域“三违”是?', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic29():
            topic29.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：我不伤害自己、我不伤害别人、我不被别人伤害。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='30.“三不伤害”是?', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic30():
            topic30.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：明火、电能火源、化学火源、炽热物体火源。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='31.着火源分为哪几类？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic31():
            topic31.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答；可燃物、助燃物、火源。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='32.火灾发生时主要表现是燃烧，发生燃烧的三个条件是？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic32():
            topic32.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：32学时。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='33. 生产经营单位主要负责人和安全生产管理人员初次安全培训时间不得少于学时？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic33():
            topic33.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：锤头是否牢固可靠。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='34. 使用手锤作业时应先检查？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic34():
            topic34.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：用人单位承担.', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='35. 劳动者被诊断为职业病的，但用人单位没有依法参加工伤保险，其医疗和生活保障由该由谁承担', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic35():
            topic35.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：撞伤、压伤、轧伤、卷缠等。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='36. 运转中的机械设备对人的伤害主要有？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic36():
            topic36.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：袖口紧、领口紧、下摆紧。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='37. 工人操作机械时穿着工作服的“三紧”是指?', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic37():
            topic37.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：固定式防护装置和活动式防护装置两类。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='38. 常见的防护装置有防护罩、网、屏障、栅栏等形式，可分为哪两种？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic38():
            topic38.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：易燃液体、可燃气体和电气火灾。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='39. 干粉灭火剂适合扑救什么类型火灾？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        def topic39():
            topic39.config(state=DISABLED, relief='sunken')
            # 替换1
            global currentpage, pagecount

            # 替换1
            def answer():
                tk.Label(window, text='答：呼吸道、皮肤、消化道三种途径进入体内。', ).place(x=50, y=350)
                # 替换2
                pygame.mixer.music.stop()

            window = tk.Tk()
            window.title('题目')
            window.geometry('700x700')
            if Btn0["state"] != "normal":
                Btn0.config(state=NORMAL)  # button to page down is enabled
            v.set(str(currentpage))
            track = pygame.mixer.music.load('countdown_first.wav')
            pygame.mixer.music.play()
            # 替换2
            tk.Label(window, text='40. 在工业生产中,毒物主要经过什么途径进入身体？', ).place(x=50, y=50)
            # 替换3
            tk.Label(window, text='答题时间:', ).place(x=50, y=500)
            canvas = tk.Canvas(window, width=465, height=22, bg="white")
            canvas.place(x=110, y=500)
            fill_line = canvas.create_rectangle(1.5, 1.5, 0, 23, width=0, fill="green")
            x = 465  # 未知变量，可更改
            n = 465 / x  # 465是矩形填充满的次数
            topic_window = Button(window, text='显示答案', padx=25, pady=15, command=answer)
            topic_window.pack()
            topic_window.place(x=300, y=550)
            for i in range(x):
                if i < 460:
                    n = n + 465 / x
                    canvas.coords(fill_line, (0, 0, n, 60))
                    window.update()
                    time.sleep(0.035)  # 控制进度条流动的速度
                else:
                    tk.Label(window, text='答题时间到！', ).place(x=300, y=450)

            for t in range(x):
                n = n + 465 / x
                # 以矩形的长度作为变量值更新
                canvas.coords(fill_line, (0, 0, n, 60))
                window.update()
                time.sleep(0)

        # 替换3
        topic0 = Button(root,text='第1题', padx=50, pady=20, command=topic0)
        topic0.pack()
        topic0.place(x=0, y=10)
        topic0.config(state=NORMAL)
        topic1 = Button(root,text='第2题', padx=50, pady=20, command=topic1)
        topic1.pack()
        topic1.place(x=120, y=10)
        topic1.config(state=NORMAL)
        topic2 = Button(root,text='第3题', padx=50, pady=20, command=topic2)
        topic2.pack()
        topic2.place(x=240, y=10)
        topic2.config(state=NORMAL)
        topic3 = Button(root,text='第4题', padx=50, pady=20, command=topic3)
        topic3.pack()
        topic3.place(x=360, y=10)
        topic3.config(state=NORMAL)
        topic4 = Button(root,text='第5题', padx=50, pady=20, command=topic4)
        topic4.pack()
        topic4.place(x=480, y=10)
        topic4.config(state=NORMAL)
        topic5 = Button(root,text='第6题', padx=50, pady=20, command=topic5)
        topic5.pack()
        topic5.place(x=0, y=80)
        topic5.config(state=NORMAL)
        topic6 = Button(root,text='第7题', padx=50, pady=20, command=topic6)
        topic6.pack()
        topic6.place(x=120, y=80)
        topic6.config(state=NORMAL)
        topic7 = Button(root,text='第8题', padx=50, pady=20, command=topic7)
        topic7.pack()
        topic7.place(x=240, y=80)
        topic7.config(state=NORMAL)
        topic8 = Button(root,text='第9题', padx=50, pady=20, command=topic8)
        topic8.pack()
        topic8.place(x=360, y=80)
        topic8.config(state=NORMAL)
        topic9 = Button(root,text='第10题', padx=50, pady=20, command=topic9)
        topic9.pack()
        topic9.place(x=480, y=80)
        topic9.config(state=NORMAL)
        topic10 = Button(root,text='第11题', padx=50, pady=20, command=topic10)
        topic10.pack()
        topic10.place(x=0, y=150)
        topic10.config(state=NORMAL)
        topic11 = Button(root,text='第12题', padx=50, pady=20, command=topic11)
        topic11.pack()
        topic11.place(x=120, y=150)
        topic11.config(state=NORMAL)
        topic12 = Button(root,text='第13题', padx=50, pady=20, command=topic12)
        topic12.pack()
        topic12.place(x=240, y=150)
        topic12.config(state=NORMAL)
        topic13 = Button(root,text='第14题', padx=50, pady=20, command=topic13)
        topic13.pack()
        topic13.place(x=360, y=150)
        topic13.config(state=NORMAL)
        topic14 = Button(root,text='第15题', padx=50, pady=20, command=topic14)
        topic14.pack()
        topic14.place(x=480, y=150)
        topic14.config(state=NORMAL)
        topic15 = Button(root,text='第16题', padx=50, pady=20, command=topic15)
        topic15.pack()
        topic15.place(x=0, y=220)
        topic15.config(state=NORMAL)
        topic16 = Button(root,text='第17题', padx=50, pady=20, command=topic16)
        topic16.pack()
        topic16.place(x=120, y=220)
        topic16.config(state=NORMAL)
        topic17 = Button(root,text='第18题', padx=50, pady=20, command=topic17)
        topic17.pack()
        topic17.place(x=240, y=220)
        topic17.config(state=NORMAL)
        topic18 = Button(root,text='第19题', padx=50, pady=20, command=topic18)
        topic18.pack()
        topic18.place(x=360, y=220)
        topic18.config(state=NORMAL)
        topic19 = Button(root,text='第20题', padx=50, pady=20, command=topic19)
        topic19.pack()
        topic19.place(x=480, y=220)
        topic19.config(state=NORMAL)
        topic20 = Button(root,text='第21题', padx=50, pady=20, command=topic20)
        topic20.pack()
        topic20.place(x=0, y=290)
        topic20.config(state=NORMAL)
        topic21 = Button(root,text='第22题', padx=50, pady=20, command=topic21)
        topic21.pack()
        topic21.place(x=120, y=290)
        topic21.config(state=NORMAL)
        topic22 = Button(root,text='第23题', padx=50, pady=20, command=topic22)
        topic22.pack()
        topic22.place(x=240, y=290)
        topic22.config(state=NORMAL)
        topic23 = Button(root,text='第24题', padx=50, pady=20, command=topic23)
        topic23.pack()
        topic23.place(x=360, y=290)
        topic23.config(state=NORMAL)
        topic24 = Button(root,text='第25题', padx=50, pady=20, command=topic24)
        topic24.pack()
        topic24.place(x=480, y=290)
        topic24.config(state=NORMAL)
        topic25 = Button(root,text='第26题', padx=50, pady=20, command=topic25)
        topic25.pack()
        topic25.place(x=0, y=360)
        topic25.config(state=NORMAL)
        topic26 = Button(root,text='第27题', padx=50, pady=20, command=topic26)
        topic26.pack()
        topic26.place(x=120, y=360)
        topic26.config(state=NORMAL)
        topic27 = Button(root,text='第28题', padx=50, pady=20, command=topic27)
        topic27.pack()
        topic27.place(x=240, y=360)
        topic27.config(state=NORMAL)
        topic28 = Button(root,text='第29题', padx=50, pady=20, command=topic28)
        topic28.pack()
        topic28.place(x=360, y=360)
        topic28.config(state=NORMAL)
        topic29 = Button(root,text='第30题', padx=50, pady=20, command=topic29)
        topic29.pack()
        topic29.place(x=480, y=360)
        topic29.config(state=NORMAL)
        topic30 = Button(root,text='第31题', padx=50, pady=20, command=topic30)
        topic30.pack()
        topic30.place(x=0, y=430)
        topic30.config(state=NORMAL)
        topic31 = Button(root,text='第32题', padx=50, pady=20, command=topic31)
        topic31.pack()
        topic31.place(x=120, y=430)
        topic31.config(state=NORMAL)
        topic32 = Button(root,text='第33题', padx=50, pady=20, command=topic32)
        topic32.pack()
        topic32.place(x=240, y=430)
        topic32.config(state=NORMAL)
        topic33 = Button(root,text='第34题', padx=50, pady=20, command=topic33)
        topic33.pack()
        topic33.place(x=360, y=430)
        topic33.config(state=NORMAL)
        topic34 = Button(root,text='第35题', padx=50, pady=20, command=topic34)
        topic34.pack()
        topic34.place(x=480, y=430)
        topic34.config(state=NORMAL)
        topic35 = Button(root,text='第36题', padx=50, pady=20, command=topic35)
        topic35.pack()
        topic35.place(x=0, y=500)
        topic35.config(state=NORMAL)
        topic36 = Button(root,text='第37题', padx=50, pady=20, command=topic36)
        topic36.pack()
        topic36.place(x=120, y=500)
        topic36.config(state=NORMAL)
        topic37 = Button(root,text='第38题', padx=50, pady=20, command=topic37)
        topic37.pack()
        topic37.place(x=240, y=500)
        topic37.config(state=NORMAL)
        topic38 = Button(root,text='第39题', padx=50, pady=20, command=topic38)
        topic38.pack()
        topic38.place(x=360, y=500)
        topic38.config(state=NORMAL)
        topic39 = Button(root,text='第40题', padx=50, pady=20, command=topic39)
        topic39.pack()
        topic39.place(x=480, y=500)
        topic39.config(state=NORMAL)

        def page_down():
            """
            add 1 to displayed number,
            disable Btn2 button when currentpage reaches pagecount
            """
            global currentpage, pagecount

            currentpage += 1
            topic0.config(state=NORMAL, relief=RAISED)
            topic1.config(state=NORMAL, relief=RAISED)
            topic2.config(state=NORMAL, relief=RAISED)
            topic3.config(state=NORMAL, relief=RAISED)
            topic4.config(state=NORMAL, relief=RAISED)
            topic5.config(state=NORMAL, relief=RAISED)
            topic6.config(state=NORMAL, relief=RAISED)
            topic7.config(state=NORMAL, relief=RAISED)
            topic8.config(state=NORMAL, relief=RAISED)
            topic9.config(state=NORMAL, relief=RAISED)
            topic10.config(state=NORMAL, relief=RAISED)
            topic11.config(state=NORMAL, relief=RAISED)
            topic12.config(state=NORMAL, relief=RAISED)
            topic13.config(state=NORMAL, relief=RAISED)
            topic14.config(state=NORMAL, relief=RAISED)
            topic15.config(state=NORMAL, relief=RAISED)
            topic16.config(state=NORMAL, relief=RAISED)
            topic17.config(state=NORMAL, relief=RAISED)
            topic18.config(state=NORMAL, relief=RAISED)
            topic19.config(state=NORMAL, relief=RAISED)
            topic20.config(state=NORMAL, relief=RAISED)
            topic21.config(state=NORMAL, relief=RAISED)
            topic22.config(state=NORMAL, relief=RAISED)
            topic23.config(state=NORMAL, relief=RAISED)
            topic24.config(state=NORMAL, relief=RAISED)
            topic25.config(state=NORMAL, relief=RAISED)
            topic26.config(state=NORMAL, relief=RAISED)
            topic27.config(state=NORMAL, relief=RAISED)
            topic28.config(state=NORMAL, relief=RAISED)
            topic29.config(state=NORMAL, relief=RAISED)
            topic30.config(state=NORMAL, relief=RAISED)
            topic31.config(state=NORMAL, relief=RAISED)
            topic32.config(state=NORMAL, relief=RAISED)
            topic33.config(state=NORMAL, relief=RAISED)
            topic34.config(state=NORMAL, relief=RAISED)
            topic35.config(state=NORMAL, relief=RAISED)
            topic36.config(state=NORMAL, relief=RAISED)
            topic37.config(state=NORMAL, relief=RAISED)
            topic38.config(state=NORMAL, relief=RAISED)
            topic39.config(state=NORMAL, relief=RAISED)

            v.set(str(currentpage))

        Btn0 = Button(root,text="恢复", padx=8, pady=6, command=page_down)
        Btn0.pack()
        Btn0.place(x=650, y=500)

        root.mainloop()
    topic0_window2 = Button(window2,text='必答题', padx=200, pady=20, command=bida)
    topic0_window2.pack()
    topic0_window2.place(x=0, y=10)
    topic0_window2.config(state=NORMAL)
    topic0_window2 = Button(window2,text='选答题', padx=200, pady=20, command=xuanda)
    topic0_window2.pack()
    topic0_window2.place(x=0, y=80)
    topic0_window2.config(state=NORMAL)
    topic0_window2 = Button(window2,text='风险题', padx=200, pady=20, command=bida)
    topic0_window2.pack()
    topic0_window2.place(x=0, y=150)
    topic0_window2.config(state=NORMAL)
window1 = tk.Tk()
window1.geometry('800x600')
window1.title('采矿厂2019年安全生产知识竞赛')
topic0_window1=Button(text='安全',padx=200,pady=20,command=anquan)
topic0_window1.pack()
topic0_window1.place(x=0,y=10)
topic0_window1.config(state=NORMAL)
topic0_window1=Button(text='爆破员',padx=193,pady=20,command=baopo)
topic0_window1.pack()
topic0_window1.place(x=0,y=80)
topic0_window1.config(state=NORMAL)
topic0_window1=Button(text='挖掘机驾驶员',padx=175,pady=20,command=wajueji)
topic0_window1.pack()
topic0_window1.place(x=0,y=150)
topic0_window1.config(state=NORMAL)
topic0_window1=Button(text='自卸车驾驶员',padx=175,pady=20,command=zixieche)
topic0_window1.pack()
topic0_window1.place(x=0,y=220)
topic0_window1.config(state=NORMAL)
window1.mainloop()
