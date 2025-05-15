
def subtract():
    with open("list", "r") as f1, open("past_words", "r") as f2:
        words1 = f1.read().upper().strip().split()
        words2 = f2.read().strip().split()

    # Keep only words in file1 that are not in file2
    result = [word for word in words1 if word not in words2]

    # Save back to file1.txt
    with open("list", "w") as f1:
        f1.write(" ".join(result))

if __name__ == "__main__":
    subtract()