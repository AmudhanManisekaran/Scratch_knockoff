from passlib.hash import sha256_crypt

from db_handler import firebase_handler as fb_handle

def verify(db_url, username, password):
    if is_username(db_url, username):
        user_data = fb_handle.retrieve_data(db_url, username)
        password_candidate = fb_handle.retrieve_password_from_fb_data(user_data)
        if is_password_correct(password_candidate, password):
            return (True, None)
        else:
            return (False, 'Password Incorrect')
    return (False, 'Username Incorrect')

def is_username(db_url, username):
    data = fb_handle.retrieve_data(db_url, username)
    return data != None

def is_password_correct(password_candidate, password):
    return sha256_crypt.verify(password_candidate, password)
