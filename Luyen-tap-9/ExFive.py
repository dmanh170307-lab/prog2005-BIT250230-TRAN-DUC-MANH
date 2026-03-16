class User:
    def __init__(self, user_id):
        self._id = user_id
    @property
    def id(self):
        return self._id
nguoi_dung = User(101)
print(nguoi_dung.id)
