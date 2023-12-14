# pip install fastapi
# pip install "uvicorn[standard]"
# >uvicorn app:app --reload


from fastapi import FastAPI


# 1. Create the Web service application
app = FastAPI()



@app.get("/")  # http://127.0.0.1:8000/
def root():
    return {"message": "Welcome by Webservice WBS"} 


@app.get("/greeting") # http://127.0.0.1:8000/greeting
def greeting():
    return {"specialmessage": "Welcome Mohamed",
            "emp_id": 500}  


@app.get("/getuserinfo") # http://127.0.0.1:8000/getuserinfo
def get_user_info():
    return {"id": 700,
            "fn": "Thomas",
            "ln": "Meier"
            }  
 

# http://127.0.0.1:8000/getuserinfodynamic?empid=70&name=thomas
# http://127.0.0.1:8000/getuserinfodynamic?empid=70&name=80     ---> because 80 can be converted to "80"
# ERROR: http://127.0.0.1:8000/getuserinfodynamic?empid=meier&name=thomas    ----> Error because empid should be integer

@app.get("/getuserinfodynamic")
def get_user_info_dynamic(empid:int, name:str):
    return {
        "id": empid,
        "name": name,
        "message": "The emp is valid"
    } 


