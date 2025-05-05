from  models.user import User

user = User()
user.create_table()
user.insert(name="Alice", created_at="2025-05-06")

print(user.all())