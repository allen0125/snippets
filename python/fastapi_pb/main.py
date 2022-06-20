
from fastapi import FastAPI, Form
from fastapi import Response
from fastapi_pb.pbs.build.message_pb2 import RequestMessage, ResponsedMessage


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/")
async def post_msg(pyload: bytes = Form(...)):
    req_msg = RequestMessage()
    print(pyload)
    req_msg.ParseFromString(pyload)

    res_msg = ResponsedMessage()
    res_msg.uid = 2
    res_msg.msg = f"Hello No.{req_msg.uid} user, your request message is: {req_msg.msg}"
    res_bytes = res_msg.SerializeToString()
    print(res_bytes)
    return Response(res_bytes)
