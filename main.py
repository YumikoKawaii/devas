import uvicorn
from application import initialize

app = initialize()

if __name__ == '__main__':
    uvicorn.run("main:application", host="0.0.0.0", port=800, reload=True, access_log=True)
