from random import*

from time import*
import os
from tkinter import *
import tkinter.simpledialog
import tkinter.messagebox
import tkinter.ttk
import pyperclip

title = "Survival_Game 1.2"
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
        tkinter.messagebox.showwarning('请勿试图伪造存档码,以免造成游戏崩溃')
        
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
        UsersName =tkinter.simpledialog.askstring(title,"请输入用户名:",initialvalue='steve')
    tkinter.messagebox.showinfo(title,UsersName + "进入了游戏")
    tkinter.messagebox.showinfo(title,"您好,您来到这个世界的目的是生存下去\r我是您的助手,将协助您生存\r您可以:\r砍树,三次一天,需要买斧头\r挖矿,一次一天,需要买镐子\r买东西\r探索,无限制,可买村庄及城市\r等\r接下来请选职业")
    job=tkinter.simpledialog.askinteger(title,"职业有:\r1.渔夫\r2.农民\r3.矿工\r4.伐木工\r请输入正确的职业:(输入其他数字则随机生成)",initialvalue='')
if job <= 0 or job >=5:
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
    ask=tkinter.messagebox.askyesno(title,("商品:",goods,"\r","价格:",price,'emc'))
    if ask == True :
        if shoppingthing == 'food':
            ask = tkinter.simpledialog.askinteger(title,"输入数量:")
        else:
            ask==1
        money -= int(price) * int(ask)
        return True
    else:
        return False
