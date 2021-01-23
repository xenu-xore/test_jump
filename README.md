SearchingCSV
============

Программа, которая принимает в качестве входных данных два аргумента «путь к каталогу» и «слово»:
    
    root@root:~/: main.py /some_dir/data_dir/ some_value

Первый параметр это путь до каталога, в котором находится csv файлы, файлы в каталоге могут находиться в других 
под каталогах, те структура может быть вложенной, например так:

    data/
      - 1.csv
      filedir1/
        - 2.csv
        - 3.csv
        _filedir1/
          - 4.csv


Requirements
============

* Python 3.5+
* Works on Linux, Windows

Install
=======

Загрузите zip-archive и распакуйте в любом месте или скачайте через оператора git

    git clone https://github.com/xenu-xore/test_jump.git


Documentation
=============

    positional arguments:
      directory             Enter directory name
      word                  Enter searching name
    
    optional arguments:
      -h, --help            show this help message and exit
      --create_dirs CREATE_DIRS [CREATE_DIRS ...]
                            Сreating a chain of stores

Чтобы определить надежность программы, достаточно запустить

    root@root:~/: main.py data AAPL
Если вы хотите отдельно создать директорию и вложенные в нее поддиректории и сгенерировать в них файлы csv. 
(По условию задачи  можно было понять двояко о input data для строк, поэтому на всякий случай есть метод для ввода и флаг --create_dirs)

    root@root:~/: main.py new_data AAPL --create_dirs true

Система сама посчитает среднее значение для сгенерированных файлов csv и передаст в консоль. 
Для более тонкой настройки генерации данных в csv вы можете изменить параметры myData на иные, чтобы посчитать их среднее значение

Если вы все сделали правильно, то ожидаемый результат должен совпасть с условием задачи:

    {'open': 68.096, 'high': 68.863, 'low': 67.107, 'close': 67.753}
