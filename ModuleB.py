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
                    credential = line.split(":")
                    name = credential[0].strip()
                    passwd = credential[1].strip()
                    if name not in self.user_pass_combo:
                        self.user_pass_combo[name] = [passwd]
                    else:
                        # make sure the password associated with this username is not already in the list
                        if passwd not in self.user_pass_combo[name]:
                            self.user_pass_combo[name].append(passwd)
    
    def write_file(self):
        """
        writes the passwords of the username one line at a time
        """
        with open(self.filename, "w") as file:
            if self.username in self.user_pass_combo:
                for v in self.user_pass_combo[self.username]:
                    file.write(v + "\n")

if __name__ == '__main__':
    mod_b = moduleB('rellassemmeby-2298@yopmail.com')
    mod_b.write_file()
