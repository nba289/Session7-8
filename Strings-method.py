text = "abcdefghijklmnop"
print(dir(text))
help(text.isupper)
print(text.isupper())  # is the all uppercase?
print("ABC".isupper())  # is the all uppercase?
print(text.upper())  # convert the text to uppercase?
print(text.upper().isupper())  # is the all uppercase? yes

new_text = text.upper()
print(text, new_text)
print("bannannnana" .count("n"))
print("bannannnana" .index("ana"))
print("banabnabanana".replace("ana", "XXYYZZ"))
sentence = "Hello, good sir; How shall! I be off assistance today?"
#dumb way to do it
print(sentence.replace(",","").replace(";",""))

#elegant way to do it
punctuation = ".,;!?"
for p in punctuation:
    sentence = sentence.replace(p, "")
print(sentence)

print("this a sentence and I want the words".split(" "))

text = "Bob goes to school. Bob likes to party. Bob likes drugs. Bob likes boys."
print(text.find("Bob"))
print(text.rfind("Bob"))
# find all the positions of bob
i = 0
while i < len(text):
    i = text.find("Bob", i)
    if i == -1:
        break
    print(i)
    i += 1

