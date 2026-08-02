import webbrowser


password = input("enter password : ")

if password == "abcde":
    print(" search for key ")
    buttom = int(input())
    if(buttom == 1):
        url = input("enter url : ")
        webbrowser.open(f"https://www.{url}.com")
    else:
        print("blah blah")
    
else :
    print("try again")
    
