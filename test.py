from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel, EmailStr

# pydantic schemas

class UserLogin(BaseModel):
	email: EmailStr 
	password: str
	remember_me: bool | None = None

app = FastAPI()

# functions

def get_app_name():
	return "Users API"


def get_current_user():
	return {"name": "Raul", "role": "admin"}


def get_current_user_or_401():
	current_user = {"name": "Raul"}
	if current_user is None:
		raise HTTPException(
			status_code=status.HTTP_401_UNAUTHORIZED,
			detail="User is not authorized"
		)
	return current_user


def require_admin(current_user = Depends(get_current_user)):
	if current_user["role"] != "admin":
		raise HTTPException(
			status_code=status.HTTP_403_FORBIDDEN,
			detail="It is not admin"
		)

	return current_user

# endpoints

@app.get("/admin")
def get_admin(admin = Depends(require_admin)):
	return {"admin": admin}


@app.get("/profile")
def get_profile(current_user = Depends(get_current_user)):
	return {"current_user": current_user}


@app.get("/info")
async def get_info(app_name = Depends(get_app_name)):
	return {"app_name": app_name}
	

@app.get("/me")
def get_me(user = Depends(get_current_user_or_401)):
	return {"user": user}


@app.post("/login")
def user_login(user: UserLogin):
	return user
