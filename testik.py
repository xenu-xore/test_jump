import os

path = os.getcwd() + "/test/dir1/dir2/"

try:
    os.makedirs(path)
except OSError:
    print("Создать директорию %s не удалось" % path)
else:
    print("Успешно создана директория %s" % path)