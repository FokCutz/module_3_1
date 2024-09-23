calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    len_str = len(string)
    up = string.upper()
    low = string.lower()
    tuple1 = len_str , up , low
    return tuple1

def is_contains(string, list_ti_search):
    count_calls()
    tuple2 = string.lower() in (s.lower() for s in list_ti_search)
    return tuple2


print(string_info('Абобус'))
print(string_info('amogus'))
print(string_info('among us'))
print(is_contains('Amogus' , ['amoGUS', 'among us' , 'abobus']))
print(is_contains('Антон' , ['Антуан', 'АНТОНИО' , 'Энтони']))
print(is_contains('Влад' , ['Владислав', 'вЛАд' , 'ладик']))
print(calls)