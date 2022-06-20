import requests
from pbs.build.message_pb2 import RequestMessage, ResponsedMessage


def test_protobuf():
    """
    test
    :return:
    """
    req = RequestMessage()
    req.uid = 1
    req.msg = "Hello World"
    req_bytes = req.SerializeToString()
    data = {'pyload': req_bytes}
    response = requests.post("http://127.0.0.1:8080/", data=data)
    print(response.content)

    res = ResponsedMessage()
    res.ParseFromString(response.content)
    print(res.uid)
    print(res.msg)


if __name__ == '__main__':
    test_protobuf()
