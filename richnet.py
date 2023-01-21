import pyperclip

def convert_to_digidip(original_link):
    return "https://go.skimresources.com?id=100269X1558466&xs=1&url=" + original_link

while True:
    original_link = input("Please enter a website link: ")
    digidip_link = convert_to_digidip(original_link)
    print("Your link is: " + digidip_link)
    user_input = input("Enter 'r' to reset, 'c' to copy link, 'e' to exit: ")
    if user_input.lower() == 'e':
        break
    elif user_input.lower() == 'c':
        pyperclip.copy(digidip_link)
        print("Link copied to clipboard")
    elif user_input.lower() != 'r':
        print("Invalid input")
