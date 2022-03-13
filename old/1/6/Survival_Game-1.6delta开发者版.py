from random import*
import time
import os
os.system("title Survival_Game 1.6.1")
os.system("color b")
screen = []
a: int = 0
day = 1
money = 0
house = ""
admin = ""
job = 0
day_money = 0
mineral_abundance = 50
number_of_stronghold = 7
village_built = True
sword = False#剑
shield = False#盾
armour = False#盔甲
time_tick = 0
villages_for_sale = 0
big_villages_for_sale = 0
sold_village = 0
HP = 100#生命值
SV = 100#饥饿值
IQ = 130#智商
PT = 0#威信
job_list = ["1.渔夫","2.农民","3.矿工","4.伐木工","5.乞丐","6.科学家","7.工程师","8.将领","9.国王"]
CLA = 0
TP = 0
ask = ""
face_thing = "nothing"
tree_time = 0
mine_time = 0
bag = {}
while True:
    a = input("1.创建新的世界;2.进入输入的世界(老版存档码及新版存档码都可用):")
    if a == "2":
        a = input("请输入存档码")
        if " ahfuiehaihfrhsufcha" in a:
            a = a.replace(" ahfuiehaihfrhsufcha","")
            b = a.split(" ")
            try:
                if "#" in a:
                    if b[5] == "nothing":
                        b[5] = ""
                    day_money = int(b[0])
                    money = int(b[1])
                    a = b[2].split("#")
                    job = int(a[1])
                    CLA = int(a[2])
                    TP = int(a[3])
                    admin = b[3]
                    day = int(b[4])
                    house = b[5]
                else:
                    if b[5] == "nothing":
                        b[5] = ""
                    day_money = int(b[0])
                    money = int(b[1])
                    job = int(b[2])
                    admin = b[3]
                    day = int(b[4])
                    house = b[5]
                a = False
            except:
                print(":( Survival_Game.exe未响应")
                print("我们只收集亿些错误信息,随后程序将重启")
                a = [".","..","...","....",".....","......"]
                for i in range(100):
                    time.sleep(0.1)
                    print(a[i % 6])
                    os.system("cls")
                a = "true"
        else:
            a = True
    else:
        a = True
    if a != "true":
        break
if a:
    while admin == "" or " " in admin:
        admin = input("请输入用户名(不含空格)")
    print("世界选项:按任意按键改变设置,直接enter使用默认配置")
    a = input()
    if a != "":
        print("奖励箱:默认关闭,输入1开启,其他保持默认")
        a = input()
        if a == "1":
            money += 15000
            house = "火柴盒"
        print("世界类型:输入1改变设置,其他保持默认")
        a = input()
        if a == "1":
            b = 0
            world_set = ["正常","自定义"]
            while True:
                b += 1
                print("改变世界设置:输入任意按键确定并退出,直接enter下一个")
                print("世界类型:",world_set[b % 2])
                a = input()
                if a != "":
                    world_set = world_set[b % 2]
                    break
            if world_set != "正常":
                if world_set == "自定义":
                    print("设置矿物丰度(0至100,默认50)")
                    while True:
                        a = input()
                        try:
                            if -1 < int(a) < 101:
                                break
                        except:
                            print("数字有误")
                    mineral_abundance = int(a)
                    print("设置村庄生成(默认生成,输入1关闭")
                    a = input()
                    if a == "1":
                        village_built = False
                    else:
                        village_built = True
                    print("设置要塞数量(下限、默认7个,上限100个)")
                    a = str(a)
                    while True:
                        a = input()
                        try:
                            if 6 < int(a) < 101:
                                break
                        except:
                            print("数字有误")
                    number_of_stronghold = int(a)
    else:
        mineral_abundance = 50
        number_of_stronghold = 7
        village_built = True
    print(admin + "进入了游戏")
    print("您好,您来到这个世界的目的……想干什么就干什么吧")
    print("您可以砍树,挖矿,买东西,探索等")
    print("接下来请选职业")
    print("职业有:")
    print("1.渔夫,2.农民,3.矿工,4.伐木工,5.乞丐(现在可选职业)")
    print("6.科学家,7.工程师,8.将领,9.国王")
    while job != "1" and job != "2" and job != "3" and job != "4" and job != "5":
        job = input("请输入正确的,现在可选的职业:")
