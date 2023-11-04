from UserOperation import UserOperation
class Start(object):
    menu = ("\nMENU\n"
         +"1 -> Создать заметку\n"
         +"2 -> Удалить заметку по ID\n"
         +"3 -> Редактировать заметку\n"
         +"4 -> Выборка заметок по дате создания\n"
         +"5 -> Показать весь список заметок\n"
         +"6 -> Выбрать заметку по названию\n"
         +"7 -> Выход\n\n"
         +"Выберите пункт меню и введите его номер -> ")
    
    menuEdit = ("\n1 -> редактировать заголовок\n"
                +"2 -> редактировать тело заметки\n"
                +"3 -> выйти в главное меню\n\n"
                +"Выберите пункт меню и введите его номер -> ")
    
    newText = ("\nВведите новый текст -> ")
    searchId = ("\nВведите ID заметки -> ")
    
    def __init__(self):
        self.main = UserOperation()

    def programStart(self):
        flag = True
        while flag:
            user_input = int(input(self.menu))
            if user_input == 1:
                self.main.newNote()
                continue
            elif user_input == 2:
                self.main.allPrintNote()
                searchNote = int(input(self.searchId))
                if(self.main.printNoteId(searchNote) == True):
                    self.main.delete(searchNote)
                    continue
                else: continue
            elif user_input == 3:
                flag2 = True
                self.main.allPrintNote()
                searchNote = int(input(self.searchId))
                if(self.main.printNoteId(searchNote) == True):
                    while flag2:
                        comand = int(input(self.menuEdit))
                        if comand == 1:
                            newTitle = input(self.newText)
                            self.main.editTitle(searchNote,newTitle)
                            continue
                        elif comand == 3:
                            flag2 = False
                else: continue        
            if user_input == 7:
                flag = False    
