import os #import operating system module
def create_file(filename):
    try:
        #use with method then not need to close().
        with open(filename,'x')as f:
            print(f"file name {filename}:create successfully")
    except FileExistsError:
        print(f" file name {filename} already exits")
    except Exception as E:
        print("An Error")
def view_all_files():
    files=os.listdir() #list of current directory
    if not files:
        print("no file found")
    else:
        print("files in directory!")
        for  file in files:
            print(file) # display all file
def delete_file(filename):
    try:
        os.remove[filename] #remove file
        print(f'{filename} has been deleted sucessfully')
    except FileNotFoundError:
        print("file not found")
    except Exception as e:
        print("An error occurred")
def read_file(filename):
    try:
        with open ("simple.txt",'r')as f:
            content=f.read()
            print(f'{filename}:\n{content}')
    except FileNotFoundError:
        print(f"{filename} doesn't exist")
    except Exception as e:
        print("An error occurred!")
def edit_file(filename):
    try:
       with open("simple.txt",'a')as f:
        content=input("Enter data to add=")
        f.write(content+"\n")
        print('content added to {filename} successfully')
    except FileNotFoundError:
        print(f"{filename} doesn't exits!")
    except Exception as e:
        print('An error occurred')
def main():
    while True:
        print("File managemant App")
        print("1:create file")
        print("2:view all file")
        print("3:delete file")
        print("4:read file")
        print("5: Edit file")
        print('6:Exit')
        choice=input("Enter you choice (1-6)")
        if choice=='1':
            filename=input("enter the file name to create=")
            create_file(filename)
        elif choice=='2':
            view_all_files()
        elif choice=="3":
            filename=input("enter the name of file you want to delete=")
            delete_file(filename)
        elif choice=='4':
            filename=input("enter the file name to read=")
            read_file(filename)
        elif choice=='5':
            filename=input("Enter the file name to Edit ")
            edit_file(filename)
        elif choice=='6':
            print("closing the app......")
            break
        else:
            print("invalid syntax")
if __name__=="__main__":
    main()



