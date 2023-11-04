from Note import Note
from BookeNote import Book
class UserOperation(object):
    def __init__(self): # Инициализатор текущего класса
        self.new_book = Book() # Иниацилизируем класс хранения заметок и записью в файл
        self.new_book.savingData() # Перезаписываем старые данные в новый лист для удобства редактирования.

    def newNote(self): # Метод создания новой заметки в виде класса с полями
        title = input("\nВведите заголовок заметки: ")
        body = input("Введите тело замети: ")
        new_note = Note(body, title)
        self.new_book.new_list.append(new_note) # Добавляем заметку в лист, для удобства дальнейшей работы сними
        self.new_book.recordingToFile() # Перезаписываем файл с заметками

    def delete(self,id): # Метод удаления заметки по ID
        for note in self.new_book.new_list:
            if note.id == id:
                self.new_book.new_list.remove(note) #Удаляем из списка
                print("\nУспешно сохранено!\n")
            self.new_book.recordingToFile() #Перезаписываем файл

    def editTitle(self, id,newValue):  #метод редактирования Заголовка заметки по ID
        for note in self.new_book.new_list:
            if note.id == id:
                note.title = newValue # Перезаписывается поле заголовок с новым значением
                print("\nУспешно сохранено!\n")
            self.new_book.recordingToFile()# Перезапись файла

    def allPrintNote(self): # Вывод в консоль всех заметок
        for note in self.new_book.new_list:
            print(f"\n{note.date}\nID: {note.id}\nTitle: {note.title}\nBody: {note.body}\n\n")
          
    def printNoteId(self, searchId):  # Поиск заметки по ID с последующим выводом в консоль (Возвращает True если ID найден и False в обратном случае)
        for note in self.new_book.new_list:
            if note.id == searchId:  
                print(f"\n{note.date}\nID: {note.id}\nTitle: {note.title}\nBody: {note.body}\n\n")
                return True
            else: continue            
        print("Заметка не найдена!")
        return False

    

                


