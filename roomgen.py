import random

class rooms:
    class norm:
        tb = {
            "l":False,
            "r":False,
            "t":True,
            "b":True,
        },
        lr = {
            "l":True,
            "r":True,
            "t":False,
            "b":False,
        },
        br = {
            "l":False,
            "r":False,
            "t":False,
            "b":True,
        },
        bl = {
            "l":True,
            "r":False,
            "t":False,
            "b":True,
        },
        tr = {
            "l":False,
            "r":True,
            "t":True,
            "b":False,
        },
        tl = {
            "l":True,
            "r":False,
            "t":True,
            "b":False,
        },
    def generate(count):
        prevroom = ""
        roomnames = ["bl","br","bt","lr","tl","tr"]
        roomlist = [rooms.norm.bl, rooms.norm.br, rooms.norm.tb, rooms.norm.lr, rooms.norm.tl, rooms.norm.tr]
        room = random.randint(1,6)
        roomname = roomnames[room]
        roomdata = roomlist[room]
        prevroom = roomdata
        loop = count
        while loop > 0:
            roomnames = ["bl","br","bt","lr","tl","tr"]
            roomlist = [rooms.norm.bl, rooms.norm.br, rooms.norm.tb, rooms.norm.lr, rooms.norm.tl, rooms.norm.tr]
            
            
            print(room)
            print(roomname)
            print(roomdata)
            c = roomdata.__contains__
            o = prevroom.__contains__
            if c("bl:True") and o("br:True"):
                print("Connection")
                prevroom = roomdata
            room = random.randint(1,6)
            roomname = roomnames[room]
            roomdata = roomlist[room]

rooms.generate(10)
