n=1
l=[]
while True:
    print("1.Account Opening.\n2.Account Updation.\n3.Diposit in Account.\n4.Withdraw from Account.\n5.Manager folder.")
    x=int(input("enter the no. what you want:"))
    if x==1:
        z=[]
        print("Your Account number is:",n)
        name=input("Enter your name:")
        a=input("Enter customer id.:")
        c=input("Enter branch name:")
        d=input("Enter your address:")
        e=input("Enter IFSE code:")
        f=input("Enter Account type:")
        g=0
        z.append(name)
        z.append(a)
        z.append(c)
        z.append(d)
        z.append(e)
        z.append(f)
        z.append(g)
        l.append(z)
        n=n+1
    elif x==2:
        no=int(input("Enter your Account number:"))
        print("What you want to update")
        print("1.Your name.\n2.Your address.\n3.Account type.")
        y=int(input("Enter the no."))
        xy=l[no-1]
        print(xy)
        if y==1:
            na=input("Enter your new name:")
            xy[0]=na
        elif y==2:
            ad=input("Enter your new Adress:")
            xy[3]=ad
        elif y==3:
            ty=input("Enter your new Account type:")
            xy[-2]=ty
    elif x==4:
        no=int(input("Enter your Account number:"))
        withdraw=int(input("Enter the Amount:"))
        ab=l[no-1]
        cd=ab[-1]
        ammount=cd-withdraw
        ab[-1]=ammount
    elif x==3:
        no=int(input("Enter your Account number:"))
        diposit=int(input("Enter the Amount:"))
        ab=l[no-1]
        cd=ab[-1]
        ammount=cd+diposit
        ab[-1]=ammount
    elif x==5:
        password=input("Enter password to access Manager folder:")
        if password=="abc123":
            print("1.Show total account.\n2.Check the customer names who have transaction more than 10 lakhs per month.\n3.Check the customer names who have transaction less than 500 per month.")
            n=input("enter the no.")
            if n==1:
                print(l)
            elif n==2:
                for i in l:
                    if i[-1]>=10000:
                        print(i)
            else:
                for i in l:
                    if i[-1]<=500:
                        print(i)
        else:
            print("*Wrong Password*\nYou can not access Manager folder.")
    elif x==6:
        break
