import PyPDF2  ##pdf kullanabilmek için
  
# dosyayı açıp değişkene atar.
pdfFileObj = open('ödev2.pdf', 'rb')
  
# okuma
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# obje oluşturmak için
pageObj = pdfReader.getPage(0)
  
# metin okuma
print(pageObj.extractText())
  
# kapama
pdfFileObj.close() 



def caesar_cipher(raw_text, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    shifted_alphabet = alphabet[26-key:]+alphabet[0:(26-key)]
    cipher_text = ""
    for i in range(len(raw_text)):
        char = raw_text[i]
        idx = alphabet.find(char.upper())
        if idx == -1:
            cipher_text = cipher_text + char
        elif char.islower():
            cipher_text = cipher_text + shifted_alphabet[idx].lower()
        else:
            cipher_text = cipher_text + shifted_alphabet[idx] 
    return(cipher_text)


''' def ceaser(message,key):  
    encrypted_message = ""


    numbers = ["0","1","2","3","4","5","6","7","8","9"]



    for i in numbers:

                                                        ##sayılar için ama çalıştıramadım.
        if i not in numbers:
            encrypted_message +=i

        else:
            encrypted_message += numbers[(numbers.index(i)+2) % len(numbers)]

    print(encrypted_message)
    
out1=(ceaser(pageObj.values,2))
smy=open("dosya2.txt","w")
smy.write(str(out1))
smy.close() '''



out2=(caesar_cipher(pageObj.extractText(),8))
ths = open("dosya.txt", "w")
ths.write(out2)
ths.close()
