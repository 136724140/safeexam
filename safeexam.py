from tkinter import *
from tkinter import messagebox

root = Tk()

root.geometry('300x300+20+20')

global currentpage
global pagecount
currentpage = 0
pagecount = 0

v = StringVar()
#Label(root, textvariable=v).place(x=20, y=10)
v.set(str(currentpage))


def topic0():
    global currentpage, pagecount
    topic0.config(state=DISABLED,relief = 'sunken')
    tc3 = messagebox.showinfo(title='必答题第1题',message ='1．炸药在爆炸过程中内能转变为？')
    if tc3 == 'ok':
        tc4 = messagebox.showinfo(title='答案',message= '答：机械能、光能和热能等并对外界做功。')
    if Btn0["state"] != "normal":
        Btn0.config(state=NORMAL)  # button to page down is enabled
    v.set(str(currentpage))
def topic1():
    global currentpage, pagecount
    topic1.config(state=DISABLED,relief = 'sunken')
    tc3 = messagebox.showinfo(title='必答题第2题',message ='2．从广义上讲，爆炸可分为？')
    if tc3 == 'ok':
        tc4 = messagebox.showinfo(title='答案',message= '答：物理爆炸、化学爆炸和核爆炸。')
    if Btn0["state"] != "normal":
        Btn0.config(state=NORMAL)  # button to page down is enabled
    v.set(str(currentpage))
def topic2():
    global currentpage, pagecount
    topic2.config(state=DISABLED,relief = 'sunken')
    tc3 = messagebox.showinfo(title='必答题第3题',message ='3．物理爆炸的特征是？')
    if tc3 == 'ok':
        tc4 = messagebox.showinfo(title='答案',message= '答：爆炸时物质的形态发生变化而化学成分不发生改变。')
    if Btn0["state"] != "normal":
        Btn0.config(state=NORMAL)  # button to page down is enabled
    v.set(str(currentpage))
def topic3():
    global currentpage, pagecount
    topic3.config(state=DISABLED,relief = 'sunken')
    tc3 = messagebox.showinfo(title='必答题第4题',message ='4．化学爆炸的特点是？')
    if tc3 == 'ok':
        tc4 = messagebox.showinfo(title='答案',message= '答：在爆炸变化过程中生成新的物质。')
    if Btn0["state"] != "normal":
        Btn0.config(state=NORMAL)  # button to page down is enabled
    v.set(str(currentpage))
def topic4():
    global currentpage, pagecount
    topic4.config(state=DISABLED,relief = 'sunken')
    tc3 = messagebox.showinfo(title='必答题第5题',message ='5．炸药化学变化的三种形式包括？')
    if tc3 == 'ok':
        tc4 = messagebox.showinfo(title='答案',message= '答：炸药的热分解、燃烧和爆轰。')
    if Btn0["state"] != "normal":
        Btn0.config(state=NORMAL)  # button to page down is enabled
    v.set(str(currentpage))
def topic5():
    global currentpage, pagecount
    topic5.config(state=DISABLED,relief = 'sunken')
    tc3 = messagebox.showinfo(title='必答题第6题',message ='6．炸药的燃烧是依靠？')
    if tc3 == 'ok':
        tc4 = messagebox.showinfo(title='答案',message= '答：自身所含的氧进行反应的。')
    if Btn0["state"] != "normal":
        Btn0.config(state=NORMAL)  # button to page down is enabled
    v.set(str(currentpage))
def topic6():
    global currentpage, pagecount
    topic6.config(state=DISABLED,relief = 'sunken')
    tc3 = messagebox.showinfo(title='必答题第7题',message ='7．根据燃烧过程中燃烧速度的变化，炸药的燃烧可分为？')
    if tc3 == 'ok':
        tc4 = messagebox.showinfo(title='答案',message= '答：稳定燃烧和不稳定燃烧。')
    if Btn0["state"] != "normal":
        Btn0.config(state=NORMAL)  # button to page down is enabled
    v.set(str(currentpage))
