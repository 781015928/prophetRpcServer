
from proto import ProphetService_pb2;
from proto.ProphetModel_pb2 import *;
import pandas as pd
from fbprophet import Prophet
from pandas.plotting import register_matplotlib_converters
import time

import traceback

class ProphetServiceImpl(ProphetService_pb2.ProphetService):

    def getDateFormat(self, date):
        try:
            if ":" in date:
                time.strptime(date, "%Y-%m-%d %H:%M:%S")
                return "%Y-%m-%d %H:%M:%S"
            else:
                time.strptime(date, "%Y-%m-%d")
                return "%Y-%m-%d"
        except:
            return None

    def success(self):
        response = Response()
        response.code = 200
        return response

    def fail(self,msg):
        response = Response()

        response.code = 400
        response.message=msg
        return response

    def forecast(self, request, context):

        try:
            data = [{'y': sequence.value, 'ds': sequence.date_time} for sequence in request.sequences]
            simpleTime = data[0]['ds']
            dateFormat = self.getDateFormat(simpleTime)
            if (dateFormat == None):
                return self.fail(msg="time format not support,only support [yyyy-MM-dd] or [yyyy-MM-dd HH:mm:ss] ！")
            prophet = Prophet()
            df = pd.DataFrame(data=data)
            prophet.fit(df)
            future = prophet.make_future_dataframe(periods=1, freq=request.freq, include_history=False);
            forecast = prophet.predict(future)
            result = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(1)
            response = self.success()
            response.data.date_time = result.ds[0].strftime(dateFormat)
            response.data.forecastValue = round(result.yhat, 3)
            response.data.forecastValue_lower = round(result.yhat_lower, 3)
            response.data.forecastValue_upper = round(result.yhat_upper, 3)
            return response
        except Exception as e:

            print(repr(e))
            traceback.print_exc()
            return self.fail(str(e))

   # string date_time = 1;
   #
   # double forecastValue = 2;
   #
   # double forecastValue_lower = 3;
   #
   # double forecastValue_upper = 4;



