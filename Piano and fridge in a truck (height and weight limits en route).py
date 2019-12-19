# Вы - водитель грузовика с открытым кузовом. В кузове два груза: пианино и холодильник.
# Пианино необходимо доставить в институт, холодильник в общежитие.
# В каждое из этих мест ведет отдельная дорога, начинающаяся от перекрестка,
# на котором Вы стоите, других дорог в мире нет. Известно, что по дороге в институт
# есть мост, на котором действует ограничение максимальной допустимой массы автомобиля с грузом,
# а по дороге в общежитие есть туннель с ограничением высоты.
# Требуется определить, возможно ли доставить грузы или нет
# (разумеется, сгружать их, где попало, Вам запрещено).
# На вход подается 8 чисел натуральных чисел (каждое < 100), каждое в новой строке,
# в следующем порядке: вес грузовика без груза, высота платформы кузова (на которой стоят грузы),
# вес пианино, высота пианино, вес холодильника, высота холодильника,
# максимальный допустимый вес на мосту, максимальная допустимая высота в туннеле.
# Примечание: пианино и холодильник заведомо возвышаются над кабиной грузовика,
# т.е. высоту кабины можно в расчет не принимать.
# Вывести YES если доставка возможна и NO в противном случае.

truck_weight = int(input())
platform_height = int(input())
piano_weight = int(input())
piano_height = int(input())
fridge_weight = int(input())
fridge_height= int(input())
bridge_weight_limit = int(input())
tunnel_height_limit = int(input())

if truck_weight + piano_weight + fridge_weight <= bridge_weight_limit:
    if platform_height + fridge_height <= tunnel_height_limit:
        print("YES")
    else:
        print("NO")
else:
    if platform_height + fridge_height <= tunnel_height_limit and platform_height + piano_height <= tunnel_height_limit:
        if truck_weight + piano_weight <= bridge_weight_limit:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
