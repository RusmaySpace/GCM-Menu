from colorama import *

init(autoreset=True)

def Vibor2():
    print("\n\nТы выбрал 7-ой пункт" + Fore.LIGHTCYAN_EX + " \"Информация\"" + Fore.RESET + ". Что конкретно ты хотешь узнать? \n")
    print("\n1. Команда GuildCraftsMen.")
    print("2. О разработчике.")
    print("3. Где найти наши проекты?\n")
    print(Fore.LIGHTRED_EX + "Если ты напишешь в поле ввода букву вместо числа, то программа закроется!\n" + Fore.RESET)
    global a2
    a2 = int(input(Fore.RESET + "Введи запрос, который тебя интересует (номер пункта).." + Fore.LIGHTCYAN_EX))
    if a2 == 2:
        print(Fore.LIGHTWHITE_EX +"\n\nYou" + Fore.LIGHTRED_EX + "Tube" + Fore.RESET + ": GuildCraftsMen")
        print(Fore.BLUE + "VK" + Fore.RESET + ": @rusmayxd")
        print(Fore.LIGHTMAGENTA_EX + "Discord" + Fore.RESET + ": RusmayXD (#9999)")
        print(Fore.LIGHTCYAN_EX + "Telegram" + Fore.RESET + ": Rusmay")
        Commands2()
    elif a2 == 1:
        print("\nНАША КОМАНДА:\n")                                                                                                                 
        print(Fore.LIGHTCYAN_EX + "Dev & Director " + Fore.RESET + "— RusmayXD.")
        print(Fore.LIGHTGREEN_EX + "Designers " + Fore.RESET + "— Kotodens, RusmayXD.")
        print(Fore.YELLOW + "Testers - GCM STUDIO" + Fore.RESET)
        Commands2()
    elif a2 == 3:
        print("\nГде найти наши проекты? Всё очень просто." + Fore.LIGHTGREEN_EX +" Проекты храняться на проверенных нами сайтах:" + Fore.RESET)
        print(Fore.RESET)
        print("1. https://mody-minecraft.ru/")
        print("2. https://minecraft-inside.ru/")
        print("3. https://www.curseforge.com/\n")
        print("Перейдя на один из сайтов, просто введи название проекта, который хочешь найти.")
        print("P.S. Вовсе не обязательно вводить/копировать всю ссылку в браузер, " + Fore.LIGHTGREEN_EX + "достаточно списать окончание сайта." + Fore.RESET)
        print("Например mody-minecraft.ru")
        Commands2()
    else:
        print("\nЯ не способен обработать твой запрос. Либо ты ввёл его неправильно, либо с пробелами, либо я тупой.")
        Vibor2()

def skoro():
    print(Fore.RESET + "\nДанный запрос ещё в разработке. Следи за процессом его создания в дискорд-сервере и/или ВК GCM Dev",GCM)
    print("Ссылка на дискорд-сервер: https://discord.gg/UsJDHNk37v")
    Commands()

def Commands2():  
    print(Fore.RESET + "\n\nКоманды:\n")
    print(Fore.RESET + "Чтоб вернуться в основное лобби, напиши — " + Fore.LIGHTCYAN_EX + "\"меню\"" + Fore.RESET + ".")
    print(Fore.RESET + "Если ты хочешь выбрать другой пункт информации — пропиши команду " + Fore.LIGHTCYAN_EX + "\"вернуться\"" + Fore.RESET + ".")
    print(Fore.RESET + "Если ты закончил работу, введи слово " + Fore.LIGHTCYAN_EX + "\"конец\" " + Fore.RESET + "для полного закрытия программы.\n")
    end = str(input(Fore.RESET + "Что дальше? Введи команду: " + Fore.LIGHTRED_EX))
    if end in "меню":
        welcome()
    elif end in "вернуться":
        Vibor2()
    elif end in "конец":
        print(Fore.LIGHTGREEN_EX + "\nСпасибо за тест моей программы, до новых встреч!\n")
    else:
        print(Fore.RED + "\nЯ не понял твою команду, возможно ты ошибся(лась) в её написании, или поставил(а) лишний пробел." + Fore.RESET) 
        print(Fore.RED + "Доступные команды: меню и конец.\n" + Fore.RESET)
        print(Fore.RESET + "Попробуй еще раз!")
        Commands()

def Commands():
    print(Fore.RESET + "\nКоманды:\n")
    print(Fore.RESET + "Чтоб вернуться в основное лобби, напиши — " + Fore.LIGHTCYAN_EX + "\"меню\"" + Fore.RESET +".")
    print(Fore.RESET + "Если ты закончил работу, введи слово " + Fore.LIGHTCYAN_EX + "\"конец\""  + Fore.RESET +  " для закрытия программы.\n")
    end = str(input(Fore.RESET + "Что дальше? Введи команду: " + Fore.LIGHTRED_EX))
    if end in "меню":
        welcome()
    elif end in "конец":
        print(Fore.LIGHTGREEN_EX + "\nСпасибо за тест моей программы, до новых встреч!\n")
    else:
        print(Fore.RED + "\nЯ не понял твою команду, возможно ты ошибся(лась) в её написании, или поставил(а) лишний пробел." + Fore.RESET)
        print(Fore.RED + "Доступные команды: меню и конец.\n" + Fore.RESET)
        print(Fore.RESET + "Попробуй еще раз!")
        Commands()

