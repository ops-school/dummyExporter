# flask_web/app.py

from flask import Flask
import random
import os
import sys

app = Flask(__name__)
RAND = random.Random()
PROCESS_ID = os.getpid()
PROCESS_NAME = sys.argv[0].split('/')[-1]


# setup global_variable
my_dict = {}
my_dict['DummyService_requests{caller = "APT",'] = 10008.0
my_dict['DummyService_errors{'] = 43.0
my_dict['DummyService_duration_summary{quantile="0.5",'] = 100.0
my_dict['DummyService_duration_summary{quantile="0.75",'] = 0.0
my_dict['DummyService_duration_summary{quantile="0.95",'] = 0.0
my_dict['DummyService_duration_summary{quantile="0.98",'] = 0.0
my_dict['DummyService_duration_summary{quantile="0.99",'] = 0.0
my_dict['DummyService_duration_summary{quantile="0.999",'] = 0.0
my_dict['DummyService_duration_summary_count{'] = 10008.0
my_dict['DummyService_duration_summary_sum{'] = 433354.0
my_dict['DummyService_duration_cumulative_bucket{le="10.0",'] = 1056.0
my_dict['DummyService_duration_cumulative_bucket{le="20.0",'] = 2702.0
my_dict['DummyService_duration_cumulative_bucket{le="30.0",'] = 3333.0
my_dict['DummyService_duration_cumulative_bucket{le="40.0",'] = 4963.0
my_dict['DummyService_duration_cumulative_bucket{le="50.0",'] = 5592.0
my_dict['DummyService_duration_cumulative_bucket{le="60.0",'] = 6005.0
my_dict['DummyService_duration_cumulative_bucket{le="70.0",'] = 7381.0
my_dict['DummyService_duration_cumulative_bucket{le="80.0",'] = 8774.0
my_dict['DummyService_duration_cumulative_bucket{le="90.0",'] = 9178.0
my_dict['DummyService_duration_cumulative_bucket{le="+Inf",'] = 10008.0
my_dict['DummyService_duration_non_cumulative_bucket{le="10.0",'] = 646.0
my_dict['DummyService_duration_non_cumulative_bucket{le="20.0",'] = 646.0
my_dict['DummyService_duration_non_cumulative_bucket{le="30.0",'] = 646.0
my_dict['DummyService_duration_non_cumulative_bucket{le="40.0",'] = 646.0
my_dict['DummyService_duration_non_cumulative_bucket{le="50.0",'] = 646.0
my_dict['DummyService_duration_non_cumulative_bucket{le="60.0",'] = 646.0
my_dict['DummyService_duration_non_cumulative_bucket{le="70.0",'] = 646.0
my_dict['DummyService_duration_non_cumulative_bucket{le="80.0",'] = 646.0
my_dict['DummyService_duration_non_cumulative_bucket{le="90.0",'] = 646.0
my_dict['DummyService_duration_non_cumulative_bucket{le="+Inf",'] = 646.0

