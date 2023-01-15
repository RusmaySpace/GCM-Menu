from colorama import *

init(autoreset=True)

def Vibor2(): # Выбор для третьей глобальной переменной
    print()
    print()
    print("Ты выбрал 4-ый пункт" + Fore.LIGHTCYAN_EX + " \"Информация\"" + Fore.RESET + ". Что конкретно ты хотешь узнать?")
    print()
    print("1. Команда GuildCraftsMens.")
    print("2. О разработчике.")
    print("3. Где найти наши проекты?")
    print()
    print(Fore.LIGHTRED_EX + "Если ты напишешь в поле ввода букву вместо числа, то программа закроется!" + Fore.RESET)
    print()
    global a2
    a2 = int(input(Fore.RESET + "Введи запрос, который тебя интересует (номер пункта).." + Fore.LIGHTCYAN_EX))
    if a2 == 2:
        print()
        print("О РАЗРАБОТЧИКЕ:")
        print()
        print(Fore.LIGHTWHITE_EX +"You" + Fore.LIGHTRED_EX + "Tube" + Fore.RESET + ": GuildCraftsMens")
        print(Fore.BLUE + "VK" + Fore.RESET + ": @rusmayxd")
        print(Fore.LIGHTMAGENTA_EX + "Discord" + Fore.RESET + ": RusmayXD#9626")
        print(Fore.LIGHTCYAN_EX + "Telegram" + Fore.RESET + ": Rusmay")
        Commands2()
    elif a2 == 1:
        print()
        print("НАША КОМАНДА:")
        print()                                                                                                                   
        print(Fore.LIGHTCYAN_EX + "Dev & Director " + Fore.RESET + "— RusmayXD.")
        print(Fore.LIGHTGREEN_EX + "Designers " + Fore.RESET + "— Kotodens, RusmayXD.")
        print(Fore.YELLOW + "Testers " + Fore.RESET + "— Kotodens, K1BORG_666, Burrito.")
        print(Fore.BLUE + "Builders " + Fore.RESET + "— 5ki5l5ler5, RusmayXD.")
        print(Fore.MAGENTA + "Sponsors " + Fore.RESET + "— Cats_Ksuwa.")
        print()
        Commands2()
    elif a2 == 3:
        print()
        print("Где найти наши проекты? Всё очень просто." + Fore.LIGHTGREEN_EX +" Проекты храняться на проверенных нами сайтах:" + Fore.RESET)
        print(Fore.RESET)
        print("1. https://mody-minecraft.ru/")
        print("2. https://minecraft-inside.ru/")
        print("3. https://www.curseforge.com/")
        print()
        print("Перейдя на один из сайтов, просто введи название проекта, который хочешь найти.")
        print("P.S. Вовсе не обязательно вводить/копировать всю ссылку в браузер, " + Fore.LIGHTGREEN_EX + "достаточно списать окончание сайта." + Fore.RESET)
        print("Например mody-minecraft.ru")
        Commands2()
    else:
        print()
        print("Я не способен обработать твой запрос. Либо ты ввёл его неправильно, либо с пробелами, либо я тупой.")
        Vibor2()

def Commands2(): # Команды "меню, выйти, повторить"    
    print()
    print()
    print(Fore.RESET + "Команды:")
    print()
    print(Fore.RESET + "Чтоб вернуться в основное лобби, напиши — " + Fore.LIGHTCYAN_EX + "\"меню\"" + Fore.RESET + ".")
    print(Fore.RESET + "Если ты хочешь выбрать другой пункт информации — пропиши команду " + Fore.LIGHTCYAN_EX + "\"вернуться\"" + Fore.RESET + ".")
    print(Fore.RESET + "Если ты закончил работу, введи слово " + Fore.LIGHTCYAN_EX + "\"конец\" " + Fore.RESET + "для полного закрытия программы.")
    print()
    end = str(input(Fore.RESET + "Что дальше? Введи команду: " + Fore.LIGHTRED_EX))
    if end in "меню":
        welcome()
    elif end in "вернуться":
        Vibor2()
    elif end in "конец":
        print()
        print(Fore.LIGHTGREEN_EX + "Спасибо за тест моей программы, до новых встреч!")
        print()
    else:
        print()
        print(Fore.RED + "Я не понял твою команду, возможно ты ошибся(лась) в её написании, или поставил(а) лишний пробел." + Fore.RESET) 
        print(Fore.RED + "Доступные команды: меню и конец." + Fore.RESET)
        print()
        print(Fore.RESET + "Попробуй еще раз!")
        Commands()

