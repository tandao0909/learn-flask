from hello import db, User, Role

db.drop_all()
db.create_all()

admin_role = Role(name="Admin")
mod_role = Role(name="Moderator")
user_role = Role(name="User")

user_john = User(username = "john", role=admin_role)
user_susan = User(username = "susan", role=user_role)
user_david = User(username = "david", role=user_role)

print(admin_role.id)
print(mod_role.id)
print(user_role.id)

db.session.add(admin_role)
db.session.add(mod_role)
db.session.add(user_role)
db.session.add(user_john)
db.session.add(user_susan)
db.session.add(user_david)

# More concise way
# db.session.add_all([admin_role, mod_role, user_role, user_john, user_susan, user_david])

db.session.commit()

print(admin_role.id)
print(mod_role.id)
print(user_role.id)

# Changing row
admin_role.name = "Administrator"
db.session.add(admin_role)
db.session.commit()

# Deleting row
db.session.delete(mod_role)
db.session.commit()

# Querying row
print(Role.query.all())
print(User.query.all())

# filters
print(User.query.filter_by(role=user_role).all())
print(str(User.query.filter_by(role=user_role)))

user_role = Role.query.filter_by(name="User").first()
print(user_role)

users = user_role.users
print(users)
print(users[0].role)

print(user_role.users.order_by(User.username).all())
print(user_role.users.count())