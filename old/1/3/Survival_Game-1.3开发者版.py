from random import*
from turtle import*
from time import*
import os
os.system("title Survival_Game 1.3")
os.system("color b")
a = input("输入存档码(第一次进入游戏请忽视,请勿试图伪造存档码,以免造成游戏崩溃):")
if " ahfuiehaihfrhsufcha" in a:
    a.replace(" ahfuiehaihfrhsufcha","")
    b = a.split(" ")
    try:
        if b[5] == "nothing":
            b[5] = ""
        day_money = int(b[0])
        money = int(b[1])
        job = int(b[2])
        admin = b[3]
        day = int(b[4])
        house = b[5]
    except:
        print("请勿伪造存档码,以免游戏崩溃!")
        a = True
else:
    a = True
if a == True:
    day = 1
    money = 0
    house = ""
    job = 0
    day_money = 0
    admin = ""
    while admin == "":
        admin = input("请输入用户名:")
    print(admin + "进入了游戏")
    print("您好,您来到这个世界的目的是生存下去")
    print("您可以:")
    print("砍树,挖矿,买东西,探索等")
    print("接下来请选职业")
    print("职业有:")
    print("1.渔夫,2.农民,3.矿工,4.伐木工")
    job = input("请输入正确的职业:")
if job != "1" or job != "2" or job != "3" or job != "4":
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
    print("商品:",goods)
    print("价格:",price)
    print("购买请输入 1")
    ask = input()
    if ask == "1":
        ask = input("输入数量:")
        money -= int(price) * int(ask)
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
            ask = input("输入数量(输入full以补满")
            if ask == "full":
                ask = 100 - SV
                money -= int(price) * int(ask)
            else:
                money -= int(price) * int(ask)
        return True
    else:
        return False
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
    if sword == True:
        print("您拥有防身武器")
    if shield == True:
        print("您拥有盾牌")
    if armour == True:
        print("您拥有盔甲")
    print("您的饥饿值是",SV)
    if SV == 0:
        print("请去饭店恢复体力!")
    print("接下来您要干什么?")
    print("1.探索,2.挖矿,3.砍树,4.去商/饭店,5.职业技能,6.回收村庄")
    print("输入gamemode查看游戏规则")
    print("输入exit退出并生成存档码")
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
                    money += 128000
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
                    money += 260000
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
                elif sword == True:
                    sword = False
                elif shield == True:
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
            for i in range(2):
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
        if house == "":
            print("房屋区")
            a = qus("1.豪华大别墅","10000000")
            if a == True:
                house = "豪华大别墅"
            a = qus("2.郊区平房","200000")
            if a == True:
                house = "郊区平房"
            a = qus("3.市区公寓","800000")
            if a == True:
                house = "市区公寓"
        else:
            a = input("要换房请输入1")
            if a == "1":
                print("房屋区")
                a = qus("1.豪华大别墅","10000000")
                if a == True:
                    house = "豪华大别墅"
                a = qus("2.郊区平房","200000")
                if a == True:
                    house = "郊区平房"
                a = qus("3.市区公寓","800000")
                if a == True:
                    house = "市区公寓"
        if SV < 100:
            print("食物区")
            a = food_qus("1.面包","5")
            if a == True:
                print("已食用")
            a = food_qus("2.牛奶","5")
            if a == True:
                print("已食用")
            a = "0"
        if sword == False or shield == False or armour == False:
            print("盔甲区")
            a = qus("1.剑","100")
            if a == True:
                sword = True
            a = qus("2.盾","150")
            if a == True:
                shield = True
            a = qus("3.盔甲","10000")
            if a == True:
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
                    money += randint(40,100)
                else:
                    print("钓到稀有物品!")
                    money += 500
            time_tick += 1000
        if job == 2:
            print("需要购买种子")
            a = input("数量:")
            money -= int(a) * 10
            print("还需要购买锄头")
            money -= 100
            CLA += int(a)
            time_tick += 5000
        else:
            print("这个职业没有主动技能")
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
    if a == "gamemode":
        print("砍树三次一天")
        print("挖矿一次一天")
        print("探索无限制")
        print("一天24小时")
        print("饱食度,生命值最高100")
        print("饱食度为100时自动恢复生命值")
        print("饱食度为0时会扣除生命值")
        print("当钱为负数时会有利息50%")
        print("没有房时18时过后会有20%几率去世,30%几率生命值减去40")
    if house == "":
        a = randint(1,100)
        if 0 < a < 20:
            if armour == False and shield == False and sword == False:
                HP == 0
            else:
                HP -= 50
        if 20 < a < 50:
            if armour == False and shield == False and sword == False:
                HP -= 40
            else:
                HP -= 20
                if sword == True:
                    sword = False
                elif shield == True:
                    shield = True
                else:
                    armour = True 
        if HP == 0:
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
                    print(admin + "爆炸了")
                    screen.append(admin + "爆炸了")
    if HP <= 0:
        a = "die"
    if SV <= 0:
        if armour == False:
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
    if a == "exit":
        if house == "":
            house = "nothing"
        print("存档码:")
        print(str(day_money)+" "+str(money)+" "+str(job)+" "+admin+" "+str(day)+" "+str(house)+" ahfuiehaihfrhsufcha")
        print("请复制上一行(最好粘贴在一个TXT里)")
        break
    sleep(1)
a = input()