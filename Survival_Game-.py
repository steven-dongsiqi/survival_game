from random import*
#from turtle import*
from time import*
import os
from tkinter import *
import tkinter.simpledialog
import tkinter.messagebox
import tkinter.ttk
import pyperclip
#os.system("title Survival_Game 1.2")
#os.system("color b")
title = "Survival_Game 1.2"
#a = input("输入存档码(第一次进入游戏请忽视,请勿试图伪造存档码,以免造成游戏崩溃):")————————————————###同等替换为以下可视化设计###————————————————
WorldSeed=tkinter.simpledialog.askstring(title,"输入存档码(第一次进入游戏请忽视,请勿试图伪造存档码,以免造成游戏崩溃):",initialvalue='')

if " ahfuiehaihfrhsufcha" in WorldSeed :#校验存档码
    WorldSeed.replace(" ahfuiehaihfrhsufcha","")
    info = WorldSeed.split(" ")
    try:
        if info[5] == "nothing":
            info[5] = ""
            
        day_money = int(info[0])
        money = int(info[1])
        job = int(info[2])
        UsersName = info[3]
        day = int(info[4])
        house = info[5]
    except:
#        print("请勿伪造存档码,以免游戏崩溃!")————————————————###同等替换为以下可视化设计###————————————————
        
        NewUser = True
else:
    NewUser = True
if NewUser == True:
    day = 1
    money = 0
    house = ""
    job = 0
    day_money = 0
    UsersName = ""
    while UsersName == "":
        #UsersName = input("请输入用户名:")————————————————###同等替换为以下可视化设计###————————————————
        UsersName =tkinter.simpledialog.askstring(title,"请输入用户名:",initialvalue='steve')
        
    #print(UsersName + "进入了游戏")————————————————###同等替换为以下可视化设计###————————————————
    tkinter.messagebox.showinfo(title,UsersName + "进入了游戏")
    #print("您好,您来到这个世界的目的是生存下去")————————————————###同等替换为以下可视化设计###————————————————
    tkinter.messagebox.showinfo(title,"您好,您来到这个世界的目的是生存下去\r我是您的助手,将协助您生存\r您可以:\r砍树,三次一天,需要买斧头\r挖矿,一次一天,需要买镐子\r买东西\r探索,无限制,可买村庄及城市\r等\r接下来请选职业")
#    print("我是您的助手,将协助您生存")
#    print("您可以:")
#    print("砍树,三次一天,需要买斧头")
#    print("挖矿,一次一天,需要买镐子")
#    print("买东西")
#    print("探索,无限制,可买村庄及城市")
#    print("等")
#    print("接下来请选职业")
#    print("职业有:")
#    print("1.渔夫,2.农民,3.矿工,4.伐木工")
#    job = input("请输入正确的职业:")
    tkinter.simpledialog.askstring(title,"职业有:\r1.渔夫\r2.农民\r3.矿工\r4.伐木工\r请输入正确的职业:(留空则随机生成)",initialvalue='')
if job != "1" and job != "2" and job != "3" and job != "4":#此处有一个更改
    job = str(randint(1,4))
job = int(job)
if job == 2:
    CLA = 0
screen = []
a = 0
sword = False
shield = False
armour = False
time_tick = 0

villages_for_sale = 0  

big_villages_for_sale = 0
sold_village = 0
HP = 100#生命值
SV = 100#饥饿值
ask = ""
face_thing = "nothing"
tree_time = 0
mine_time = 0
bag = {}
def an(a,c):
    r1 = randint(0,100)
    if r1 <= a:
        return c
    else:
        return 0
def qus(goods,price):
    global money,ask
    ask=tkinter.messagebox.askyesno(title,("商品:",goods,"/r","价格:",price))
#    print("商品:",goods)
#    print("价格:",price)
#    print("购买请输入 1")
#    ask = input()
    if ask == 'yes':
        ask = tkinter.simpledialog.askinteger("输入数量:")
        money -= int(price) * int(ask)
        return True
    else:
        return False
