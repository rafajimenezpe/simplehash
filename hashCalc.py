def header():
    #https://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=simplehash
    a = """
███████╗██╗███╗   ███╗██████╗ ██╗     ███████╗██╗  ██╗ █████╗ ███████╗██╗  ██╗
██╔════╝██║████╗ ████║██╔══██╗██║     ██╔════╝██║  ██║██╔══██╗██╔════╝██║  ██║
███████╗██║██╔████╔██║██████╔╝██║     █████╗  ███████║███████║███████╗███████║
╚════██║██║██║╚██╔╝██║██╔═══╝ ██║     ██╔══╝  ██╔══██║██╔══██║╚════██║██╔══██║
███████║██║██║ ╚═╝ ██║██║     ███████╗███████╗██║  ██║██║  ██║███████║██║  ██║
╚══════╝╚═╝╚═╝     ╚═╝╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                        <Rafael Jiménez Pérez>
    """
    print(a)

# Header screen output
header()
# Ask for user input message
text = input('--> ')
# Calculate the hash value of the previous message
hash_value = hash(text)
# Message hash value screen output
print("\nMessage hash value:", hash_value)