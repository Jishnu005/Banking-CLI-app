# Bank Management System
import random as r
di = {}
class InsufficientMoney(Exception):
    pass

class Bank:
    def __init__(self, account_no=None ,name=None, password=None, money=0):
        self.__account_no = account_no
        self.__name = name
        self.__password = password
        self.__money = money

    def add_account(self):
        self.__name = input("Enter your full name:")
        self.__password = int(input("Enter a 4-digit Numerric Password:"))
        self.__account_no = r.randint(110000001, 111111111)
        print(f"Welcome {self.__name}, Your account is successfully created.")
        print(f"Your password:{self.__password}", f"And Your AC NO.:{self.__account_no}",sep="\n")

        di[self.__account_no] = self

        with open('management.txt', 'a') as m:
            m.write(f"{self.__account_no},{self.__name},{self.__password},{self.__money}\n")

    def login(self):
            while True:
                print(f"\nWelcome {self.__name}\n")
                d_c = int(input("Want to deposit press '1'\nTo take-out press '2'\nTo check balance press '3'\nExit press '4'\nEnter:"))
                if d_c == 1:
                    # DEPOSIT MONEY
                    dep = int(input("Enter the amount you want to deposit:"))
                    self.__money += dep
                    print(f"Current Balance: ₹{self.__money}")

                    with open('management.txt', 'r') as l:
                        line = l.readlines()
                        """ .readline() makes each line as a element of list('line') with \n(new line)
                        EX: File: 110435931,Jishnu Mangaraj,1212,18000
                                  110435930,Bibhu Mangaraj,1210,10000
                            
                            line(List):['110435931,Jishnu Mangaraj,1212,18000\n',
                                        '110435930,Bibhu Mangaraj,1210,10000\n']
                            """

                    with open('management.txt', 'w') as od:
                        for li in line:
                            l = li.strip().split(',') # .strip() removes the \n at the end.
                            # Ex: l = [110435930,Bibhu Mangaraj,1210,10000]

                            if int(l[0]) == self.__account_no:
                                od.write(f"{self.__account_no},{self.__name},{self.__password},{self.__money}\n")

                            else:
                                od.write(li + '\n')
                    
                elif d_c == 4:
                    # EXIT
                    break
                
                elif d_c == 3:
                    # CHECK MONEY
                    print(f"Your Current Balance is:{self.__money}")
                    
                elif d_c == 2:
                    # TAKE-OUT MONEY
                    cred = int(input("Enter the amount you want to take-out:"))
                    if cred > self.__money:
                        raise InsufficientMoney("Transaction Declined!!!- Your Acount has insufficient balance to provide.")
                    else:
                        self.__money-=cred
                        print(f"Current Balance: ₹{self.__money}")

                        with open('management.txt', 'r') as l:
                            line = l.readlines()
                            """ .readline() makes each line as a element of list('line') with \n(new line)
                            EX: File: 110435931,Jishnu Mangaraj,1212,18000
                                    110435930,Bibhu Mangaraj,1210,10000
                                
                                line(List):['110435931,Jishnu Mangaraj,1212,18000\n',
                                            '110435930,Bibhu Mangaraj,1210,10000\n']
                                """

                        with open('management.txt', 'w') as od:
                            for li in line:
                                l = li.strip().split(',') # .strip() removes the \n at the end.
                                # Ex: l = [110435930,Bibhu Mangaraj,1210,10000]

                                if int(l[0]) == self.__account_no:
                                    od.write(f"{self.__account_no},{self.__name},{self.__password},{self.__money}\n")
                                else:
                                    od.write(li)
                        
                else:
                    print("Wrong Input!!!")
                    return 
            


print("Welcome to Chor Bank:")
while True:
    print("1. To create new account, press 1","2. To log-in to your account press 2",sep="\n")
    a = int(input("Enter:"))

    if a == 1:
        b = Bank()
        b.add_account()

        want = int(input("Want to exit, press 1:"))
        if want == 1:
            break

    elif a==2:
        try:
            ac = int(input("Enter your AC NO.:"))
            pw = int(input("Enter your 4-digit PassWord:"))
            li = []
            with open('management.txt', 'r') as n:
                for line in n:
                    line = line.strip()
                    
                    if not line:
                        continue  # Skip completely empty lines

                    li = line.split(',')
                    if len(li) != 4:
                        continue  # Skip malformed lines
                    if int(li[0]) == ac and int(li[2]) == pw:
                        file = Bank(int(li[0]),li[1],int(li[2]),int(li[3]))
                        file.login()

            # if ac in di:
            #     u = di[ac]
            #     if u.check_password(pw):
            #         u.login()
            #     else:
            #         print("Wrong Password")
            # else:
            #     print("Wrong AC NO.")

        except InsufficientMoney as I:
            print(I)
        want = int(input("Want to exit, press 1:"))
        if want == 1:
            break
