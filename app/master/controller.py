from app import mongo


def add_form(name, email, message):
    data_to_insert = {'name': name, 'email': email, 'message': message}
    mongo.db.form.insert_one(data_to_insert)
