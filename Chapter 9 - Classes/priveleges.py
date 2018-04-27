class Priveleges():
    def __init__(self, priveleges_list):
        """Different priveleges"""
        self.priveleges_list = ['can add post', 'can delete post', 'can ban users']

    def show_priveleges(self):
        print('Has priveleges: ' + str(self.priveleges_list) + '.')