# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 17:06:57 2017

@author: A.Shatova
"""
# импорт библиотек
import random
import tkinter as Tk

root = Tk.Tk()
root.title("Пробное задание Шатовой Анастасии")
# создаем текстовый виждет
label_text = Tk.Label(root, font=("Helvetica", 15),  bg='#cffce9', fg='#077647')
label_text['text'] = "Нажатие на клавищу 'Q' начинает игру.\nВремя игры 2 минуты.\nПока не кончится время\n нажимайте на клавиши 'A','S','D' и 'F'!\nУдачи!"
label_text.pack(fill='x')

class Timer():
    ''' класс описывает поведение таймера и ход окончания игры'''
    def __init__(self):
        self.label = Tk.Label(root, height=3, font=("Helvetica", 26), bg = '#affada', fg="#077647") # создаем Label для таймера
        self.label.pack(side="top", fill="both", expand=True) # упаковываем label
        self.timer_running = False  # запущен ли таймер
        self.default_seconds = 120  # изначальное положение(2 мин 00 сек)
        self.timer_seconds = self.default_seconds  # текущее положение таймера, сек
        self.root = root
                     
    def timer_start(self):
        self.timer_running = not self.timer_running  # работа или пауза
        if self.timer_running:  # работа
            self.timer_tick()    

    def timer_reset(self):
        self.timer_running = False  # стоп
        self.timer_seconds = self.default_seconds  # изначальное положение
        self.show_timer()

    def timer_tick(self):
        if self.timer_running and self.timer_seconds:
            self.label.after(1000, self.timer_tick)  # перезапустить через 1 сек          
            self.timer_seconds -= 1 # уменьшить таймер
            self.show_timer()
        elif self.timer_seconds == 0: 
            self.end_game() # закончить игру если время кончилось
            self.show_timer()
    
    def show_timer(self):
        '''отображаем таймер'''
        m = self.timer_seconds//60
        s = self.timer_seconds-m*60
        self.label['text'] = 'ВРЕМЯ %02d:%02d' % (m, s)
        
    def end_game(self):
        ''' заканчиваем игру с окончанием таймера '''
        for i in ['a','s','d','f']: # отвязываем кнопки
            self.root.unbind(i)
        # обнуляем числа, выводим на экран число накопленных баллов,включаем мигание виджетов
        num_a.lable_cofigure('ИГРА ЗАКОНЧЕНА')
        num_b.lable_cofigure(text = '%u'%num_b.score)
        num_a.flashing, num_b.flashing = True, True
        num_a.flash()
        num_b.flash()
        
class Number():
    ''' класс описывает виджет чисел А и Б'''
    def __init__(self):
        self.label = Tk.Label(root, width=15,height=3, font=("Helvetica", 20), bg='#9bf9d1', fg="#077647") # создаем Label для таймера
        self.label.pack(side='left') # упаковываем label
        self.root = root
        self.num = 0 # исходное число 
        self.Values = {'a':1, 's':2, 'd':3, 'f':4} # баллы за нажатие кнопок A S D F
        self.score = 0 # исходное количество баллов
        self.flashing = False # виждет должен мигать?
        
    def lable_cofigure(self, text):       
        self.label.configure(text = str(text)) # изменеие тесктового поля виджета
        
    def flash(self):
        # мигание виджета
        if self.flashing == True:
            bg = self.label.cget("background")
            fg = self.label.cget("foreground")
            self.label.configure(background=fg, foreground=bg)
            self.root.after(250, self.flash)
       
def moveB(event): # генерация числа Б и алгоритм оценки
        if num_b.score != 0:
            moveA()
        num_b.lable_cofigure('') # обнуление числа Б
        num_b.score += num_b.Values[event.char] # увеличение баллов после нажатия на клавиши
        num_b.num = random.randint(1,20) # генерация числа Б
        num_b.lable_cofigure(num_b.num)  # присвоение числа Б
        if num_a.num == num_b.num: # изменение баллов в сзависимости от сравнения чисел А и Б
            num_b.score += 50
        elif num_a.num < num_b.num:
            num_b.score -= 50
#        print num_a.num, num_b.num, num_b.score
        
def moveA(): # генерация числа А
        num_a.label['text'] = ''
        num_a.num = random.randint(1,20)
        num_a.label['text'] = num_a.num 

def start_game(event):
    ''' начинает игру по нажатию на клавишу q'''
    # обнуляем баллы, таймер, мигание, числа   
    num_b.score = 0
    timer.timer_reset() 
    num_a.flashing, num_b.flashing = False, False
    num_a.lable_cofigure('')
    num_b.lable_cofigure('')
    #привязываем кнопки     
    for i in ['a','s','d','f']:
        root.bind(i, moveB)
    # запускаем генерацию числа А и таймер   
    moveA()
    timer.timer_start()

# создаем экземляры классов для виджетов    
timer = Timer()
num_a = Number()
num_b = Number()

# привязываем кнопку старта 'q'      
root.bind('q',start_game)
    
## выводим окна на экран
root.mainloop()