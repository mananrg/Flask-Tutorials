#pip install flask-bcrypt
from flask_bcrypt import Bcrypt
bcrypt=Bcrypt()
password="mypassword"
hashed_password=bcrypt.generate_password_hash(password=password)
print(hashed_password)

check=bcrypt.check_password_hash(hashed_password,'mypassword')
print(check)
