# TrickyTaskFromILocked
Выполнить программу на Распберри ПИ (язык Python) .

Задача: разбить экран на 4ре сетки: (размер не важен) 

-в первую : запись любого текстового значения (язык – русский),

 второе – начинается отсчет времени,

 третий -  число А

четвертое – число Б

При нажатии на клавиатуре (можно использовать GPIO и кнопки подключены к ним) кнопки Q – начинается основная логика программы – старт отсчета времени (2 мин) при окончании времени – программа останавливается в стартовый режим.

После старта отсчета времени – случайным образом выбирается число (от 0 до 20) и число А принимает это значение и водится на экран.

При отсчете времени ждем нажатия кнопок A, S, D, F –при нажатии на кнопку зачисляется 1,2,3 и 4 очка (согласно последовательности). И присваивается число Б  (которое тоже выводится на экран).

Если число А и Б равно – назначается новое число  А . число Б обнуляется– и начисляются 50 балов

Если А меньше Б – назначается новое число А, число Б обнуляется – и снимется 50 балов.

И так продолжается до тех пор пока не кончится обратный отсчет. Если он кончился то в число А и Б выводится (и мигает) число Балов накопленных за время игры .

Решение
-------------------------
В условиях отсутствия Raspberry Pi программа реализована следствами библиотеки tkinter.

<a href="url"><img src="https://github.com/aTasja/TrickyTaskFromILocked/blob/master/Frame.png" align="left" height="250" width="300"></a>

