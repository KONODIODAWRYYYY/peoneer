'''
    Файл вспомогательных функций и списков, для работы с БД
    и представляниями 
'''

days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]

classes = [ 10000*x+ord(y) for x in range(5,10) for y in "АБВГ"] +\
[10000*x+ord(y) for x in [10,11] for y in "АБ"]

def decode_course(course):
    ch = chr(course%10000)
    num = str(course)[:-4]
    return num+ch

def decode_serialized_data(lsns, serd_lsns):
    for i in range(len(lsns)):
        serd_lsns.data[i]["course"] = decode_course( lsns[i].course )
        serd_lsns.data[i]["room"] = lsns[i].room.decode_number()
        serd_lsns.data[i]["day"] = days[ serd_lsns.data[i]["day"] ]

def decode_query_data (lsns):
    context = []
    for i in range( len(lsns) ):
        lsn = {
            'name'   : lsns[i].name,
            'course' : decode_course(lsns[i].course),
            'time'   : lsns[i].time,
            'room'   : lsns[i].room.decode_number(),
            'day'    : days [lsns[i].day],
        }
        context.append( lsn )
    return context