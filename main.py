from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr

#fakedata

users = [
    {"name": "Raul", "email": "raul@example.com", "age": 25}
]

#schemas

class UserCreate(BaseModel):
	name: str
	email: EmailStr
	age: int


class UserUpdate(BaseModel):
	name: str | None = None
	age: int | None = None

app = FastAPI()

#endpoints

@app.post("/users")
def create_user(user: UserCreate):
	for existing_user in users:
		if existing_user["email"] == user.email:
			raise HTTPException(
				status_code=status.HTTP_409_CONFLICT,
				detail="The user with this email already exists"
			) 
	users.append(user.model_dump())
	return user



@app.get("/users")
def get_users(min_age: int | None = None, max_age: int | None = None):

	filtered_users = []

	for user in users:
		if min_age is not None and user["age"] < min_age:
			continue


		if max_age is not None and user["age"] > max_age:
			continue		

		filtered_users.append(user)
		
	return filtered_users


@app.get("/users/{user_email}")
def get_user_by_email(user_email: str):
	for user in users:
		if user["email"] == user_email:
			return user

	raise HTTPException(
		status_code=status.HTTP_404_NOT_FOUND,
		detail="User not found"
	)


@app.delete("/users/{user_email}")
def delete_user(user_email: str):
	for user in users:
		if user["email"] == user_email:
			users.remove(user)
			return "User has been deleted"

	raise HTTPException(
		status_code=status.HTTP_404_NOT_FOUND,
		detail="User not found"
	)


@app.patch("/users/{user_email}")
def update_user(user_email: str, data: UserUpdate):
	for user in users:
		if user["email"] == user_email:
			if data.name is not None:
				user["name"] = data.name
			if data.age is not None:
				user["age"] = data.age

			return user

	raise HTTPException(
		status_code=status.HTTP_404_NOT_FOUND,
		detail="User not found"
	)
