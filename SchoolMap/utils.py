def decoder (rooms, roomserd):
    for i in range (len(rooms)):
        roomserd.data[i]["number"] = rooms[i].decode_number()