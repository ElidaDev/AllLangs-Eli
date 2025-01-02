ui = input("Guess what? ")

while(ui!="what" and ui!="wat"):
    ui = input("Guess what? ")
print("Nevermind...")

ui = input("say what? ")
answers = ["huh", "what", "?"]

while(not(ui.lower() in answers)):
    ui = input("Try again! ")