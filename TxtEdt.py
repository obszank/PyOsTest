import os

def main():
    print("Welcome to TxtEdt!")
    print("Type your text. Write SAVE <filename> to save and QUIT to exit")

    text = []

    while True:
        line = input(">")

        if line.startswith("SAVE "):
            filename = line.split(" ", 1)[1]
            savepath = f"../Documents/{filename}"
            with open(savepath, "w") as f:
                f.write("\n".join(text))
            print(f"File {filename} saved successfully")

        elif line.strip().upper() == "QUIT":
            break
        
        else:
            text.append(line)
        
    print("Exiting...")

if __name__ == "__main__":
    main()
