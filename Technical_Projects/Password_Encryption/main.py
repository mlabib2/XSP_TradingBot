import bcrypt
#must be byte string
# hashed = bcrypt.hashpw(password, bcrypt.gensalt())

# username = request.form.get("username")
# password = request.form.get("password").encode("utf-8") 

#Look user up in BD using username 

# if bcrypt.checkpw(password, hashed):
#     print("It matches")
    # return redirect(url_for("user_profile"))
# else:
#     print("Didn't Match")
    # flash("Invalid Credentials")

password = b"SecretPassword55"
import time 

start = time.time()
hashed = bcrypt.hashpw(password, bcrypt.gensalt(rounds = 17))
end = time.time()
f = end - start 
print(f)

