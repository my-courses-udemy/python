
def read_phrases():
    file = open('/home/fundalap-nh48/SANTIAGO/CURSOS UDEMY/PYTHON/BOT MESSENGER/phrases.txt', 'r')

    files = file.readlines()
    file.close()
    return files