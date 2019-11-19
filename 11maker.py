def sentence_maker(phrase):
    interrogatives =("how","why","what")
    capi = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capi)
    #else:
        #return "{}.".format(capi)
        #return "false"
print(sentence_maker("aspire nxt pvt ltd"))