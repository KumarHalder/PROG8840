class User:
    def __init__(self, user_id, name, age):
        self.user_id = user_id
        self.name = name
        self.age = age
        
users_db = {
    1: User(1, "Alice", 30),
    2: User(2, "Bob", 25),
}

def get_user(user_id):
    user = users_db.get(user_id)
    if user:
        return {"user_id": user.user_id, "name": user.name, "age": user.age}, 200
    return {"error": "User not found"}, 404

def create_user(name, age):
    user_id = len(users_db) + 1
    user = User(user_id, name, age)
    users_db[user_id] = user
    return {"user_id": user.user_id, "name": user.name, "age": user.age}, 201

def update_user(user_id, name, age):
    if user_id in users_db:
        user = users_db[user_id]
        user.name = name
        user.age = age
        return {"user_id": user.user_id, "name": user.name, "age": user.age}, 200
    return {"error": "User not found"}, 404

def list_users():
    return [{"user_id": user.user_id, "name": user.name, "age": user.age} for user in users_db.values()], 200


