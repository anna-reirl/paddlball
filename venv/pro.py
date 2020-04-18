# class MyClass:
#     def set(self,n):
#         self.num=n
#     def get(self):
#         print('Значение поля:',self.num)
#     def __init__(self,n=0):
#         self.set(n)
#         print('Создан экземпляр класса')
#         self.get()
# a=MyClass()
# b=MyClass(100)

# деструктор
# class MyClass:
#     def __init__(self):
#         print('Hello everyone')
#     def __del__(self):
#         print('Goodbye everyone')
# print('Проверяем работу деструктора')
# obj=MyClass()
# print('Экземпляр класса создан. Удаляем его')
# del obj
# print('Выполнение программы завершено')

# поле объекта класса
# class MyClass:
#     name='Класс MyClass'
#     def set(self,n):
#         self.nickname=n
#     def get(self):
#         print('Значение поля:',self.nickname)
#     def __init__(self,n):
#         self.set(n)
#         print('Создан экземпляр класса')
#         self.get()
# green=MyClass('Зеленый')
# print('Принадлженость:',green.name)
# red=MyClass('Красный')
# print('Принадлженость:',red.name)
# MyClass.name='Здесь могла быть ваша реклама'
# print('Спрашивает Красный:',red.name)
# print('Спрашивает Зеленый:',green.name)

# добавление и удаление полей
# class MyClass:
#     pass
# A=MyClass()
# B=MyClass()
# A.first='Экземпляр А'
# B.second='Экземпляр В'
# MyClass.total='Класс MyClass'
# print(A.total,'->',A.first)
# try:
#     print(A.second)
# except:
#     print('Такого поля у экземпляра А нет')
# print(B.total,'->',B.second)
# try:
#     print(B.first)
# except AttributeError:
#     print('Такого поля у экземпляра В нет')
# del MyClass.total
# try:
#     print(A.total)
# except AttributeError:
#     print('Такого поля нет')
# try:
#     print(B.total)
# except AttributeError:
#     print('Такого поля нет')
# del A.first
# try:
#     print(A.first)
# except AttributeError:
#     print('Такого поля у экземпляра А нет')

# from tkinter import *
# root=Tk()
#
# c=Canvas(root, width=200, height=200, bg='white')
# c.pack()
#
# # c.create_line(10,10,190,50)
# # c.create_line(100,180,100,60,fill='green',
# #               width=5, arrow=LAST, dash=(10,2),
# #               activefill='lightgreen',
# #               arrowshape='10 20 10')
#
# c.create_rectangle(10,10,190,60)
# c.create_rectangle(60,80,140,190,fill='yellow',outline='green',
#                    width=3,activedash=(5,4))
# root.mainloop()

from tkinter import *
import random
import time

class Ball:
    def __init__(self, canvas,color):
        self.canvas=canvas
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,245,100)
        self.canvas_height=self.canvas.winfo_height()
        starts=[-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x=starts[0]
        self.y=-3
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y=3
        if pos[3]>=self.canvas_height:
            self.y=-3
        if pos[0]<=0:
            self.x=3
        if pos[2]>=self.canvas_width:
            self.x=-3

tk=Tk()
tk.title('PaddleBall')
tk.resizable(0,0)
tk.wm_attributes('-topmost',1)
canvas=Canvas(tk,width=500,height=400,bd=0, highlightthickness=0)
canvas.pack()
tk.update()

ball=Ball(canvas,'red')

while 1:
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

tk.mainloop()