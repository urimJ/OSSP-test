def find_dog(sound):
    if sound == "awf awf":
        return("a dog barks")
    else:
        return("it's not a dog")

sound = "awf awf"
find_result = find_dog(sound)

print(find_result)