from passlib.context import CryptContext

passowrd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# class PasswordHashing(): --> in video 2:28:28
class PasswordHashing:
    def bcrypt(password: str):
        hashed_password = passowrd_context.hash(password)
        return hashed_password
