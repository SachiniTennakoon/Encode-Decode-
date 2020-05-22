#say user to enter E to encode
print("enter E to encode")

#say user to enter D to decode
print("enter D to decode")

#say user to enter A to analyse
print("enter A to analyse")

#say user to enter Q to exit
print("enter Q to exit")

#say to enter the command
command=str(input("enter the command:  "))

#check if the input is not Q
while command!="Q":
    




    

    #check if  the command is E
    if command=="E":
        
        #defining a function for decode the string
        def Encode(m,s):

            #gwtting count as 0
            count=0
            #find the length of the string
            length=len(m)
                    # 0123456789.....
            ALPHABET='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            alphabet='abcdefghijklmnopqrstuvwxyz'

           
            #defining encode message to a space
            encode_message = ''

            #check if the length of the string is over 1
            while length >= 1:

                #get the letter corresponding to count
                letter = m[count]

                #check if the  letter is in the string alphabet 
                if letter in ALPHABET:
            
                    #find the index of the alphabet corresponding to the letter
                    index = ALPHABET.index(letter)

                    #adding the index of the alphabet and number of keys that we want to shift
                    s_key = index + s
                
                
                    mod=s_key%len(ALPHABET)

                    #find the letter in alphabat corresponding to the mod
                    encode_letter = ALPHABET[mod]

                    #subtracting 1 from length
                    length = length - 1

                    #addind 1 to the count
                    count+= 1

                    #adding the encode letter to encode message
                    encode_message+= encode_letter


                elif letter in alphabet:
            
                    index = alphabet.index(letter)
                    s_key = index + s
                    mod=s_key%len(alphabet)
                    encode_letter = alphabet[mod]
                    length = length - 1
                    count+= 1
                    encode_message+= encode_letter


                else:

                    #if there is a symbol otherthan in alphabat print it ,as it is
                    encode_message+=letter
                    length=length-1
                    count+=1
            
         
        
            #returning the encode message    
            return encode_message


        #input the message
        message=str(input("enter the message:  "))

        #input the key
        shift_num=int(input("enter the shift number: "))

        #print theencode message
        print(Encode(message,shift_num))

   
    elif command=="D":
        
        #defining a function to decode string
        def Decode(m,s):

            #getting count as 0
            count=0

            #find the length of the string
            length=len(m)

            #0123456789....
            ALPHABET='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            alphabet='abcdefghijklmnopqrstuvwxyz'

           

            #defining the decode message o a space
            decode_message = ''

            #check if the lengthof the string is over 1
            while length >= 1:
        
                #get the letter corresponding to the count
                letter = m[count]

                #check if the letter is in the string alphabet
                if letter in ALPHABET:

                    #find the index of the alphabet corresponding to the letter
                    index = ALPHABET.index(letter)

                    #adding the index of he alphabet and number of keys that we want to shift
                    decode_index = index - s

                    #
                    mod=decode_index%len(ALPHABET)

                    #find the letter in aphabet corresponding to the mod
                    decode_letter = ALPHABET[mod]

                    #subtracting 1 from length
                    length = length - 1

                    #adding 1 to the count
                    count+= 1

                    #adding the decode etter to the decode message
                    decode_message+= decode_letter

                elif letter in alphabet:
            
                    index = alphabet.index(letter)
                    decode_index = index - s
                    mod=decode_index%len(alphabet)
                    decode_letter = alphabet[mod]
                    length = length - 1
                    count+= 1
                    decode_message+= decode_letter



                else:
                    #is thereis a symbol otherthan in alphabet print it,as it is
                    decode_message+=letter
                    length=length-1
                    count+=1
        
            return decode_message



    
                 
        #input the message
        s_message=str(input("enter the secret message: "))

        #input the key
        shift_num=int(input("enter the number; "))

        #print the decode message
        print(Decode(s_message,shift_num))

    #check if the command is A
    elif command=="A":

        #defining a function to decode string
        def Decode(m,s):

            #getting count as 0
            count=0

            #find the length of the string
            length=len(m)

            #0123456789....
            alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

            #capitalizing the string
            m=m.upper()

            #defining the decode message o a space
            decode_message = ''

            #check if the lengthof the string is over 1
            while length >= 1:
        
                #get the letter corresponding to the count
                letter = m[count]

                #check if the letter is in the string alphabet
                if letter in alphabet:

                    #find the index of the alphabet corresponding to the letter
                    index = alphabet.index(letter)

                    #adding the index of he alphabet and number of keys that we want to shift
                    decode_index = index - s

                    #
                    mod=decode_index%len(alphabet)

                    #find the letter in aphabet corresponding to the mod
                    decode_letter = alphabet[mod]

                    #subtracting 1 from length
                    length = length - 1

                    #adding 1 to the count
                    count+= 1

                    #adding the decode etter to the decode message
                    decode_message+= decode_letter

                else:
                    #is thereis a symbol otherthan in alphabet print it,as it is
                    decode_message+=letter
                    length=length-1
                    count+=1
        
            return decode_message

        #defining a function to find the rotation
        def key(m,x):
            
            alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            m=m.upper()

            #fing the 1st letter in the decode string
            decode_letter=m[0]

            #find the index of the alphabet corresponding to the letter
            decode_key=alphabet.index(decode_letter)

            #fing the 1st letter in the plain string
            plain_letter=x[0]

            #find the index of the alphabet corresponding to the letter
            plain_key=alphabet.index(plain_letter)

            #get the rotation
            key=decode_key-plain_key
            
            mod=key%26

            #getting the mod
            return mod

        #getting the decode string
        decode_message=str(input("enter the decode string: "))

        #getting the plain text
        plain_text=str(input("enter the plain text: "))
        plain_text=plain_text.upper()

        #getting a range between 1 to 26 
        for number in range (1,26):

            #if the resulting decode text is in plain text
            if plain_text in Decode(decode_message,number) :

                
                x = Decode(decode_message,number) 
        
                #print that decode string
                print("decode string is",x)

                #print the rotation
                print("rotation is",key(decode_message,x))

    


    else:
        print("you entered a invalid input please try again")
        
    command=str(input("enter the command:  "))
    
    
    
            

else:
             
    print("you choose to exit the program")             
    
