import grpc

import proto.ProphetService_pb2_grpc  as prophetService_pb2_grpc  ;
from proto.ProphetService_pb2 import *;
from proto.ProphetModel_pb2   import *;
import datetime

def run():
    channel = grpc.insecure_channel("localhost:8888")
    stub = prophetService_pb2_grpc.ProphetServiceStub(channel=channel)




    r1= ProphetRequest()
    r1.freq='D'



    for num in range(1, 10):
        sequence= r1.sequences.add()
        sequence.date_time=(datetime.datetime.now() + datetime.timedelta(days=num)).strftime("%Y-%m-%d")
        sequence.value=num
    sequence = r1.sequences.add()
    sequence.date_time = 'yyyasd'
    sequence.value = 2
    response = stub.forecast(r1)


    r2= ProphetRequest()
    r2.freq='H'

    print("forecast received: %s" % response)

    for num in range(1, 10):
        sequence= r2.sequences.add()
        sequence.date_time=(datetime.datetime.now() + datetime.timedelta(hours=num)).strftime("%Y-%m-%d %H:%m:00")
        print(sequence)
        sequence.value=num

    sequence = r2.sequences.add()
    sequence.date_time = (datetime.datetime.now() + datetime.timedelta(hours=11)).strftime("%Y-%m-%d %H:%m:00")
    sequence.value = 21



    response = stub.forecast(r2)


    print("forecast received: %s" % response)



if __name__ == '__main__':
    run()
