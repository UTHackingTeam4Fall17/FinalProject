class moduleB(object):
    """
    This is the class to return to Michael
    Contains the username from Nick and a filename of the file that lists out this user's pwned passwords
    """
    def __init__(self, username):
        self.username = username
        self.filename = "passwords_list.txt" # filename to send to Michael
        self.user_pass_combo= {}
        self.create_dictionary()
    
    def create_dictionary(self):
        """
        key is username
        value is a list of passwords for that username
        ex: {"email@email", ["qwerty", "12345"]}
        important: make sure the input file is on local disk
        """
        with open("password_dumps.txt", "r") as file:
            for line in file.readlines():
                if line.strip():        # check empty lines
                    info = line.split(":")
                    value = [info[1].strip()]

                    if info[0] not in self.dicts:
                        self.user_pass_combo[info[0]] = value
                    else:
                        self.user_pass_combo[info[0]].append(info[1].strip())
    
    def write_file(self):
        """
        writes the passwords of the username one line at a time
        """
        with open(self.filename, "a") as file:
            if self.username in self.user_pass_combo:
                for v in self.user_pass_combo[self.username]:
                    file.write(v + "\n")

if __name__ == '__main__':
    mod_b = moduleB('mam-venda@hotmail.com')
    mod_b.write_file()
