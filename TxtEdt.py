import os

# print("Dir: " + os.getcwd())

def main():
    print("Welcome to TxtEdt!")
    print("Type your text. Write SAVE <filename> to save and QUIT to exit")

    text = []

    while True:
        line = input(">")

        if line.startswith("SAVE "):
            filename = line.split(" ", 1)[1]
            if __name__ == '__main__':
                savepath = f"../Documents/{filename}"
            else:
                savepath = f"Documents/{filename}"
            try:

                with open(savepath, "w") as f:
                    f.write("\n".join(text))
                print(f"File {filename} saved successfully")
            except Exception as e:
                print(f"ERR saving the file: {e}")

        elif line.strip().upper() == "QUIT":
            break
        
        else:
            text.append(line)
        
    print("Exiting...")

if __name__ == "__main__":
    main()
