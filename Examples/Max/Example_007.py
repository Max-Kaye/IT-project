mysecretdictionary = {
    "a": "z",
    "b": "y",
    "c": "x",
    "d": "w",
    "e": "v",
    "f": "u",
    "g": "t",
    "h": "s",
    "i": "r",
    "j": "q",
    "k": "p",
    "l": "o",
    "m": "n",
    "n": "m",
    "o": "l",
    "p": "k",
    "q": "j",
    "r": "i",
    "s": "h",
    "t": "g",
    "u": "f",
    "v": "e",
    "w": "d",
    "x": "c",
    "y": "b",
    "z": "a",
}

mysecretdictionaryreverse = {

}
for key in mysecretdictionary:
    value = mysecretdictionary[key]
    mysecretdictionaryreverse[value] = key

wordtoencode = "pneumonoultramicroscopicsilicovolcanoconiosis"


def encode(wordtoencode2):
    output = ""
    for achar in wordtoencode2:
        encodedchar = mysecretdictionary[achar]
        output = output + encodedchar
    return output


var = encode(wordtoencode)
print var


def decode(wordtodecode):
    output = ""
    for achar in wordtodecode:
        decodedchar = mysecretdictionaryreverse[achar]
        output = output + decodedchar
    return output


print decode(var)
