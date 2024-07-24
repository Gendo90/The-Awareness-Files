# output file with repeating text

# outputs a file named filename with the prefix text and repeated text
def outputFile(filename, prefix, text, num_repeats):
    text_to_file = prefix 
    for i in range(num_repeats):
        text_to_file += text

    text_to_file = text_to_file.strip()

    f = open(filename, "w")
    f.write(text_to_file)
    f.close()


if __name__ == "__main__":
    print("Filename? ")
    filename = input() 
    print("Prefix? ")
    prefix = input()
    print("Repeat Text? ")
    text = input()
    print("Number of Repeats (int)? ")
    num_repeats = int(input())

    outputFile(filename, prefix, text, num_repeats)