def BW():
    print("\nТы выбрал 5-ый пункт " + Fore.LIGHTCYAN_EX + "\"Better Weapons Mod\"" + Fore.RESET + ".")
    print("Данный мод добавляет различные артефакты, оружия и структуры.")
    print("Подробная информация и гайд можно найти в 7-ом пункте \"Информация\"")
    Commands()

def Exteleon():
    print("\nТы выбрал 1-ый пункт " + Fore.LIGHTCYAN_EX + "\"Exteleon Mod\"" + Fore.RESET + ".")
    print("\nМодификация добавляет сюжет, а также связанные с ним структуры, предметы, блоки и так далее.") 
    print("В моде присутствуют два измерения (нужно создать порталы) и три биома (можно найти гуляя по верхнему миру).\n")                                                                                                                                   # сделать
    print("Первое измерение создается с помощью \"кристальных блоков\", которые можно получить с помощью")
    print("соединения обсидиана и алмаза, активатором служит специальный посох, который можно получить из гнилой листвы и палок.\n")
    print("Второе измерение можно создать с помощью \"камней времени\", которые создаются с помощью кирпича и ванильных часов,") 
    print("активатором служат \"утерянные часы\", которые можно найти в структурах, или создать с помощью ванильных часов и кирпичей.\n")
    print("P.S. Трейлер проекта доступен на официальном ютуб канале (см. 7-ой пункт " + Fore.LIGHTCYAN_EX + "\"Информация\"" + Fore.RESET + ").")
    Commands()

def SSM():
    print("\nТы выбрал 2-ой пункт " + Fore.LIGHTCYAN_EX + "\"SuperSpeedRun Mod\"" + Fore.RESET + ".")
    print("\nВторая модификация от команды",GCM)
    print("Этот мод предназначен для развлечения, мы не рекомендуем добавлять его в сборки.") 
    print("Мод меняет некоторые крафты и производит свои, полностью меняя механики прохождения игры.")
    print("Подробнее можно узнать в видео-гайде на канале (см. 7-ой пункт" + Fore.LIGHTCYAN_EX + " \"Информация\"" + Fore.RESET + ").")                                                                                                             
    Commands()

def RA():
    print("\nТы выбрал 3-ий пункт " + Fore.LIGHTCYAN_EX + "\"RusmayARTs Mod\"" + Fore.RESET + ".")
    print("\nТретий проект от команды",GCM)
    print("Этот мод добавляет 40 новых картин в твой кубический мир.") 
    print("Подробнее можно узнать в видео-гайде на канале (см. 7-ой пункт" + Fore.LIGHTCYAN_EX + " \"Информация\"" + Fore.RESET + ").")                                                                                                             
    Commands()

def vibor():
    print(Fore.LIGHTRED_EX + "\nЕсли ты напишешь в поле ввода букву вместо числа, то программа закроется!\n" + Fore.RESET)
    global a
    a = int(input(Fore.RESET + "Введи запрос, который тебя интересует (номер пункта).." + Fore.LIGHTCYAN_EX))
    if a == 1:
        Exteleon()
    elif a == 2:
        SSM()
    elif a == 3:
        RA()
    elif a == 4:
        BW()
    elif a == 5 or a == 6:
        skoro()
    elif a == 7:
        Vibor2()
    else:
        print("\nЯ не способен обработать твой запрос. Либо ты ввёл его неправильно, либо с пробелами, либо я тупой.")
        vibor()

def welcome():
    global GCM
    GCM = (Fore.LIGHTBLUE_EX + "GuildCraftsMen")
    global bright
    bright = (Fore.LIGHTGREEN_EX + Style.BRIGHT + "Minecraft")
    global new
    new = (Style.BRIGHT + Fore.LIGHTRED_EX + "{СКОРО}")
    print(Fore.LIGHTYELLOW_EX +  "\nДобро пожаловать в семью",GCM,"| " + Back.LIGHTYELLOW_EX + Fore.BLUE + "By RusmayXD" + Fore.RESET)
    print("\nНаши проекты по игре",bright, "уже здесь! Взгляни:")
    print("1. Мод Exteleon")
    print("2. Мод SuperSpeedRun")
    print("3. Мод RusmayARTs")
    print("4. Мод Better Weapons")
    print("5. Мод Add apples", new)
    print("6. Игра Dungeons Time!", new)
    print("7. Информация.")
    vibor()

welcome()
