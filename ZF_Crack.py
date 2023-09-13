from tkinter import *

class Window:
    def __init__(self, init_window_name):
        self.init_window_name = init_window_name

    def init_window(self):
        self.init_window_name.title("正方解密工具")
        self.init_window_name.geometry('260x75+10+10')

        # Key
        self.init_key_lable = Label(self.init_window_name, text="Key")
        self.init_key_lable.grid(row=0, column=0)
        # KeyEntry
        self.init_key_text = Entry(self.init_window_name, width=20)
        self.init_key_text.grid(row=0, column=2)
        self.init_key_text.insert(0,"Encrypt01")

        # Secret
        self.init_secret_lable = Label(self.init_window_name, text="密文")
        self.init_secret_lable.grid(row=1, column=0)
        # SecretEntry
        self.init_secret_text = Entry(self.init_window_name, width=20)
        self.init_secret_text.grid(row=1, column=2)

        # Pwd
        self.init_pwd_lable = Label(self.init_window_name, text="明文")
        self.init_pwd_lable.grid(row=2, column=0)
        # PwdEntry
        self.init_pwd_text = Entry(self.init_window_name, width=20)
        self.init_pwd_text.grid(row=2, column=2)

        # Button
        self.init_button = Button(self.init_window_name, width=10, height=3, text="解密", command=self.crack)
        self.init_button.grid(row=0, column=3, rowspan=3)

        # Front
        self.init_window_name.attributes("-topmost", True)

    def crack(self):
        self.init_pwd_text.delete(0,END)
        pwdhash = self.init_secret_text.get()
        key = self.init_key_text.get()
        if pwdhash and key:
            len_passwd = len(pwdhash)
            len_key = len(key)
            pwdhash = pwdhash[: len_passwd//2][::-1] + pwdhash[len_passwd//2 :][::-1]
            passwd = ''
            Pos = 0
            for i in range(len_passwd):
                Pos %= len_key
                Pos += 1
                strChar = pwdhash[i] 
                KeyChar = key[Pos-1]
                ord_strChar = ord(strChar)
                ord_KeyChar = ord(KeyChar)
                if not 32 <= (ord_strChar ^ ord_KeyChar) <= 126 or not 0 <= ord_strChar <= 255:
                    passwd += strChar
                else:
                    passwd += chr(ord_strChar ^ ord_KeyChar)
            self.init_pwd_text.insert(0, passwd)
            print(passwd)
        else:
            messagebox.showinfo("提示","请检查输入")
            print(f'key={key}, secret={secret}')

    
def start_GUI():
    init_window = Tk()
    Win = Window(init_window)
    Win.init_window()
    init_window.mainloop()


if __name__ == '__main__':
    start_GUI()
    # 测试secret: juyi'v21ei