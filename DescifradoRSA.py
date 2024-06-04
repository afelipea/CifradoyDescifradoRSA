encodedMessage =int( input("Enter your encoded message: "))
x = int(input("Enter the element x of your private key: "))
n = int(input("Enter the element n of your public key: "))
decodedMessage = (encodedMessage**x)%n

print("This is the message! ")
print(decodedMessage)