job = int(job)
def an(a,c):
    r1 = randint(0,100)
    if r1 <= a:
        return c
    else:
        return 0
def qus(goods,price):
    global money,ask
    print("商品:",goods)
    print("价格:",price)
    print("购买请输入 1")
    ask = input()
    if ask == "1":
        ask = input("输入数量:")
        try:
            a = int(ask)
            money -= int(price) * int(ask)
        except:
            print("输入的不是数字")
        return True
    else:
        return False
def food_qus(goods,price):
    global money,ask,SV
    print("食品:",goods)
    print("价格:",price)
    print("购买请输入 1")
    ask = input()
    if ask == "1":
        while True:
            ask = input("输入数量(输入full以补满,输入exit退出)")
            try:
                if "exit" in ask:
                    break
                if "full" in ask:
                    ask = 100 - SV
                    money -= int(price) * int(ask)
                    print("食用了",ask,"个")
                    break
                else:
                    money -= int(price) * int(ask)
                    print("已食用")
                    break
            except:
                print("输入的[数字]不太对劲")
        return True
    else:
        return False
def monster_kill():
    a = an(30,1)
    if a == 1:
        screen.append(admin + "被僵尸杀死了")
        print(admin + "被僵尸杀死了")
    if a == 0:
        a = an(40,1)
        if a == 1:
            print(admin + "被骷髅射手杀死了")
            screen.append(admin + "被骷髅射手杀死了")
        else:
            a = an(60,1)
            if a == 1:
                print(admin + "爆炸了")
                screen.append(admin + "爆炸了")
            else:
                a = an(30,1)
                if a == 1:
                    print(admin + "试图逃离僵尸时试图在岩浆里游泳")
                    screen.append(admin + "试图逃离僵尸时试图在岩浆里游泳")
                if a == 0:
                    a = an(40,1)
                    if a == 1:
                        print(admin + "试图逃离骷髅射手时试图在岩浆里游泳")
                        screen.append(admin + "试图逃离骷髅射手时试图在岩浆里游泳")
                    else:
                        print(admin + "试图逃离苦力怕时时试图在岩浆里游泳")
                        screen.append(admin + "试图逃离苦力怕时时试图在岩浆里游泳")
    HP = 0
def E_qus(made_thing,IQ_need,price):
    global IQ,money
    if IQ_need >= IQ:
        print("可制造",made_thing)
        a = input("要制造请输入1")
        if a == 1:
            print("已制造")
            IQ += 1
            money -= price
            money += 10000000
