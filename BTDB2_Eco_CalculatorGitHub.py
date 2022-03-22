#name Gp(grouped) Sp(spaced) Re(red bloon) Ye(yellow bloons) SpYe spaced yellow bloons
from decimal import Decimal
import matplotlib.pyplot as plt
eco_rate = 6 
bloons = {
    'Test'  : {'cost' : -1,       'eco' : 1,      'speed' : 2,       'debut' : (0,0)},
    'GpRed' : {'cost' : -15,      'eco' : 1,      'speed' : 0.8,     'debut' : (1,11)},
    'SpBlu' : {'cost' : -15,      'eco' : 1.3,    'speed' : 1.5,     'debut' : (1,2)},
    'GpBlu' : {'cost' : -25,      'eco' : 1.5,    'speed' : 0.6,     'debut' : (3,13)},
    'SpGre' : {'cost' : -15,      'eco' : 1.2,    'speed' : 1.25,    'debut' : (2,4)}, 
    'GpGre' : {'cost' : -35,      'eco' : 1.5,    'speed' : 0.42,    'debut' : (5,17)},
    'SpYel' : {'cost' : -25,      'eco' : 1.8,    'speed' : 1.25,    'debut' : (3,6)},
    'GrYel' : {'cost' : -40,      'eco' : 1.7,    'speed' : 0.2,     'debut' : (7,19)},
    'SpPin' : {'cost' : -28,      'eco' : 1.8,    'speed' : 1.05,    'debut' : (4,8)},
    'GpPin' : {'cost' : -65,      'eco' : 2.4,    'speed' : 0.2,     'debut' : (9,50)},
    'SpWhi' : {'cost' : -30,      'eco' : 2,      'speed' : 0.9,     'debut' : (5,9)},
    'GpWhi' : {'cost' : -65,      'eco' : 2.5,    'speed' : 0.3,     'debut' : (10,21)},
    'SpBla' : {'cost' : -35,      'eco' : 2,      'speed' : 0.75,    'debut' : (6,9)},
    'GpBla' : {'cost' : -80,      'eco' : 3,      'speed' : 0.32,    'debut' : (10,25)},
    'SpPur' : {'cost' : -70,      'eco' : 4,      'speed' : 1.6,     'debut' : (8,10)},
    'GpPur' : {'cost' : -115,     'eco' : 2.5,    'speed' : 0.175,   'debut' : (11,50)},
    'SpZeb' : {'cost' : -60,      'eco' : 3,      'speed' : 0.6,     'debut' : (9,10)},
    'GpZeb' : {'cost' : -120,     'eco' : 2.5,    'speed' : 0.24,    'debut' : (11,29)},
    'SpLea' : {'cost' : -60,      'eco' : 4,      'speed' : 2,       'debut' : (10,11)},
    'GpLea' : {'cost' : -160,     'eco' : 4,      'speed' : 0.6,     'debut' : (12,50)},
    'SpRai' : {'cost' : -80,      'eco' : 3,      'speed' : 0.35,    'debut' : (12,13)},
    'GpRai' : {'cost' : -250,     'eco' : 4,      'speed' : 0.4,     'debut' : (14,50)},
    'SpCer' : {'cost' : -150,     'eco' : 4,      'speed' : 0.9,     'debut' : (14,15)},
    'GpCer' : {'cost' : -400,     'eco' : 1.8,    'speed' : 0.24,    'debut' : (16,50)},
    'SpMOA' : {'cost' : -1200,    'eco' : 0,      'speed' : 3,       'debut' : (18,19)},
    'GpMOA' : {'cost' : -1200,    'eco' : 0,      'speed' : 0.5,     'debut' : (20,50)},
    'SpBFB' : {'cost' : -2500,    'eco' : -50,    'speed' : 3.5,     'debut' : (20,21)},
    'GpBFB' : {'cost' : -2500,    'eco' : -50,    'speed' : 0.6,     'debut' : (22,50)},
    'SpZOM' : {'cost' : -7000,    'eco' : -200,   'speed' : 6,       'debut' : (22,23)},
    'GpZOM' : {'cost' : -7000,    'eco' : -200,   'speed' : 1,       'debut' : (24,50)},
    'SpDDT' : {'cost' : -5000,    'eco' : -300,   'speed' : 1.4,     'debut' : (26,27)},
    'GpDDT' : {'cost' : -6000,    'eco' : -600,   'speed' : 0.6,     'debut' : (28,50)},
    'SpBAD' : {'cost' : -15000,   'eco' : -800,   'speed' : 7,       'debut' : (30,31)},
    'GpBAD' : {'cost' : -15000,   'eco' : -800,   'speed' : 1,       'debut' : (32,50)},
}
def decimal(number):
    return Decimal(str(number))

def find_bloons(round):
    bloonslist = []
    for i in bloons:
        if round >= bloons[i]['debut'][0] and round <= bloons[i]['debut'][1]:
            bloonslist.append(i)
    return bloonslist
rounds_list = []

def payback_efficiency(round):
    payback_efficiency = []
    for bloon in find_bloons(round):
        payback_efficiency.append([bloon, '{:.2f}'.format(bloons[bloon]['cost'] * -1 /decimal(bloons[bloon]['eco']))])
    return payback_efficiency

def return_on_invest(bloon):
    return '{:.3f}'.format(decimal(bloons[bloon]['eco']/bloons[bloon]['cost'] * -1))

def eco_per_sec(name):
    return decimal(bloons[name]['eco'])/decimal(bloons[name]['speed'])

def get_eco_projection(name, rotations, starting_chash, starting_eco):
    bloon = bloons[name]    
    bloon_speed = bloon['speed']    
    bloon_cost = bloon['cost']
    bloon_eco = bloons[name]['eco']
    money_list = [starting_chash]
    eco_list = [starting_eco]
    round_list = [0]
    bloon_list = []
    time = 0
    time_increment = decimal(0.01)

    def addBloon(time = 0):
        eco_list.append(eco_list[-1] + bloon_eco)     
        money_list.append(money_list[-1] + bloon_cost)
        bloon_list.append([bloon, decimal(bloon_speed)])
        round_list.append(rotation + time/6)

    for rotation in range(rotations):        

        while money_list[-1] >= -bloon_cost and len(bloon_list) < 6:
            addBloon()

        time = decimal(0)

        while time < 6 and len(bloon_list) > 0:
            time = time + time_increment

            bloon_list[0][1] = decimal(bloon_list[0][1]) - decimal(time_increment)
            if bloon_list[0][1] <= 0:
                del bloon_list[0]

            if money_list[-1] >= -bloon_cost and len(bloon_list) < 6 and time < 6:
                addBloon(time)                                        
        round_list.append(rotation + 1)                           
        money_list.append(int(eco_list[-1]) + money_list[-1]) 

    return eco_list, money_list, round_list

def projector(name, rotations, starting_chash, starting_eco):
    projection = get_eco_projection(name, rotations, starting_chash, starting_eco)
    plt.plot( projection[2], projection[1], label = name)
    plt.legend(loc = "upper center")
    plt.title(name)
    plt.ylabel("Money")
    plt.xlabel("Rotations")

print("All of the bloons in round 5 are:", find_bloons(5))
print("The payback efficiency(cost/eco) for all bloons in round 5:", payback_efficiency(5))
print("This is the return on investment(eco/cost) for Grouped Reds:", return_on_invest('GpRed'))
print("Eco per second(eco/speed) for Grouped Reds:", eco_per_sec('GpRed'))
projector('GpRed', 20, 100, 50)
plt.show()
