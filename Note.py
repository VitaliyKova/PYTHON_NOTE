from datetime import datetime
class Note(object):
    
    def __init__(self, body, title): # Инициализация класса с полями (Конструктор Заметки)
        self.date = datetime.now() # Присваивание текущей даты и времени
        self.id = id(self.date) # Присваивание уникального ID
        self.body = body # Тело заметки
        self.title = title # Заголовок заметки