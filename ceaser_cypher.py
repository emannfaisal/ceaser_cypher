print("ceaser cypher")
alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
is_on="y"
while is_on=='y':
  choice=input('Do you want to encrypt or decrypt?enter "e" for encode and "d" for decode: ').lower()
  new_text=""
  text=input("Enter the text: ").lower()
  key=int(input("Enter the key: "))
  if(choice=="e"):
    for l in text:
      position=alphabets.index(l)+key
      new_text+=alphabets[position]
    print(f"The encoded text is {new_text}")
  elif(choice=="d"):
    key=key*-1
    for l in text:
      position=alphabets.index(l)+key
      new_text+=alphabets[position]
    print(f"The decoded text is {new_text}")
  is_on=input('Enter "y" to continue and "n" to stop: ' )  
      

            