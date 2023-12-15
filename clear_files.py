import os

#Пути к проектам
project1_path = "/home/admuser/TEST/"
project2_path = "/home/admuser/TEST2/"

#Расширения файлов для удаления
extensions = ['.txt', '.csv', 'bad_files.js', '.bad_files', '3']
extensions2 = ['.txt', 'bad_files.js', '.bad_files', '3']

def delete_files_with_extensions(directory, extensions):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                file_path = os.path.join(root, file)
                print("Удален файл:", file_path )
                os.remove(file_path)
                
def delete_dirs_with_extensions(directory, extensions):
    for root, dirs, files in os.walk(directory):
        for dir in dirs:
            if any(dir.endswith(ext) for ext in extensions):
                dir_path = os.path.join(root, dir)                
                if os.path.isdir(dir_path) and len(os.listdir(dir_path))==0:
                    print("Удалена директория:", dir_path )
                    os.rmdir(dir_path)                

def main():
    #Удаление файлов в проекте 1
    delete_files_with_extensions (project1_path, extensions)
    delete_dirs_with_extensions (project1_path, extensions)

    #Удаление файлов в проекте 2
    delete_files_with_extensions (project2_path, extensions)
    delete_dirs_with_extensions (project2_path, extensions)
    
    print("Операция завершена!")

if __name__ == "__main__":
    main()