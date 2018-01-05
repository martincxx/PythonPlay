def censor (text, word):
    l=len(word)
    cen_wrd=str("*"*l)
    return text.replace(word, cen_wrd)


print censor("Hijo de mil putas", "putas")
