from fastapi import FastAPI
app =FastAPI()
@app.get("/")
def pakistan():
	return {"Message":"Hello Pakistan"}
	
