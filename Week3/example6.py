def convert_in_uppercase(text):
    #return len(text) #gjatesin e tekstit
    #return text.count("er") #numerimi ne baze te prompt ne text
    return text.upper()
    #return text.lower()  -> nese do te gjitha me te vogla



if __name__ == '__main__':
    print(convert_in_uppercase("Nene Tereza aaaaaaa a a a er"))