screen.append(UsersName + "进入了游戏")
while True:
    os.system("cls")
    a = len(screen)
    for i in range(a):
        tkinter.messagebox.showinfo(screen[i])

    tkinter.messagebox.showinfo("现在是第",day,"天",time_tick/1000,"时")
    tkinter.messagebox.showinfo("您有",money,"块钱")
    if money < 0:
        tkinter.messagebox.showinfo("请尽快还债!")
    tkinter.messagebox.showinfo("您的生命值是",HP)
    if sword == True:
        tkinter.messagebox.showinfo("您拥有防身武器")
    if shield == True:
        tkinter.messagebox.showinfo("您拥有盾牌")
    if armour == True:
        tkinter.messagebox.showinfo("您拥有盔甲")
    tkinter.messagebox.showinfo("您的饥饿值是",SV)
    if SV == 0:
        tkinter.messagebox.showinfo("请去饭店恢复体力!")
    title = "{0} time: day{1} {2} o\'clock  {3} health {4} Starvation value {5}{6} emc sword {7} armour {8} shield {9}" .format (title,day , time_tick/1000, money ,HP , SV , money , str(sword) , str(armour) , str(shield))
    '''
    dth_value=IntVar()
    def fedbk():
        print(IntVar().get())
    tkinter.ttk.Radiobutton(Tk() , text='探索',variable=dth_value,value=1,command = fedbk()).pack()
    tkinter.ttk.Radiobutton(Tk() , text='挖矿',variable=dth_value,value=2,command = fedbk()).pack()
    tkinter.ttk.Radiobutton(Tk() , text='砍树',variable=dth_value,value=3,command = fedbk()).pack()
    tkinter.ttk.Radiobutton(Tk() , text='去商/饭店',variable=dth_value,value=4).pack()
    tkinter.ttk.Radiobutton(Tk() , text='职业技能',variable=dth_value,value=5).pack()
    Tk().mainloop()
    '''