screen.append(UsersName + "进入了游戏")
while True:
    os.system("cls")
    a = len(screen)
    for i in range(a):
        tkinter.messagebox.showinfo(title,screen[i])

    tkinter.messagebox.showinfo(title,("现在是第",day,"天",time_tick/1000,"时"))
    tkinter.messagebox.showinfo(title,("您有",money,"块钱"))
    if money < 0:
        tkinter.messagebox.showinfo(title,("请尽快还债!"))
    tkinter.messagebox.showinfo(title,("您的生命值是",HP))
    if sword == True:
        tkinter.messagebox.showinfo(title,"您拥有防身武器")
    if shield == True:
        tkinter.messagebox.showinfo(title,"您拥有盾牌")
    if armour == True:
        tkinter.messagebox.showinfo(title,"您拥有盔甲")
    tkinter.messagebox.showinfo(title,("您的饥饿值是",SV))
    if SV == 0:
        tkinter.messagebox.showinfo(title,"请去饭店恢复体力!")
    title = "{0} time: day{1} {2} o\'clock  {3} health {4} Starvation value {5}{6} emc sword {7} armour {8} shield {9}" .format (title,day , time_tick/1000, money ,HP , SV , money , str(sword) , str(armour) , str(shield))
    print('a')
    askop=tkinter.messagebox.askyesno(title,'接下来您要干什么?\r1.探索')
    print(askop)
    if askop == True:
        if face_thing == "nothing" or face_thing == "village":
            a = an(70,1)
            if a == 0:
                a = an(0,1)
                if a == 1:
                    a = an(50,1)
                    if a == 1:
                        tkinter.messagebox.showinfo(title,"河流!")
                        face_thing = "river"
                    elif a == 0:
                        tkinter.messagebox.showinfo(title,"大海!")
                        face_thing = "sea"
                elif a == 0:
                    tkinter.messagebox.showinfo(title,"探索了个空气……")
                    face_thing = "nothing"
            elif a == 1:
                tkinter.messagebox.showinfo(title,"发现村庄!")
                a = an(30,1)
                if a == 1:
                    askop=tkinter.messagebox.askyesno(title,"走近一看,是个大村庄\r是否买下?")
                    if askop == True:
                        money -= 20000
                        day_money += 2000
                        sold_village += 1
                    elif a == False:
                        big_villages_for_sale += 1
                elif a == 0:
                    askop=tkinter.messagebox.askyesno(title,"是否买下?")
                    if askop ==True:
                        money -= 10000
                        day_money += 1000
                        sold_village += 1
                    elif askop == False:
                        villages_for_sale += 1
                    face_thing = "village"
            time_tick += 10000
        if face_thing == "river":
            askop=tkinter.messagebox.askyesno(title,"是否探索下去?")
            if askop == True:
                tkinter.messagebox.showinfo(title,"有大海!")
                face_thing = "sea"
                time_tick += 10000
            elif a == False:
                tkinter.messagebox.showinfo(title,"又回来了")
                face_thing = "nothing"
                time_tick += 5000
        if face_thing == "sea":
            askop=tkinter.messagebox.askyesno(title,"要买船吗?")
            if askop == True:
                money -= 200
                bag["common boat"] = 1
                a = an(20,1)
                if a == 1:
                    askop=tkinter.messagebox.askyesno(title,"发现海底神殿!\r是否探索?")
                    time_tick += 10000
                    if askop == True:
                        a = an(70,1)
                        if a == 1:
                            tkinter.messagebox.showinfo(title,"获得丰厚的报酬")
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
        if askop == True:
            if mine_time <= 1 or job == 3:
                askop = tkinter.messagebox.askyesno(title,"请选择挖矿地点\r下界(是)主世界(否):")
                if askop == True:
                    tkinter.messagebox.showinfo(title,"准备一套工具!")
                    money -= 24548
                    a = an(90,1)
                    if a == 1:
                        ret = randint(0,32)*8192+randint(0,1024)*64+randint(0,256)*256+randint(0,256)*2048+randint(0,256)*128+randint(0,128)*864
                        money += ret
                        tkinter.messagebox.showinfo("获得丰厚的报酬,{0}emc".format (ret)) 
                    if a == 0 and armour == True:
                        armour = False
                    if a == 0 and shield == True:
                        shield = False
                    if a == 0 and armour == False and shield == False:
                        a = an(50,1)
                        if a == 1:
                            tkinter.messagebox.showerror(title,"失足掉入岩浆")
                            screen.append(UsersName + "试图在岩浆里游泳")
                            HP = 0
                        if a == 0 and sword == False:
                            a = an(30,1)
                            if a == 1:
                                screen.append(UsersName + "被僵尸杀死了")
                                tkinter.messagebox.showerror(title,UsersName + "被僵尸杀死了")
                            if a == 0:
                                a = an(40,1)
                                if a == 1:
                                    tkinter.messagebox.showerror(title,UsersName + "被骷髅射手杀死了")
                                    screen.append(UsersName + "被骷髅射手杀死了")
                                else:
                                    a = an(60,1)
                                    if a == 1:
                                        tkinter.messagebox.showerror(title,UsersName + "爆炸了")
                                        screen.append(UsersName + "爆炸了")
                                    else:
                                        a = an(30,1)
                                        if a == 1:
                                            tkinter.messagebox.showerror(title,UsersName + "试图逃离僵尸时试图在岩浆里游泳")
                                            screen.append(UsersName + "试图逃离僵尸时试图在岩浆里游泳")
                                        if a == 0:
                                            a = an(40,1)
                                            if a == 1:
                                                tkinter.messagebox.showerror(title,UsersName + "试图逃离骷髅射手时试图在岩浆里游泳")
                                                screen.append(UsersName + "试图逃离骷髅射手时试图在岩浆里游泳")
                                            else:
                                                tkinter.messagebox.showerror(title,UsersName + "试图逃离苦力怕时时试图在岩浆里游泳")
                                                screen.append(UsersName + "试图逃离苦力怕时时试图在岩浆里游泳")
                            HP = 0
                    time_tick += 14000
                    mine_time += 1
                    SV -= 30
                else:
                    tkinter.messagebox.showinfo(title,"准备一套工具!")
                    money -= 24548
                    a = an(90,1)
                    if a == 1:
                        tkinter.messagebox.showinfo(title,"获得丰厚的报酬")
                        money +=randint(0,256)*256+randint(0,16)*4096+randint(0,50)*277
                    elif a == 0 and armour == False and shield == False:
                        a = an(50,1)
                        if a == 1:
                            tkinter.messagebox.showerror(title,"失足掉入岩浆")
                            screen.append(UsersName + "试图在岩浆里游泳")
                            HP = 0
                        if a == 0 and sword == False:
                            a = an(30,1)
                            if a == 1:
                                screen.append(UsersName + "被岩浆怪杀死了")
                                tkinter.messagebox.showerror(title,UsersName + "被岩浆怪杀死了")
                            if a == 0:
                                a = an(40,1)
                                if a == 1:
                                    tkinter.messagebox.showerror(title,UsersName + "被骷髅射手杀死了")
                                    screen.append(UsersName + "被骷髅射手杀死了")
                                else:
                                    a = an(60,1)
                                    if a == 1:
                                        tkinter.messagebox.showerror(title,UsersName + "被烈焰人杀死了")
                                        screen.append(UsersName + "被烈焰人杀死了")
                                    else:
                                        a = an(30,1)
                                        if a == 1:
                                            tkinter.messagebox.showerror(title,UsersName + "试图逃离岩浆怪时试图在岩浆里游泳")
                                            screen.append(UsersName + "试图逃离岩浆怪时试图在岩浆里游泳")
                                        if a == 0:
                                            a = an(40,1)
                                            if a == 1:
                                                tkinter.messagebox.showerror(title,UsersName + "试图逃离骷髅射手时试图在岩浆里游泳")
                                                screen.append(UsersName + "试图逃离骷髅射手时试图在岩浆里游泳")
                                            else:
                                                tkinter.messagebox.showerror(title,UsersName + "试图逃离烈焰人时试图在岩浆里游泳")
                                                screen.append(UsersName + "试图逃离烈焰人时试图在岩浆里游泳")
                            HP = 0
                    time_tick += 20000
                    mine_time += 1
                    SV -= 40
            else:
                tkinter.messagebox.showwarning(title,"今日挖矿次数已用完")
            a = "0"
        else:
            askop=tkinter.messagebox.askyesno(title,'接下来您要干什么?\r3.砍树')
            if askop == True:
                if tree_time <= 3 or job == 4:
                    tkinter.messagebox.showinfo(title,"准备一套工具!")
                    money -= 100
                    for i in range(2):
                        if randint(1,3) == 1:
                            tkinter.messagebox.showinfo(title,"丰产林!")
                            money += 2500
                        money += 7500
                else:
                    tkinter.messagebox.showwarning(title,"今日砍树次数已用完")
                time_tick += 10000
                a = "0"
            else:
                askop=tkinter.messagebox.askyesno(title,'接下来您要干什么?\r4.去商/饭店')
                if askop == True:
                    tkinter.messagebox.showinfo(title,"商店:")
                    if house == "":
                        shoppingthing='house'
                        tkinter.messagebox.showinfo(title,"房屋区")
                        a = qus("1.豪华大别墅","10000000")
                        if a == True:
                            house = "1"
                        else:
                            a = qus("2.郊区平房","200000")
                            if a == True:
                                house = "2"
                            else:
                                a = qus("3.市区公寓","800000")
                                if a == True:
                                    house = "3"
                    else:
                        askpo = tkinter.messagebox.askyesno("要换房吗")
                        if askop == "1":
                            tkinter.messagebox.showinfo("房屋区")
                            shoppingthing='house'
                            a = qus("1.豪华大别墅","10000000")
                            if a == True:
                                house = "1"
                            else:    
                                a = qus("2.郊区平房","200000")
                                if a == True:
                                    house = "2"
                                else:
                                    a = qus("3.市区公寓","800000")
                                    if a == True:
                                        house = "3"
                    tkinter.messagebox.showinfo("食物区")
                    shoppingthing = 'food'
                    a = qus("1.面包","72")
                    if a == True:
                        SV += 10 * int(ask)
                        tkinter.messagebox.showinfo("已食用")
                    a = qus("2.牛奶","784")
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
                    if askop == True:
                        if job == 1:
                            tkinter.messagebox.showinfo(title,"钓鱼!花费36emc")
                            money -= 36
                            if an(10,1) == 1:
                                tkinter.messagebox.showinfo(title,"鱼跑了!")
                            else:
                                if an(50,1) == 1:
                                    tkinter.messagebox.showinfo(title,"钓到了几条鱼")
                                    money += 64*randint(1,5)
                                else:
                                    tkinter.messagebox.showinfo(title,"钓到稀有物品!")
                                    money += 500
                            time_tick += 1000
                        elif job == 2:
                            tkinter.messagebox.showinfo(title,"需要购买种子")
                            a = tkinter.simpledialog.askstring(title,"数量:",initialvalue='')
                            money -= int(a) * 16
                            tkinter.messagebox.showinfo(title,"需要购买锄头,花费520emc")#游戏中铁锄的emc值
                            money -= 520
                            CLA += int(a)
                            time_tick += 5000
                        else:
                            tkinter.messagebox.showinfo(title,"这个职业没有主动技能")
                    else :
                        pyperclip.copy((str(day_money)+" "+str(money)+" "+str(job)+" "+UsersName+" "+str(day)+" "+str(house)+" ahfuiehaihfrhsufcha"))
                        askop=tkinter.messagebox.askyesno(title,'存档码已复制到剪贴板?点击否再次复制,点击确定退出游戏(会自动弹出记事本)')
                        os.system('notepad')
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