def topic7():
    global currentpage, pagecount
    topic7.config(state=DISABLED,relief = 'sunken')
    tc3 = messagebox.showinfo(title='必答题第8题',message ='8．爆速的含义？')
    if tc3 == 'ok':
        tc4 = messagebox.showinfo(title='答案',message= '答：爆速是爆轰波在炸药中传播的速度。')
    if Btn0["state"] != "normal":
        Btn0.config(state=NORMAL)  # button to page down is enabled
    v.set(str(currentpage))
def topic8():
    global currentpage, pagecount
    topic8.config(state=DISABLED,relief = 'sunken')
    tc3 = messagebox.showinfo(title='必答题第9题',message ='9．爆热的含义？')
    if tc3 == 'ok':
        tc4 = messagebox.showinfo(title='答案',message= '答：爆热是炸药爆炸做功的能量指标。')
    if Btn0["state"] != "normal":
        Btn0.config(state=NORMAL)  # button to page down is enabled
    v.set(str(currentpage))
def topic9():
    global currentpage, pagecount
    topic9.config(state=DISABLED,relief = 'sunken')
    tc3 = messagebox.showinfo(title='必答题第10题',message ='10．爆压的含义？')
    if tc3 == 'ok':
        tc4 = messagebox.showinfo(title='答案',message= '答：爆压是炸药爆炸时生成的高温高压气体的压力。')
    if Btn0["state"] != "normal":
        Btn0.config(state=NORMAL)  # button to page down is enabled
    v.set(str(currentpage))
def topic10():
    global currentpage, pagecount
    topic10.config(state=DISABLED,relief = 'sunken')
    tc3 = messagebox.showinfo(title='必答题第11题',message ='11．殉爆的含义？')
    if tc3 == 'ok':
        tc4 = messagebox.showinfo(title='答案',message= '答：殉爆是主爆药发生爆炸时引起相隔一定距离的受爆药爆炸的现象。')
    if Btn0["state"] != "normal":
        Btn0.config(state=NORMAL)  # button to page down is enabled
    v.set(str(currentpage))
def topic11():
    global currentpage, pagecount
    topic11.config(state=DISABLED,relief = 'sunken')
    tc3 = messagebox.showinfo(title='必答题第12题',message ='12．殉爆距离的含义？')
    if tc3 == 'ok':
        tc4 = messagebox.showinfo(title='答案',message= '答：主爆药与受爆药之间能发生殉爆的最大距离称为殉爆距离。')
    if Btn0["state"] != "normal":
        Btn0.config(state=NORMAL)  # button to page down is enabled
    v.set(str(currentpage))
def topic12():
    global currentpage, pagecount
    topic12.config(state=DISABLED,relief = 'sunken')
    tc3 = messagebox.showinfo(title='必答题第13题',message ='13．炸药的感度表示？')
    if tc3 == 'ok':
        tc4 = messagebox.showinfo(title='答案',message= '答：炸药在外界作用下发生爆炸的难易程度。 ')
    if Btn0["state"] != "normal":
        Btn0.config(state=NORMAL)  # button to page down is enabled
    v.set(str(currentpage))
def topic13():
    global currentpage, pagecount
    topic13.config(state=DISABLED,relief = 'sunken')
    tc3 = messagebox.showinfo(title='必答题第14题',message ='14．热感度的含义？')
    if tc3 == 'ok':
        tc4 = messagebox.showinfo(title='答案',message= '答：热感度指在热的作用下炸药发生爆炸的难易程度。')
    if Btn0["state"] != "normal":
        Btn0.config(state=NORMAL)  # button to page down is enabled
    v.set(str(currentpage))
