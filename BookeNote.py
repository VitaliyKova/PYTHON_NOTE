
from Note import Note
from datetime import datetime

class Book(object):
    def __init__(self): # Инициализация класса с созданием листа для хранения заметок
        self.new_list = []


    def recordingToFile(self): # Запись в файл JSon в режиме чтение и перезапись
        with open('notes.json', 'w', encoding='utf-8') as f:
            for note in self.new_list:
                f.write(f"{note.date}\nID: {note.id}\nTitle: {note.title}\nBody: {note.body}\n\n")

    def savingData(self):
        try:
            with open('notes.json', 'r', encoding='utf-8') as f:
                count = len(f.readlines())
                with open('notes.json', 'r', encoding='utf-8') as f1:
                    i = 0
                    while i < count:
                        line = f1.readline()
                        if line == '\n':
                            i+=1
                        else:
                            save_note = Note("","")
                            save_note.date = datetime.strptime(line.rstrip('\n'), '%Y-%m-%d %H:%M:%S.%f')
                            i += 1
                            save_note.id = int(f1.readline().lstrip('ID: ').rstrip('\n'))
                            i += 1
                            save_note.title = f1.readline().lstrip('Title: ').rstrip('\n')
                            i += 1
                            save_note.body = f1.readline().lstrip('Body: ').rstrip('\n')
                            i += 1
                            self.new_list.append(save_note)
                    self.recordingToFile()        
        except:
            new_file = open('notes.json', 'w', encoding='utf-8')
            new_file.close
            print("\nСоздайте вашу первую заметку! :)")
        else:
            print("\nДанные загружены...\nСинхронизация завершена...\n")           
                    
                    

                     
                                 
            