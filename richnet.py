def convert_to_digidip(original_link):
//change the return to add your own affiliate conversion link and delete this text
return "https://go.skimresources.com?id=100269X1558466&xs=1&url=" + original_link

while True:
    original_link = input("Please enter a website link: ")
    digidip_link = convert_to_digidip(original_link)
    print("The digidip link is: " + digidip_link)
    user_input = input("Enter 'r' to reset, 'e' to exit: ")
    if user_input.lower() == 'e':
        break
    elif user_input.lower() != 'r':
        print("Invalid input")