def topic14():
    global currentpage, pagecount
    topic14.config(state=DISABLED,relief = 'sunken')
    tc3 = messagebox.showinfo(title='必答题第15题',message ='15．撞击感度的含义？')
    if tc3 == 'ok':
        tc4 = messagebox.showinfo(title='答案',message= '答：撞击感度指在机械撞击作用下炸药发生爆炸的难易程度。')
    if Btn0["state"] != "normal":
        Btn0.config(state=NORMAL)  # button to page down is enabled
    v.set(str(currentpage))
def topic15():
    global currentpage, pagecount
    topic15.config(state=DISABLED,relief = 'sunken')
    tc3 = messagebox.showinfo(title='必答题第16题',message ='16. 目前使用最广泛的乳化炸药分哪三类？')
    if tc3 == 'ok':
        tc4 = messagebox.showinfo(title='答案',message= '答：岩石乳化炸药、煤矿乳化炸药和露天乳化炸药。')
    if Btn0["state"] != "normal":
        Btn0.config(state=NORMAL)  # button to page down is enabled
    v.set(str(currentpage))
def topic16():
    global currentpage, pagecount
    topic16.config(state=DISABLED,relief = 'sunken')
    tc3 = messagebox.showinfo(title='必答题第17题',message ='17.2号岩石乳化炸药爆速不小于？')
    if tc3 == 'ok':
        tc4 = messagebox.showinfo(title='答案',message= '答：3200m/s。')
    if Btn0["state"] != "normal":
        Btn0.config(state=NORMAL)  # button to page down is enabled
    v.set(str(currentpage))
def topic17():
    global currentpage, pagecount
    topic17.config(state=DISABLED,relief = 'sunken')
    tc3 = messagebox.showinfo(title='必答题第18题',message ='18、目前，常用的工业雷管主要有？')
    if tc3 == 'ok':
        tc4 = messagebox.showinfo(title='答案',message= '答：电雷管、导爆管雷管和电子雷管三大类。')
    if Btn0["state"] != "normal":
        Btn0.config(state=NORMAL)  # button to page down is enabled
    v.set(str(currentpage))
def topic18():
    global currentpage, pagecount
    topic18.config(state=DISABLED,relief = 'sunken')
    tc3 = messagebox.showinfo(title='必答题第19题',message ='19、秒延期电雷管是通电后延迟爆炸时间以什么为计量单位的延发电雷管？')
    if tc3 == 'ok':
        tc4 = messagebox.showinfo(title='答案',message= '答：秒、半秒、1／4秒.')
    if Btn0["state"] != "normal":
        Btn0.config(state=NORMAL)  # button to page down is enabled
    v.set(str(currentpage))
def topic19():
    global currentpage, pagecount
    topic19.config(state=DISABLED,relief = 'sunken')
    tc3 = messagebox.showinfo(title='必答题第20题',message ='20、《爆破安全规程》规定，用来导通电雷管的仪表工作电流不应超过多少毫安？')
    if tc3 == 'ok':
        tc4 = messagebox.showinfo(title='答案',message= '答：30mA')
    if Btn0["state"] != "normal":
        Btn0.config(state=NORMAL)  # button to page down is enabled
    v.set(str(currentpage))

def page_down():
    """
    add 1 to displayed number,
    disable Btn2 button when currentpage reaches pagecount
    """
    global currentpage, pagecount

    currentpage += 1
    topic1.config(state=NORMAL)  # button to page up is enabled
    topic2.config(state=NORMAL)

    v.set(str(currentpage))


topic0 = Button(text="1", padx=16, pady=8, command=topic0)
topic0.pack()
topic0.place(x=0, y=10)
topic0.config(state=NORMAL)
topic2 = Button(text="2", padx=16, pady=8, command=topic2)
topic2.pack()
topic2.place(x=50, y=10)
topic2.config(state=NORMAL)

Btn0 = Button(text="恢复", padx=8, pady=6, command=page_down)
Btn0.pack()
Btn0.place(x=250, y=200)

root.mainloop()