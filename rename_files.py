import os
def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir(r"C:\Users\aman5\Desktop\New folder (2)")
    print(file_list)
    saved_path = os.getcwd()
    print("Current working Directory is "+saved_path)
    os.chdir(r"C:\Users\aman5\Desktop\New folder (2)")
    #(2) for each file, rename filename
    for file_name in file_list:
        print("old Name : "+file_name)
        print("New Name : "+file_name.translate(None, "1234567890"))
        os.rename(file_name,file_name.translate(None, "1234567890"))
        os.chdir(saved_path)


rename_files()
