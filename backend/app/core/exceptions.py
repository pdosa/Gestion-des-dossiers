from fastapi import HTTPException

credentials_exception=HTTPException(
    status_code=401,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


permission_exception=HTTPException(
    status_code=401,
    detail="this user don't have a permission"
)

incorrect_username_or_password_exceptions=HTTPException(
    status_code=401,
    detail="Incorrect matricule or password"
)

no_access_method=HTTPException(
    status_code=403,
    detail="Unauthorized request"
)