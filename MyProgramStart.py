from UserOperation import UserOperation
class Start(object):
    menu = ("\nMENU\n"
         +"1 -> Создать заметку\n"
         +"2 -> Удалить заметку по ID\n"
         +"3 -> Редактировать заметку\n"
         +"4 -> Выборка заметок по дате создания\n"
         +"5 -> Показать весь список заметок\n"
         +"6 -> Выход\n\n"
         +"Выберите пункт меню и введите его номер -> ")
    
    menuEdit = ("\n1 -> редактировать заголовок\n"
                +"2 -> редактировать тело заметки\n"
                +"3 -> выйти в главное меню\n\n"
                +"Выберите пункт меню и введите его номер -> ")
    
    newText = ("\nВведите новый текст -> ")
    searchId = ("\nВведите ID заметки -> ")
    searchDate = ("\nВведите дату (в формате ДД-ММ-ГГГГ) для выборки заметок -> ")
    
    def __init__(self): # Инициализатор текущего класса
        self.main = UserOperation()

    def programStart(self): # Метод определяющий поведение программы, который зависит от выбора пользователя
        flag = True
        while flag: # Запускаем цикл до остановки его пользователем
            user_input = int(input(self.menu))
            if user_input == 1: # Создание заметки
                self.main.newNote()
                continue
            elif user_input == 2: # Удалить заметку по ID
                self.main.allPrintNote() # выводим все существующие для выбора
                searchNote = int(input(self.searchId))
                if(self.main.printNoteId(searchNote) == True): # ЕСли заметка с заданым id существует, то она удаляется
                    self.main.delete(searchNote) 
                    continue
                else: continue
            elif user_input == 3: # Редактировать заметку по ID
                flag2 = True
                self.main.allPrintNote()
                searchNote = int(input(self.searchId))
                if(self.main.printNoteId(searchNote) == True): # ЕСли заметка с заданым id существует
                    while flag2: # Дополнительный цикл для выбора редактируемого поля
                        comand = int(input(self.menuEdit))
                        if comand == 1: # Редактирование заголовка заметки
                            newTitle = input(self.newText)
                            self.main.editTitle(searchNote,newTitle)
                            continue
                        if comand == 2: # Редактирование тела заметки
                            newTitle = input(self.newText)
                            self.main.editBody(searchNote,newTitle)
                            continue
                        elif comand == 3: # Останавливаем цикл(Выход в основное меню)
                            flag2 = False
                else: continue        
            elif user_input == 4: # Выборка заметок по дате создания
                search_date = input(self.searchDate)
                self.main.date_search(search_date)
                continue
            elif user_input == 5: # Вывод в консоль всех заметок
                self.main.allPrintNote()
            if user_input == 6: # Останавливаем цикл(Выход из программы)
                flag = False    
