from fastapi import FastAPI,Depends,Header,HTTPException

app = FastAPI()

def get_token(token: str = Header(None)):
    if token != "verify":
        raise HTTPException(
            status_code= 401,
            detail = "Invalid token"
        )
    return {
        "user" : "verified"
    }

@app.get("/secure-data")
def secure_data(user = Depends(get_token)):
    return {
        "msg" : "Secure Data",
        "user":user
    }