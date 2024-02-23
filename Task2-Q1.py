class Cypher():
    def __init__(self,string):
        self.string=string

    def conversion(cls,string):
        convert_string=''
        for char in string:
            if char.isdigit():
                convert_string += str((int(char)+1)% 10)
            elif char.isalpha():
                 offset = ord('A' if char.isupper() else 'a')
                 convert_string+= chr((ord(char) - offset + 2) % 26 + offset)
        else:
            convert_string += char
        return convert_string
    def do_conversion(self):
        converted_string = self.conversion(self.string)
        print("Converted String:", converted_string)
        return converted_string
    
c1=Cypher("ABcD1293Z")
c1.do_conversion()