def Commands(): # Команды "меню, выйти"
    print()
    print()
    print(Fore.RESET + "Команды:")
    print()
    print(Fore.RESET + "Чтоб вернуться в основное лобби, напиши — " + Fore.LIGHTCYAN_EX + "\"меню\"" + Fore.RESET +".")
    print(Fore.RESET + "Если ты закончил работу, введи слово " + Fore.LIGHTCYAN_EX + "\"конец\""  + Fore.RESET +  " для закрытия программы.")
    print()
    end = str(input(Fore.RESET + "Что дальше? Введи команду: " + Fore.LIGHTRED_EX))
    if end in "меню":
        welcome()
    elif end in "конец":
        print()
        print(Fore.LIGHTGREEN_EX + "Спасибо за тест моей программы, до новых встреч!")
        print()
    else:
        print()
        print(Fore.RED + "Я не понял твою команду, возможно ты ошибся(лась) в её написании, или поставил(а) лишний пробел." + Fore.RESET)
        print(Fore.RED + "Доступные команды: меню и конец." + Fore.RESET)
        print()
        print(Fore.RESET + "Попробуй еще раз!")
        Commands()

def BW(): # {SKORO}
    print()
    print()
    print(Fore.RESET + "Данный запрос ещё в разработке. Следи за процессом его создания в дискорд-сервере",GCM)
    print("P.S. Дабы получить к нему доступ, обратись в дискорд создателю —> 4-ый пункт.")
    Commands()

def Exteleon(): #Exteleon Mod
    print()
    print()
    print("Ты выбрал 1-ый пункт " + Fore.LIGHTCYAN_EX + "\"Exteleon Mod\"" + Fore.RESET + ".")
    print()
    print("Модификация добавляет сюжет, а также связанные с ним структуры, предметы, блоки и так далее.") 
    print("В моде присутствуют два измерения (нужно создать порталы) и три биома (можно найти гуляя по верхнему миру).")                                                                                                                                   # сделать
    print()
    print("Первое измерение создается с помощью \"кристальных блоков\", которые можно получить с помощью")
    print("соединения обсидиана и алмаза, активатором служит специальный посох, который можно получить из гнилой листвы и палок.")
    print()
    print("Второе измерение можно создать с помощью \"камней времени\", которые создаются с помощью кирпича и ванильных часов,") 
    print("активатором служат \"утерянные часы\", которые можно найти в структурах, или создать с помощью ванильных часов и кирпичей.")
    print()
    print("P.S. Трейлер проекта доступен на официальном ютуб канале (см. 4-ый пункт " + Fore.LIGHTCYAN_EX + "\"Информация\"" + Fore.RESET + ").")
    Commands()

def SSM(): #SuperSpeedRun Mod
    print()
    print()
    print("Ты выбрал 2-ой пункт " + Fore.LIGHTCYAN_EX + "\"SuperSpeedRun Mod\"" + Fore.RESET + ".")
    print()
    print("Вторая модификация от команды",GCM)
    print("Этот мод предназначен для развлечения, мы не рекомендуем добавлять его в сборки.") 
    print("Мод меняет некоторые крафты и производит свои, полностью меняя механики прохождения игры.")
    print("Подробнее можно узнать в видео-гайде на канале (см. 4-ый пункт" + Fore.LIGHTCYAN_EX + " \"Информация\"" + Fore.RESET + ").")                                                                                                             
    Commands()

def vibor(): #Ввод запросов
    print()
    print(Fore.LIGHTRED_EX + "Если ты напишешь в поле ввода букву вместо числа, то программа закроется!" + Fore.RESET)
    print()
    global a
    a = int(input(Fore.RESET + "Введи запрос, который тебя интересует (номер пункта).." + Fore.LIGHTCYAN_EX))
    if a == 1:
        Exteleon()
    elif a == 2:
        SSM()
    elif a == 3:
        BW()
    elif a == 4:
        Vibor2()
    else:
        print()
        print("Я не способен обработать твой запрос. Либо ты ввёл его неправильно, либо с пробелами, либо я тупой.")
        vibor()

def welcome(): # первичное меню
    global GCM
    GCM = (Fore.LIGHTBLUE_EX + "GuildCraftsMens")
    global bright
    bright = (Fore.LIGHTGREEN_EX + Style.BRIGHT + "MineCraft")
    global new
    new = (Style.BRIGHT + Fore.LIGHTRED_EX + "{СКОРО}")
    print()
    print(Fore.LIGHTYELLOW_EX +  "Добро пожаловать в семью",GCM,"| " + Back.LIGHTYELLOW_EX + Fore.BLUE + "v.1.7.1. by RusmayXD" + Fore.RESET)
    print()
    print("Наши проекты по игре",bright, "уже здесь! Взгляни:")
    print("1. Exteleon Mod.")
    print("2. SuperSpeedRun Mod.")
    print("3. BetterWeapons Mod.",new)
    print("4. Информация.")
    vibor()

welcome()