admins = [0]

class User:
    def __init__(self, user_id):
        # admin check
        if user_id in admins:
            self.is_admin = True

        else:
            self.is_admin = False