def update_dict():
  """ change dict data with random """
  my_dict['DummyService_requests{caller = "APT",'] += RAND.randint(0, 100)
  my_dict['DummyService_errors{'] += RAND.randint(0, 10)
  my_dict['DummyService_duration_summary_count{'] += RAND.randint(0, 100)
  my_dict['DummyService_duration_summary_sum{'] += RAND.randint(0, 1000)
  my_dict['DummyService_duration_summary{quantile="0.5",'] += (5-RAND.randint(0, 10))

  my_dict['DummyService_duration_summary{quantile="0.75",'] = (my_dict['DummyService_duration_summary{quantile="0.5",']+RAND.randint(0, 3))
  my_dict['DummyService_duration_summary{quantile="0.95",'] = (my_dict['DummyService_duration_summary{quantile="0.75",']+RAND.randint(0, 5))
  my_dict['DummyService_duration_summary{quantile="0.98",'] = (my_dict['DummyService_duration_summary{quantile="0.95",']+RAND.randint(0, 5))
  my_dict['DummyService_duration_summary{quantile="0.99",'] = (my_dict['DummyService_duration_summary{quantile="0.98",']+RAND.randint(0, 5))
  my_dict['DummyService_duration_summary{quantile="0.999",'] = (my_dict['DummyService_duration_summary{quantile="0.99",']+RAND.randint(0, 10))

  my_dict['DummyService_duration_non_cumulative_bucket{le="10.0",'] += (5-RAND.randint(0, 10))
  my_dict['DummyService_duration_non_cumulative_bucket{le="20.0",'] += (5-RAND.randint(0, 10))
  my_dict['DummyService_duration_non_cumulative_bucket{le="30.0",'] += (5-RAND.randint(0, 10))
  my_dict['DummyService_duration_non_cumulative_bucket{le="40.0",'] += (5-RAND.randint(0, 10))
  my_dict['DummyService_duration_non_cumulative_bucket{le="50.0",'] += (5-RAND.randint(0, 10))
  my_dict['DummyService_duration_non_cumulative_bucket{le="60.0",'] += (5-RAND.randint(0, 10))
  my_dict['DummyService_duration_non_cumulative_bucket{le="70.0",'] += (5-RAND.randint(0, 10))
  my_dict['DummyService_duration_non_cumulative_bucket{le="80.0",'] += (5-RAND.randint(0, 10))
  my_dict['DummyService_duration_non_cumulative_bucket{le="90.0",'] += (5-RAND.randint(0, 10))
  my_dict['DummyService_duration_non_cumulative_bucket{le="+Inf",'] += (5-RAND.randint(0, 10))

  my_dict['DummyService_duration_cumulative_bucket{le="10.0",'] += my_dict['DummyService_duration_non_cumulative_bucket{le="10.0",']
  my_dict['DummyService_duration_cumulative_bucket{le="20.0",'] = my_dict['DummyService_duration_non_cumulative_bucket{le="20.0",'] + my_dict['DummyService_duration_cumulative_bucket{le="10.0",']
  my_dict['DummyService_duration_cumulative_bucket{le="30.0",'] = my_dict['DummyService_duration_non_cumulative_bucket{le="30.0",'] + my_dict['DummyService_duration_cumulative_bucket{le="20.0",']
  my_dict['DummyService_duration_cumulative_bucket{le="40.0",'] = my_dict['DummyService_duration_non_cumulative_bucket{le="40.0",'] + my_dict['DummyService_duration_cumulative_bucket{le="30.0",']
  my_dict['DummyService_duration_cumulative_bucket{le="50.0",'] = my_dict['DummyService_duration_non_cumulative_bucket{le="50.0",'] + my_dict['DummyService_duration_cumulative_bucket{le="40.0",']
  my_dict['DummyService_duration_cumulative_bucket{le="60.0",'] = my_dict['DummyService_duration_non_cumulative_bucket{le="60.0",'] + my_dict['DummyService_duration_cumulative_bucket{le="50.0",']
  my_dict['DummyService_duration_cumulative_bucket{le="70.0",'] = my_dict['DummyService_duration_non_cumulative_bucket{le="70.0",'] + my_dict['DummyService_duration_cumulative_bucket{le="60.0",']
  my_dict['DummyService_duration_cumulative_bucket{le="80.0",'] = my_dict['DummyService_duration_non_cumulative_bucket{le="80.0",'] + my_dict['DummyService_duration_cumulative_bucket{le="70.0",']
  my_dict['DummyService_duration_cumulative_bucket{le="90.0",'] = my_dict['DummyService_duration_non_cumulative_bucket{le="90.0",'] + my_dict['DummyService_duration_cumulative_bucket{le="80.0",']
  my_dict['DummyService_duration_cumulative_bucket{le="+Inf",'] = my_dict['DummyService_duration_non_cumulative_bucket{le="+Inf",'] + my_dict['DummyService_duration_cumulative_bucket{le="90.0",']

def create_data():
   update_dict()
   return_string = ''
   for key in my_dict:
     return_string += key+'process_id="'+str(PROCESS_ID)+'",process_name="'+PROCESS_NAME+'"} '+str(my_dict[key])+"\n"
   return return_string

@app.route('/')
def hello_world():
    return 'Welcome to OpsSchool metrics Dummy exporter <br> To get the dummy metrics go to the "/metrics" route!'


@app.route('/isUp')
def goaway():
    return 'DUMMY EXPORTER IS UP!'

@app.route('/metrics')
def metrics():
    return_data = create_data()
    return return_data

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
