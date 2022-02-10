


from ProphetServiceImpl import *


from proto.ProphetService_pb2_grpc import *;

import grpc

import time
from concurrent import futures

import logging
def main():

    port=8888
    logging.basicConfig(level=logging.ERROR)
    logging.getLogger('fbprophet.plot').setLevel(logging.ERROR)
    logging.getLogger('fbprophet').setLevel(logging.ERROR)


    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    add_ProphetServiceServicer_to_server(ProphetServiceImpl(), server)

    server.add_insecure_port('[::]:%d'%(port))
    server.start()

    print('''           listen port : %d
        
                                 _____                 _          _   
                                |  __ \               | |        | |  
                                | |__) | __ ___  _ __ | |__   ___| |_ 
                                |  ___/ '__/ _ \| '_ \| '_ \ / _ \ __|
                                | |   | | | (_) | |_) | | | |  __/ |_ 
                                |_|   |_|  \___/| .__/|_| |_|\___|\__|
                                                | |                   
                                                |_|                   
                
            '''%(port))

    try:
        while True:
            time.sleep(100)
    except KeyboardInterrupt:
        print("stop")
        server.stop(0)
main()