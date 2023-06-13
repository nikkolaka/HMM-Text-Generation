from Markov import train_trigram, generate_text


def main():
    # train on hounds of baskerville
    file = open("houn.txt", "r")
    text = file.read()
    model = train_trigram(text)
    print("I am reading Hounds of Baskerville")
    print("Model now has " + str(len(model)) + " keys\n")

    # train on the sign of the four
    file = open("sign.txt", "r")
    text = file.read()
    model = train_trigram(text, model)
    print("I am reading The Sign of the Four")
    print("Model now has " + str(len(model)) + " keys\n")


    # train on a study in scarlet
    file = open("stud.txt", "r")
    text = file.read()
    model = train_trigram(text, model)
    print("I am reading A Study in Scarlet")
    print("Model now has " + str(len(model)) + " keys\n")


    # train on the valley of fear
    file = open("vall.txt", "r")
    text = file.read()
    model = train_trigram(text, model)
    print("I am reading The Valley of Fear")
    print("Model now has " + str(len(model)) + " keys\n")

    # train on moby dick
    file = open("moby.txt", "r", errors="ignore")
    text = file.read()
    model = train_trigram(text, model)
    print("I am reading Moby Dick")
    print("Model now has " + str(len(model)) + " keys\n")

    generated_string = generate_text(model, 2000)
    print(generated_string)
    file = open("Readme.txt", "a")
    file.write(generated_string)


main()
