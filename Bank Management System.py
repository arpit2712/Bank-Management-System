

# Bank Management System:
'''In this system we are opening accounts of client and do some mathematics as withdraw
the money and deposite the money and etc.'''


def Existing_Customer():
    n=input("Enter A/c number:")
    if(n in data2["A/c"]):
    
        print("🧐🧐🧐🧐🧐")
        print("Record found successfully .")
        print("Choose one option")
        print("1️⃣👉 Check Balance")
        print("2️⃣👉 Withdraw ")
        print("3️⃣👉 Deposite ")

        ch=int(input("Choose any one option:"))
        if(ch==1):
            print("Total Balance=",data2["Balance"])
            print("_"*60)

        elif(ch==2):
            n=int(input("Enter withdraw ammount:"))
            data2["Balance"]=g-n
            print("Current Balance=",data2["Balance"])
           
            print("_"*60)

        elif(ch==3):
            
            n=int(input("Enter deposite amount:"))
            data2["Balance"]=g+n
            print("Current Balance=",data2["Balance"])
            
            print("_"*60)
            
    else:
        print("🧐🧐🧐🧐🧐")
        print("‼️‼️Sorry‼️‼️")
        print("Record does not found....")
        
    

        
print("____________________________________________________")
print("               Bank Management System                ")
print("_____________________________________________________")
print("Choose any one option...")
print("1️⃣👉 New Customer.")
print("2️⃣👉 Existing Customer.")
print("3️⃣👉 Exit.")


while(True):
    
    ch=int(input("Choose any one option:"))
    if(ch==1):
        
        
        a=input("Enter account number:")
        b=input("Enter Name of Customer:")
        c=input("Enter Current address of Customer:")
        d=int(input("Enter Phone Number of Customer:"))
        e=input("Enter Govt. ID(pan/aadhar) of Customer:")
        f=input("Enter A/c-type(saving/current) of Customer:")
        g=int(input("Enter Balance:"))

        
        print("Account Created successfully.")

        data2={"A/c":a,"Name":b,"Address":c,"No.":d,"ID":e,"Type":f,"Balance":g}
        
    elif(ch==2):
        
        Existing_Customer()

    elif(ch==3):
    
        print("😭😭😭😭😭😭")
        exit()

        
    
    
    msg=input("Do you want to continue this loop(y/n):")
    if(msg=="y"):
        print("😁😁😁😁😁")
        continue
    elif(msg=="n"):
        
        print("😭😭😭😭😭😭")
        exit()



