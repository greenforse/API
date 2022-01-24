class User:
    def init(self, login, is_admin):
        self.login = login
        self.is_admin = is_admin

    def view(self):
        if self.is_admin:
            return "SELECT* FROM users"
        else:
            return "SELECT* FROM users"

    def remove_user(self):