#    print("接下来您要干什么?")
#    print("1.探索,2.挖矿,3.砍树,4.去商/饭店,5.职业技能")
#    print("输入exit退出并生成存档码")
    askop=tkinter.messagebox.askyesno(title,'接下来您要干什么?\r1.探索')
    if askop == 'true':
        if face_thing == "nothing" or face_thing == "village":
            a = an(70,1)
            if a == 0:
                a = an(30,1)
                if a == 1:
                    a = an(50,1)
                    if a == 1:
                        tkinter.messagebox.showinfo("河流!")
                        face_thing = "river"
                    elif a == 0:
                        tkinter.messagebox.showinfo("大海!")
                        face_thing = "sea"
                elif a == 0:
                    tkinter.messagebox.showinfo("探索了个空气……")
                    face_thing = "nothing"
            elif a == 1:
                tkinter.messagebox.showinfo("发现村庄!")
                a = an(30,1)
                if a == 1:
                    askop=tkinter.messagebox.askyesno(title,"走近一看,是个大村庄\r是否买下?")
                    if askop == "yes":
                        money -= 20000
                        day_money += 2000
                        sold_village += 1
                    elif a == "no":
                        big_villages_for_sale += 1
                elif a == 0:
                    askop=tkinter.messagebox.askyesno(title,"是否买下?")
                    if askop == "yes":
                        money -= 10000
                        day_money += 1000
                        sold_village += 1
                    elif askop == "no":
                        villages_for_sale += 1
                    face_thing = "village"
            time_tick += 10000
        if face_thing == "river":
            askop=tkinter.messagebox.askyesno(title,"是否探索下去?")
            #print("是否探索下去(是为1,否为2)")
            #a = input()
            if askop == "yes":
                tkinter.messagebox.showinfo("有大海!")
                face_thing = "sea"
                time_tick += 10000
            elif a == "no":
                tkinter.messagebox.showinfo("又回来了")
                face_thing = "nothing"
                time_tick += 5000
        if face_thing == "sea":
            askop=tkinter.messagebox.askyesno(title,"要买船吗?")
            #a = input()
            if askop == "yes":
                money -= 200
                bag["common boat"] = 1
                a = an(20,1)
                if a == 1:
                    askop=tkinter.messagebox.askyesno(title,"发现海底神殿!\r是否探索?")
                    time_tick += 10000
                    if askop == "yes":
                        a = an(70,1)
                        if a == 1:
                            tkinter.mmessagebox.showinfo("获得丰厚的报酬")
                            money += 64000
                        if a == 0 and armour == False:
                            tkinter.messagebox.showerror(UsersName + "被守卫者的魔法杀死了")
                            screen.append(UsersName + "被守卫者的魔法杀死了")
                            HP = 0
                        else:
                            armour == False
            face_thing = "nothing"
        SV -= 20
        time_tick += 50000
        a = "0"
    else:
        askop=tkinter.messagebox.askyesno(title,'接下来您要干什么?\r2.挖矿')
        if askop == 'true':
            if mine_time <= 1 or job == 3:
                askop = tkinter.messagebox.askyesno(title,"请选择挖矿地点\r下界(是)主世界(否):")
                if askop == "yes":
                    tkinter.messagebox.showinfo("准备一套工具!")
                    money -= 24548
                    a = an(90,1)
                    if a == 1:
                        ret = random.randint(0,32)*8192+random.randint(0,1024)*64+random.randint(0,256)*256+random.randint(0,256)*2048+random.randint(0,256)*128+random.randint(0,128)*864
                        money += ret
                        tkinter.messagebox.showinfo("获得丰厚的报酬,{0}emc".format (ret)) 
                    if a == 0 and armour == True:
                        armour = False
                    if a == 0 and shield == True:
                        shield = False
                    if a == 0 and armour == False and shield == False:
                        a = an(50,1)
                        if a == 1:
                            tkinter.messagebox.showerror("失足掉入岩浆")
                            screen.append(UsersName + "试图在岩浆里游泳")
                            HP = 0
                        if a == 0 and sword == False:
                            a = an(30,1)
                            if a == 1:
                                screen.append(UsersName + "被僵尸杀死了")
                                tkinter.messagebox.showerror(UsersName + "被僵尸杀死了")
                            if a == 0:
                                a = an(40,1)
                                if a == 1:
                                    tkinter.messagebox.showerror(UsersName + "被骷髅射手杀死了")
                                    screen.append(UsersName + "被骷髅射手杀死了")
                                else:
                                    a = an(60,1)
                                    if a == 1:
                                        tkinter.messagebox.showerror(UsersName + "爆炸了")
                                        screen.append(UsersName + "爆炸了")
                                    else:
                                        a = an(30,1)
                                        if a == 1:
                                            tkinter.messagebox.showerror(UsersName + "试图逃离僵尸时试图在岩浆里游泳")
                                            screen.append(UsersName + "试图逃离僵尸时试图在岩浆里游泳")
                                        if a == 0:
                                            a = an(40,1)
                                            if a == 1:
                                                tkinter.messagebox.showerror(UsersName + "试图逃离骷髅射手时试图在岩浆里游泳")
                                                screen.append(UsersName + "试图逃离骷髅射手时试图在岩浆里游泳")
                                            else:
                                                tkinter.messagebox.showerror(UsersName + "试图逃离苦力怕时时试图在岩浆里游泳")
                                                screen.append(UsersName + "试图逃离苦力怕时时试图在岩浆里游泳")
                            HP = 0
                    time_tick += 14000
                    mine_time += 1
                    SV -= 30
                else:
                    tkinter.messagebox.showinfo("准备一套工具!")
                    money -= 24548
                    a = an(90,1)
                    if a == 1:
                        tkinter.messagebox.showinfo("获得丰厚的报酬")
                        money += random.randint(0,256)*256+random.randinnt(0,16)*4096+random.randint(0,50)*277
                    elif a == 0 and armour == False and shield == False:
                        a = an(50,1)
                        if a == 1:
                            tkinter.messagebox.showerror("失足掉入岩浆")
                            screen.append(UsersName + "试图在岩浆里游泳")
                            HP = 0
                        if a == 0 and sword == False:
                            a = an(30,1)
                            if a == 1:
                                screen.append(UsersName + "被岩浆怪杀死了")
                                tkinter.messagebox.showerror(UsersName + "被岩浆怪杀死了")
                            if a == 0:
                                a = an(40,1)
                                if a == 1:
                                    tkinter.messagebox.showerror(UsersName + "被骷髅射手杀死了")
                                    screen.append(UsersName + "被骷髅射手杀死了")
                                else:
                                    a = an(60,1)
                                    if a == 1:
                                        tkinter.messagebox.showerror(UsersName + "被烈焰人杀死了")
                                        screen.append(UsersName + "被烈焰人杀死了")
                                    else:
                                        a = an(30,1)
                                        if a == 1:
                                            tkinter.messagebox.showerror(UsersName + "试图逃离岩浆怪时试图在岩浆里游泳")
                                            screen.append(UsersName + "试图逃离岩浆怪时试图在岩浆里游泳")
                                        if a == 0:
                                            a = an(40,1)
                                            if a == 1:
                                                tkinter.messagebox.showerror(UsersName + "试图逃离骷髅射手时试图在岩浆里游泳")
                                                screen.append(UsersName + "试图逃离骷髅射手时试图在岩浆里游泳")
                                            else:
                                                tkinter.messagebox.showerror(UsersName + "试图逃离烈焰人时试图在岩浆里游泳")
                                                screen.append(UsersName + "试图逃离烈焰人时试图在岩浆里游泳")
                            HP = 0
                    time_tick += 20000
                    mine_time += 1
                    SV -= 40
            else:
                tkinter.messagebox.showwarning("今日挖矿次数已用完")
            a = "0"
        else:
            askop=tkinter.messagebox.askyesno(title,'接下来您要干什么?\r3.砍树')
            if askop == 'true':
                if tree_time <= 3 or job == 4:
                    tkinter.messagebox.showinfo("准备一套工具!")
                    money -= 100
                    for i in range(2):
                        if randint(1,3) == 1:
                            tkinter.messagebox.showinfo("丰产林!")
                            money += 2500
                        money += 7500
                else:
                    tkinter.messagebox.showwarning("今日砍树次数已用完")
                time_tick += 10000
                a = "0"
            else:
                askop=tkinter.messagebox.askyesno(title,'接下来您要干什么?\r4.去商/饭店')
                if askop == 'true':
                    tkinter.messagebox.showinfo("商店:")
                    if house == "":
                        shoppingthing='house'
                        tkinter.messagebox.showinfo("房屋区")
                        a = qus("1.豪华大别墅","10000000emc")
                        if a == True:
                            house = "1"
                        a = qus("2.郊区平房","200000emc")
                        if a == True:
                            house = "2"
                        a = qus("3.市区公寓","800000emc")
                        if a == True:
                            house = "3"
                    else:
                        askpo = tkinter.messagebox.askyesno("要换房吗")
                        if askop == "1":
                            tkinter.messagebox.showinfo("房屋区")
                            shoppingthing='house'
                            a = qus("1.豪华大别墅","10000000emc")
                            if a == True:
                                house = "1"
                            a = qus("2.郊区平房","200000emc")
                            if a == True:
                                house = "2"
                            a = qus("3.市区公寓","800000enc")
                            if a == True:
                                house = "3"
                    tkinter.messagebox.showinfo("食物区")
                    shoppingthing = 'food'
                    a = qus("1.面包","72emc")
                    if a == True:
                        SV += 10 * int(ask)
                        tkinter.messagebox.showinfo("已食用")
                    a = qus("2.牛奶","784emc")
                    if a == True:
                        SV += 10 * int(ask)
                        tkinter.messagebox.showinfo("已食用")
                    a = "0"
                    tkinter.messagebox.showinfo("盔甲区")
                    shoppingthing = armour
                    a = qus("1.剑","100")
                    if a == True:
                        sword = True
                    a = qus("2.盾","150")
                    if a == True:
                        shield = True
                    a = qus("3.盔甲","10000")
                    if a == True:
                        armour = True
                    a = "0"
                else:
                    askop=tkinter.messagebox.askyesno(title,'接下来您要干什么?\r5.职业技能\r按否退出')
                    if askop == 'true':
                        if job == 1:
                            tkinter.messagebox.showinfo("钓鱼!花费36emc")
                            money -= 36
                            if an(10,1) == 1:
                                tkinter.messagebox.showinfo("鱼跑了!")
                            else:
                                if an(50,1) == 1:
                                    tkinter.messagebox.showinfo("钓到了几条鱼")
                                    money += 64*randint(1,5)
                                else:
                                    tkinter.messagebox.showinfo("钓到稀有物品!")
                                    money += 500
                            time_tick += 1000
                        elif job == 2:
                            tkinter.messagebox.showinfo("需要购买种子")
                            a = tkinter.simpledialog.askstring(title,"数量:",initialvalue='')
                            money -= int(a) * 16
                            tkinter.messagebox.showinfo("需要购买锄头,花费520emc")#游戏中铁锄的emc值
                            money -= 520
                            CLA += int(a)
                            time_tick += 5000
                        else:
                            tkinter.messagebox.showinfo("这个职业没有主动技能")
                    else :
                        pyperclip.copy((str(day_money)+" "+str(money)+" "+str(job)+" "+UsersName+" "+str(day)+" "+str(house)+" ahfuiehaihfrhsufcha"))
                        askop=tkinter.messagebox.askyesno(title,'存档码已复制到剪贴板?点击否再次复制,点击确定退出游戏')
                        pyperclip.copy((str(day_money)+" "+str(money)+" "+str(job)+" "+UsersName+" "+str(day)+" "+str(house)+" ahfuiehaihfrhsufcha")) if askop == 'fause' else exit()
    if SV <= 0 and HP >= 21:
        HP -= 20
        SV = 0
    if SV <= 0 and HP <= 20:
        HP -= 20
        SV = 0
        tkinter.messagebox.showerror(UsersName+"饿死了")
        screen.append(UsersName+"饿死了")
    if SV >= 100:
        SV = 100
        HP += 20
    if HP > 100:
        HP = 100
    if HP <= 0:
        money = 0
        HP = 100
        SV = 100
        face_thing = "nothing"
        bag = {}
        sword = False
        shield = False
        armour = False
    if time_tick >= 24000:
        time_tick = 0
        mine_time = 0
        tree_time = 0
        day += 1
        money += day_money
    if money < 0:
        money += money * 0.5



