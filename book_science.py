from urllib.request import urlopen
import certifi

url="https://www.gutenberg.org/files/84/84-0.txt"
local_name = "frankenstein.txt"

def save_locally():
    with open(local_name, "w") as local_fp:
        with urlopen(url, cafile=certifi.where()) as fp:
            for line in fp:
                line = line.decode().replace("\n", "")
                local_fp.write(line)

# save_locally()

punctuation = ",;.!-()?"
def get_unique_words():
    unique_words = {}
    with open(local_name) as fp:
        for line in fp:
            #remove punctuation
            for p in punctuation:
                 line = line.replace(p, " ")
            line = line.lower()
            #get the words:
            for word in line.split():
                unique_words [word] = unique_words.get(word, 0) + 1

    return unique_words

# save_locally()
unique_words = get_unique_words()
most_frequent = list(unique_words.values())
most_frequent.sort(reverse = True)
print(most_frequent)
for word in most_frequent[:10]:
    for unique_word, value in unique_words.items():
        if word == value:
            print(f"common words {unique_word} appears {value} times")
            break
