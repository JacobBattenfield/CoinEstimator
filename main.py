def ChooseSystem():
    print("This Program Helps Determine The Number Of Coins You Have Given A Certain Weight")
    print("It Will Also Help You Find How Many Coin Rolls To Obtain.")
    print("Would You Like To Proceed In Imperial(I) Or Metric(M)? Or Would You Like To Quit(Q).")
    UserResponse = input("Type (I) (M) or (Q) To Proceed: ").lower()
    if(UserResponse=='i'):
        Tabulate("Pounds");
    elif(UserResponse=='m'):
        Tabulate("Grams")
    elif(UserResponse=='q'):
        return
    else:
        print()
        print("INVALID OPTION, RESETTING");
        ChooseSystem()
def Tabulate(type):
    penny = input("How Many "+type+ " Of Pennies Do You Have?: ")
    nickel = input("How Many "+type+ " Of Nickles Do You Have?: ")
    dime = input("How Many "+type+ " Of Dimes Do You Have?: ")
    quarter = input("How Many "+type+ " Of Quarters Do You Have?: ")
    halfdollar = input("How Many "+type+ " Of Half Dollars Do You Have?: ")
    if type == "Pounds":
        amount = [round(float(penny)/.0068),round(float(nickel)/.011),round(float(dime)/.005),round(float(quarter)/.0125),round(float(halfdollar)/.025)]
        print(f"You Have {amount[0]} Pennies | {amount[1]} Nickels | {amount[2]} Dimes | {amount[3]} Quarters | {amount[4] } Half-Dollars")
        print(f"You Would Need {round(amount[0]/50)} Penny Rolls | {round(amount[1]/40)} Nickle Rolls | {round(amount[2]/50)} Dime Rolls | {round(amount[3]/40)} Quarter Rolls | {round(amount[4]/20)} Half-Dollar Rolls")
        total = ((amount[0]*.01)+(amount[1]*.05)+(amount[2]*.10)+(amount[3]*.25)+(amount[4]*.50));
        print(f"Your Total Money Is About ${total}")
    if type == "Grams":
        amount = [round(float(penny)/2.5),round(float(nickel)/5),round(float(dime)/2.268),round(float(quarter)/5.67),round(float(halfdollar)/11.34)]
        print(f"You Have {amount[0]} Pennies | {amount[1]} Nickels | {amount[2]} Dimes | {amount[3]} Quarters | {amount[4] } Half-Dollars")
        print(f"You Would Need {round(amount[0]/50)} Penny Rolls | {round(amount[1]/40)} Nickle Rolls | {round(amount[2]/50)} Dime Rolls | {round(amount[3]/40)} Quarter Rolls | {round(amount[4]/20)} Half-Dollar Rolls")
        total = ((amount[0]*.01)+(amount[1]*.05)+(amount[2]*.10)+(amount[3]*.25)+(amount[4]*.50));
        print(f"Your Total Money Is About ${total}")
def main():
    ChooseSystem()
if __name__ == '__main__':
    main();
