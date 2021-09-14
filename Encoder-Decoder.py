import base64
import time
import webbrowser
while True:
    print("\tMAIN MENU")
    print("\t_________")
    print("1.Base 64 Encoder")
    print("2.Base 64 Decoder")
    print("3.Base 32 Encoder")
    print("4.Base 32 Decoder")
    print("5.Binary Encoder")
    print("6.Binary Decoder")
    print("7.EXIT")
    ch=int(input("Enter A Choice (1-7): "))
    if ch==1:
        a=input('Enter A String: ')
        sample_string_bytes = a.encode("ascii")
        base64_bytes = base64.b64encode(sample_string_bytes)
        base64_string = base64_bytes.decode("ascii")
        print(f"Encoded String: {base64_string}")
    elif ch==2:
        b=input('Enter A String: ')
        base64_bytes = b.encode("ascii")
        sample_string_bytes = base64.b64decode(base64_bytes)
        sample_string = sample_string_bytes.decode("ascii")
        print(f"Decoded String: {sample_string}")
    elif ch==3:
        a=input('Enter A String: ')
        print("Encoding String...")
        time.sleep(2)
        print(base64.b32encode(bytearray(a, 'ascii')).decode('utf-8'))
    elif ch==4:
        a=input('Enter A String: ')
        print("Decoding String...")
        time.sleep(2)
        print(base64.b32decode(bytearray(a, 'ascii')).decode('utf-8'))
    elif ch==5:
        a=input('Enter A String: ')
        res = ''.join(format(ord(i), '08b') for i in a)
        print("The string after binary conversion : " + str(res))
    elif ch==6:
        webbrowser.open('https://codebeautify.org/binary-to-text')
    elif ch==7:
        print("Thank You For Using This Tool")
        time.sleep(1)
        print('Exiting...')
        time.sleep(2)
        break
    else:
        print('Invalid Option!!!. Choose From (1-7) ')

        
        
        
    

    


























      

