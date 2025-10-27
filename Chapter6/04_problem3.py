c1 = "Make a Lot Money"
c2 = "Buy Now"
c3 = "Contact me"
c4 = "Telegram link"

message = input("enter a String: ")

if((c1 in message) or (c2 in message) or (c3 in message) or (c4 in message)):
    print("This is a scam")
     
else:
    print("this is not a scam")