screen.append(admin + "进入了游戏")
while True:
    os.system("cls")
    a = len(screen)
    for i in range(a):
        print(screen[i])
    print("现在是第",day,"天",time_tick/1000,"时")
    print("您有",money,"块钱")
    if money < 0:
        print("请尽快还债!")
    print("您的生命值是",HP)
    if sword:
        print("您拥有防身武器")
    if shield:
        print("您拥有盾牌")
    if armour:
        print("您拥有盔甲")
    print("您的饥饿值是",SV)
    if SV == 0:
        print("请去饭店恢复体力!")
    if sold_village != 0:
        print("您有",sold_village,"个村庄")
    print("您有",CLA,"亩田地")
    print("您的科学进度为",)
    print("接下来您要干什么?")
    print("1.探索,2.挖矿,3.砍树,4.去商/饭店,5.职业技能,6.回收村庄,7.转职跳槽")
    print("输入gamemode查看游戏规则")
    print("输入duty查看职业的用处及达成条件")
    print("输入exit退出并生成新版存档码")
    a = input()
    if a == "1":
        if face_thing == "nothing" or face_thing == "village":
            a = an(70,1)
            if a == 0:
                a = an(30,1)
                if a == 1:
                    a = an(50,1)
                    if a == 1:
                        print("河流!")
                        face_thing = "river"
                    elif a == 0:
                        print("大海!")
                        face_thing = "sea"
                elif a == 0:
                    print("探索了个空气……")
                    face_thing = "nothing"
                time_tick += 1000
            elif a == 1:
                print("发现村庄!")
                a = an(30,1)
                if a == 1:
                    print("走近一看,是个大村庄")
                    print("是否买下?(是为1,否为2)")
                    a = input()
                    if a == "1":
                        money -= 20000
                        day_money += 2000
                        sold_village += 1
                    elif a == "2":
                        big_villages_for_sale += 1
                elif a == 0:
                    print("是否买下?(是为1,否为2)")
                    a = input()
                    if a == "1":
                        money -= 10000
                        day_money += 1000
                        sold_village += 1
                    elif a == "2":
                        villages_for_sale += 1
                    face_thing = "village"
                time_tick += 2000
            time_tick += 4000
        if face_thing == "river":
            print("是否探索下去(是为1,否为2)")
            a = input()
            if a == "1":
                print("有大海!")
                face_thing = "sea"
                time_tick += 8000
            elif a == "0":
                print("又回来了")
                face_thing = "nothing"
                time_tick += 5000
        if face_thing == "sea":
            print("要买船吗?(买为1,不买为2)")
            a = input()
            if a == "1":
                money -= 200
                a = an(20,1)
                if a == 1:
                    print("发现海底神殿!")
                    print("是(1)否(2)探索?")
                    time_tick += 10000
                    a = input()
                    if a == "1":
                        a = an(70,1)
                        if a == 1:
                            print("获得丰厚的报酬")
                            money += 64000
                        if a == 0 and armour == False:
                            print(admin + "被守卫者的魔法杀死了")
                            screen.append(admin + "被守卫者的魔法杀死了")
                            HP = 0
                        else:
                            armour = False
                time_tick += 20000
            face_thing = "nothing"
        SV -= 20
        a = "0"
    if a == "2":
        if mine_time <= 1 or job == 3:
            print("请选择挖矿地点(地狱:1|主世界:2)")
            a = input()
            if a == "2":
                print("准备一套工具！")
                money -= 10000
                a = an(90,1)
                if a == 1:
                    print("获得丰厚的报酬")
                    money += 15000000
                if a == 0 and armour == True:
                    armour = False
                elif a == 0 and shield == True:
                    shield = False
                if a == 0 and armour == False and shield == False:
                    a = an(50,1)
                    if a == 1:
                        print("失足掉入岩浆")
                        screen.append(admin + "试图在岩浆里游泳")
                        HP = 0
                    if a == 0 and sword == False:
                        monster_kill()
                    else:
                        sword = False
                time_tick += 10000
                mine_time += 1
                SV -= 30
            if a == "1":
                print("准备一套工具！")
                money -= 20000
                a = an(90,1)
                if a == 1:
                    print("获得丰厚的报酬")
                    money += 20000000
                elif a == 0 and armour == False and shield == False:
                    a = an(50,1)
                    if a == 1:
                        print("失足掉入岩浆")
                        screen.append(admin + "试图在岩浆里游泳")
                        HP = 0
                    if a == 0 and sword == False:
                        a = an(30,1)
                        if a == 1:
                            screen.append(admin + "被岩浆怪杀死了")
                            print(admin + "被岩浆怪杀死了")
                        if a == 0:
                            a = an(40,1)
                            if a == 1:
                                print(admin + "被骷髅射手杀死了")
                                screen.append(admin + "被骷髅射手杀死了")
                            else:
                                a = an(60,1)
                                if a == 1:
                                    print(admin + "被烈焰人杀死了")
                                    screen.append(admin + "被烈焰人杀死了")
                                else:
                                    a = an(30,1)
                                    if a == 1:
                                        print(admin + "试图逃离岩浆怪时试图在岩浆里游泳")
                                        screen.append(admin + "试图逃离岩浆怪时试图在岩浆里游泳")
                                    if a == 0:
                                        a = an(40,1)
                                        if a == 1:
                                            print(admin + "试图逃离骷髅射手时试图在岩浆里游泳")
                                            screen.append(admin + "试图逃离骷髅射手时试图在岩浆里游泳")
                                        else:
                                            print(admin + "试图逃离烈焰人时试图在岩浆里游泳")
                                            screen.append(admin + "试图逃离烈焰人时试图在岩浆里游泳")
                        HP = 0
                elif sword:
                    sword = False
                elif shield:
                    shield = False
                else:
                    armour = False
                time_tick += 14000
                mine_time += 1
                SV -= 40
        else:
            print("今日挖矿次数已用完")
        a = "0"
    if a == "3":
        if tree_time < 3 or job == 4:
            print("准备一套工具!")
            money -= 100
            for i in range(10):
                if randint(1,3) == 1:
                    print("丰产林!")
                    money += 2500
                money += 7500
            time_tick += 1000
        else:
            print("今日砍树次数已用完")
        a = "0"
    if a == "4":
        print("商店:")
        if job != 5:
            if house == "":
                print("房屋区")
                a = qus("1.豪华大别墅","10000000")
                if a:
                    house = "豪华大别墅"
                a = qus("2.郊区平房","200000")
                if a:
                    house = "郊区平房"
                a = qus("3.市区公寓","800000")
                if a:
                    house = "市区公寓"
            else:
                a = input("要换房请输入1")
                if a == "1":
                    print("房屋区")
                    a = qus("1.豪华大别墅","10000000")
                    if a:
                        house = "豪华大别墅"
                    a = qus("2.郊区平房","200000")
                    if a:
                        house = "郊区平房"
                    a = qus("3.市区公寓","800000")
                    if a:
                        house = "市区公寓"
        print("日用品区")
        print("要买脑补品请输入1")
        a = input()
        if a == "1":
            a = qus("脑白银",1000000)
            if a:
                IQ += 3
            a = qus("脑白金",1500000)
            if a:
                IQ += 5
            a = qus("脑黄金",2000000)
            if a:
                IQ += 10
        if SV < 100:
            print("食物区")
            a = food_qus("1.面包","5")
            if a:
                print("已食用")
            a = food_qus("2.牛奶","5")
            if a:
                print("已食用")
            a = "0"
        if sword == False or shield == False or armour == False:
            print("盔甲区")
            a = qus("1.剑","100")
            if a:
                sword = True
            a = qus("2.盾","150")
            if a:
                shield = True
            a = qus("3.盔甲","10000")
            if a:
                armour = True
    if a == "5":
        if job == 1:
            print("钓鱼!")
            money -= 100
            if an(10,1) == 1:
                print("鱼跑了!")
            else:
                if an(50,1) == 1:
                    print("钓到了几条鱼")
                    money += randint(4,10)*10
                else:
                    print("钓到稀有物品!")
                    money += randint(1,5)*100
            time_tick += 1000
        if job == 2:
            print("需要购买种子")
            while True:
                try:
                    a = int(input("数量:"))
                    break
                except:
                    print("请输入数值")
            money -= a * 10
            print("还需要购买锄头")
            money -= 100
            CLA += int(a)
            time_tick += 5000
        if job == 3:
            print("你的职业技能是挖矿")
        if job == 4:
            print("你的职业技能是砍树")
        if job == 5:
            a = randint(0,100)
            if 0 <= a < 30:
                print("乞讨成功")
                money += 50000
            if 30 <= a < 60:
                print("乞讨失败")
            else:
                a = randint(1,8)
                if a == 1:
                    print("你被人家打死了")
                    screen.append(admin + "被一户人家打死了")
                    HP = 0
                elif a == 2:
                    print("你被人家打了四分之一的血量")
                    HP -= 25
                    if HP <= 0:
                        screen.append(admin + "被一户人家打死了")
                        HP = 0
                elif a == 3 or a == 4:
                    print("你被人家打了二分之一的血量")
                    HP -= 50
                    if HP <= 0:
                        screen.append(admin + "被一户人家打死了")
                        HP = 0
                elif a == 5 or a == 6:
                    print("你被警察罚款100元")
                    money -= 100
                else:
                    print("你被警察罚款50元")
                    money -= 50
        if job == 6:
            if IQ >= 130:
                if TP == 0:
                    print("可以学习小学知识")
                    a = input("要学习需要输入1")
                    if a == 1:
                        print("已学习")
                        IQ += 1
                        TP = 1
                        money -= 1000
                        money += 100000
                        time_tick += 200000
            if IQ >= 135:
                if TP == 1:
                    print("可以学习中学知识")
                    a = input("要学习需要输入1")
                    if a == 1:
                        print("已学习")
                        IQ += 1
                        TP = 2
                        money -= 2500
                        money += 100000
                        time_tick += 400000
            if IQ >= 138:
                if TP == 2:
                    print("可以学习大学知识")
                    a = input("要学习需要输入1")
                    if a == 1:
                        print("已学习")
                        IQ += 1
                        TP = 3
                        money -= 5000
                        money += 100000
                        time_tick += 800000
            if IQ >= 140:
                if TP == 3:
                    print("可以学习顶级知识")
                    a = input("要学习需要输入1")
                    if a == 1:
                        print("已学习")
                        IQ += 1
                        TP = 4
                        money -= 10000
                        money += 100000
                        time_tick += 2000000
            if IQ >= 155:
                if TP == 4:
                    print("可以研究微观世界")
                    a = input("要研究需要输入1")
                    if a == 1:
                        print("已研究")
                        IQ += 5
                        TP = 5
                        money += 1000000
                        money -= 5000000
            if IQ >= 170:
                if TP == 5:
                    print("可以研究纳米技术")
                    a = input("要研究需要输入1")
                    if a == 1:
                        print("已研究")
                        IQ += 5
                        TP = 6
                        money += 1000000
                        money -= 100000000
            if IQ >= 180:
                if TP == 6:
                    print("可以研究曲率")
                    a = input("要研究需要输入1")
                    if a == 1:
                        print("已研究")
                        IQ += 5
                        TP = 7
                        money += 1000000
                        money -= 100000000
            if IQ >= 190:
                if TP == 7:
                    print("可以研究维度")
                    a = input("要研究需要输入1")
                    if a == 1:
                        print("已研究")
                        IQ += 5
                        TP = 8
                        money += 1000000
                        money -= 100000000
            if IQ >= 195:
                if TP == 8:
                    print("可以研究光学")
                    a = input("要研究需要输入1")
                    if a == 1:
                        print("已研究")
                        IQ += 5
                        TP = 9
                        money += 1000000
                        money -= 5000000000
            if IQ >= 200:
                if TP == 9:
                    print("可以研究冬眠")
                    a = input("要研究需要输入1")
                    if a == 1:
                        print("已研究")
                        IQ += 5
                        TP = 10
                        money += 1000000
                        money -= 500000000
            if IQ >= 210:
                if TP == 10:
                    print("可以研究强互作用力")
                    a = input("要研究需要输入1")
                    if a == 1:
                        print("已研究")
                        IQ += 5
                        TP = 11
                        money += 1000000
                        money -= 800000000
            if IQ >= 250:
                if TP == 11:
                    print("可以研究星系社会学")
                    a = input("要研究需要输入1")
                    if a == 1:
                        print("已研究")
                        IQ += 5
                        TP = 12
                        money += 1000000
                        money -= 500000000
            if IQ >= 320:
                if TP == 12:
                    print("可以研究安全声明")
                    a = input("要研究需要输入1")
                    if a == 1:
                        print("已研究")
                        IQ += 5
                        TP = 13
                        money += 1000000
                        money -= 10000000000
            if IQ >= 470:
                if TP == 13:
                    print("可以研究物体二向")
                    a = input("要研究需要输入1")
                    if a == 1:
                        print("已研究")
                        IQ += 5
                        TP = 14
                        money += 1000000
                        money -= 80000000000
            if IQ >= 490:
                if TP == 14:
                    print("可以研究物体一向")
                    a = input("要研究需要输入1")
                    if a == 1:
                        print("已研究")
                        IQ += 5
                        TP = 15
                        money += 1000000
                        money -= 120000000000
            if IQ >= 500:
                if TP == 15:
                    print("可以研究物体零向")
                    a = input("要研究需要输入1")
                    if a == 1:
                        print("已研究")
                        IQ += 5
                        TP = 16
                        money += 1000000
                        money -= 600000000000
            if IQ >= 500:
                if TP == 16:
                    print("可以研究时空旅行")
                    a = input("要研究需要输入1")
                    if a == 1:
                        print("已研究")
                        IQ += 5
                        TP = 17
                        money += 1000000
                        money -= 12000000000
            if IQ >= 500:
                if TP == 17:
                    print("可以研究平行宇宙穿越")
                    a = input("要研究需要输入1")
                    if a == 1:
                        print("已研究")
                        IQ += 5
                        TP = "MAX"
                        money += 1000000
                        money -= 100000000000
        if job == 7:
            E_qus("望远镜",140,200000)
            E_qus("卫星",145,200000000)
            E_qus("火箭",145,300000000)
            E_qus("行星系飞船",150,3000000000)
            E_qus('"飞刃"',155,5000000)
            E_qus("恒星系飞船",160,5000000000)
            E_qus("太空城",190,7000000000)
            E_qus("冬眠仪器",200,100000000)
            E_qus("智子",200,6000000000)
            E_qus("生态循环系统",200,500000000)
            E_qus("光速飞船",220,8000000000)
            E_qus("强互作用力材料",220,10000000000)
            E_qus("水滴",225,9000000000)
            E_qus("引力波天线",240,5000000000)
            E_qus("低光速黑洞",250,1000000000)
            E_qus("光粒",470,100000000000)
            E_qus("二向箔",480,250000000000)
        if job == 8:
            a = randint(1,360)
            if 1 <= a < 200:
                print("胜利")
                HP -= 20
                if HP <= 0:
                    print("您被对手杀死了")
                    screen.append(admin+"被敌方杀死了")
                PT += 20
                money += 20000000
            else:
                print("失败")
                print("您被对手杀死了")
                screen.append(admin + "被敌方杀死了")
                HP = 0
        if job == 9:
            print("您想干什么都行")
        a = "0"
    if a == "6":
        if villages_for_sale == 0 and big_villages_for_sale == 0:
            print("没有待售村庄")
        else:
            money -= villages_for_sale * 10000
            day_money += villages_for_sale * 1000
            print("已购",villages_for_sale,"个小村庄")
            money -= big_villages_for_sale * 20000
            day_money += big_villages_for_sale * 2000
            print("已购",big_villages_for_sale,"个大村庄")
        a = "0"
    if a == "7":
        if IQ < 140:
            job_list.remove("7.工程师")
        if IQ < 140 and PT < 70:
            job_list.remove("6.科学家")
        if IQ < 140 and PT < 85:
            job_list.remove("8.将领")
        if IQ < 300 and money <= 100000000000:
            job_list.remove("9.国王")
        for a in job_list:
            print(a)
        while True:
            try:
                a = input("请输入跳槽目标的编号")
                a = int(a)
                if 0 <= a <= 5:
                    print("跳槽成功!")
                    job = a
                    a = True
                if len(job_list) > 5:
                    if len(job_list) == 7:
                        if 5 < a <= 7:
                            print("跳槽成功!")
                            job = a
                            a = True
                    if len(job_list) >= 8:
                        if a == 8:
                            print("跳槽成功!")
                            job = a
                            a = True
                    if len(job_list) == 9:
                        if a == 9:
                            print("跳槽成功!")
                            job = a
                            a = True
                if a != True:
                    print("跳槽失败")
                if a:
                    break
            except:
                print("跳槽失败")
    if a == "gamemode":
        print("砍树三次一天")
        print("挖矿一次一天")
        print("探索无限制")
        print("一天24小时,24000刻")
        print("饱食度,生命值最高100")
        print("饱食度为100时自动恢复生命值")
        print("饱食度为0时会扣除生命值")
        print("当钱为负数时会有利息50%")
        print("没有房时18时过后会有20%几率去世,30%几率生命值减去40")
    if a == "duty":
        print("渔夫:")
        print("  职业用处:")
        print("    可以花费100元下一次钩,45%钓上普通鱼(40至100元),45%钓上稀有物品(100至500元),10%空钩")
        print("  职业要求:")
        print("    无")
        a = input()
        print("农民:")
        print("  职业用处:")
        print("    用10元/个的种子+100元的锄头能使日收入增加100")
        print("  职业要求:")
        print("    无")
        a = input()
        print("矿工:")
        print("  职业用处:")
        print("    一天挖矿无次数限制")
        print("  职业要求:")
        print("    无")
        a = input()
        print("伐木工:")
        print("  职业用处:")
        print("    一天砍树无次数限制")
        print("  职业要求:")
        print("    无")
        a = input()
        print("乞丐:")
        print("  职业用处:")
        print("    去乞讨,有很大几率失败")
        print("  职业要求:")
        print("    无")
        a = input()
        print("科学家:")
        print("  职业用处:")
        print("    研究科学问题")
        print("  职业要求:")
        print("    IQ >= 140,威信 >= 70")
        a = input()
        print("工程师:")
        print("  职业用处:")
        print("    制作东西")
        print("  职业要求:")
        print("    IQ >= 140")
        a = input()
        print("将领:")
        print("  职业用处:")
        print("    打仗")
        print("  职业要求:")
        print("    IQ >= 140,威信 >= 85")
        a = input()
        print("国王:")
        print("  职业用处:")
        print("    想干什么干什么,无法干体力活")
        print("  职业要求:")
        print("    IQ >= 300 money >= 100000000000(一千亿元)")
        a = input()
    if house == "" or house == "nothing":
        print("你没有房子,晚上很危险哟")
        if time_tick >= 19000 or time_tick < 5000:
            print("到了晚上,是(1)否挖三填一?")
            a = input()
            if a != "1":
                a = randint(1,100)
                if 0 < a < 20:
                    if armour == False and shield == False and sword == False:
                        HP = 0
                    else:
                        HP -= 30
                elif 20 < a < 50:
                    if armour == False and shield == False and sword == False:
                        HP -= 40
                    else:
                        HP -= 10
                        if sword:
                            sword = False
                        elif shield:
                            shield = False
                        else:
                            armour = False
                else:
                    print("侥幸逃脱一劫")
                if HP == 0:
                    monster_kill()
            else:
                print("在下面度过了一夜")
                time_tick = 5000
    if HP <= 0:
        a = "die"
    if SV <= 0:
        if not armour:
            HP -= 20
        else:
            HP -= 10
        SV = 0
        if HP <= 0 and a != "die":
            print(admin+"饿死了")
            screen.append(admin+"饿死了")
    if SV >= 100:
        SV = 100
        HP += 20
    if HP > 100:
        HP = 100
    if HP <= 0:
        money = 0
        HP = 100
        SV = 100
        PT = 0
        face_thing = "nothing"
        bag = {}
        sword = False
        shield = False
        armour = False
    if time_tick >= 24000:
        time_tick -= 24000
        mine_time = 0
        tree_time = 0
        day += 1
        money += day_money + CLA*100
    if money < 0:
        money += money * 0.5
    if a == "exit":
        if house == "":
            house = "nothing"
        print("存档码:")
        print(str(day_money)+" "+str(money)+" "+str(job)+"#"+str(CLA)+"#"+str(TP)+" "+admin+" "+str(day)+" "+str(house)+" ahfuiehaihfrhsufcha")
        print("请复制上一行(最好粘贴在一个TXT里)")
        break
    time.sleep(1)
a = input()