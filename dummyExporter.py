
# flask_web/app.py

from flask import Flask
import random
import os
import sys

app = Flask(__name__)
RAND = random.Random()
PROCESS_ID = os.getpid()
PROCESS_NAME = sys.argv[0].split('/')[-1]

class DummyMetrics:
  def __init__(self):
    self.metrics_dict = {}
    self.metrics_dict['DummyService_requests{caller = "Dummy",'] = 19998.0
    self.metrics_dict['DummyService_errors{'] = 43.0
    self.metrics_dict['DummyService_duration_summary{quantile="0.5",'] = 100.0
    self.metrics_dict['DummyService_duration_summary{quantile="0.75",'] = 0.0
    self.metrics_dict['DummyService_duration_summary{quantile="0.95",'] = 0.0
    self.metrics_dict['DummyService_duration_summary{quantile="0.98",'] = 0.0
    self.metrics_dict['DummyService_duration_summary{quantile="0.99",'] = 0.0
    self.metrics_dict['DummyService_duration_summary{quantile="0.999",'] = 0.0
    self.metrics_dict['DummyService_duration_summary_count{'] = 10008.0
    self.metrics_dict['DummyService_duration_summary_sum{'] = 433354.0
    self.metrics_dict['DummyService_duration_cumulative_bucket{le="10.0",'] = 1056.0
    self.metrics_dict['DummyService_duration_cumulative_bucket{le="20.0",'] = 2702.0
    self.metrics_dict['DummyService_duration_cumulative_bucket{le="30.0",'] = 3333.0
    self.metrics_dict['DummyService_duration_cumulative_bucket{le="40.0",'] = 4963.0
    self.metrics_dict['DummyService_duration_cumulative_bucket{le="50.0",'] = 5592.0
    self.metrics_dict['DummyService_duration_cumulative_bucket{le="60.0",'] = 6005.0
    self.metrics_dict['DummyService_duration_cumulative_bucket{le="70.0",'] = 7381.0
    self.metrics_dict['DummyService_duration_cumulative_bucket{le="80.0",'] = 8774.0
    self.metrics_dict['DummyService_duration_cumulative_bucket{le="90.0",'] = 9178.0
    self.metrics_dict['DummyService_duration_cumulative_bucket{le="+Inf",'] = 10008.0
    self.metrics_dict['DummyService_duration_non_cumulative_bucket{le="10.0",'] = 246.0
    self.metrics_dict['DummyService_duration_non_cumulative_bucket{le="20.0",'] = 346.0
    self.metrics_dict['DummyService_duration_non_cumulative_bucket{le="30.0",'] = 446.0
    self.metrics_dict['DummyService_duration_non_cumulative_bucket{le="40.0",'] = 546.0
    self.metrics_dict['DummyService_duration_non_cumulative_bucket{le="50.0",'] = 646.0
    self.metrics_dict['DummyService_duration_non_cumulative_bucket{le="60.0",'] = 646.0
    self.metrics_dict['DummyService_duration_non_cumulative_bucket{le="70.0",'] = 546.0
    self.metrics_dict['DummyService_duration_non_cumulative_bucket{le="80.0",'] = 446.0
    self.metrics_dict['DummyService_duration_non_cumulative_bucket{le="90.0",'] = 446.0
    self.metrics_dict['DummyService_duration_non_cumulative_bucket{le="+Inf",'] = 446.0
  def update_metrics(self):
    """ change dict data with random """
    self.metrics_dict['DummyService_requests{caller = "APT",'] += RAND.randint(0, 100)
    self.metrics_dict['DummyService_errors{'] += RAND.randint(0, 10)
    self.metrics_dict['DummyService_duration_summary_count{'] += RAND.randint(0, 100)
    self.metrics_dict['DummyService_duration_summary_sum{'] += RAND.randint(0, 1000)
    self.metrics_dict['DummyService_duration_summary{quantile="0.5",'] += (5-RAND.randint(0, 10))
    self.metrics_dict['DummyService_duration_summary{quantile="0.75",'] = (my_dict['DummyService_duration_summary{quantile="0.5",']+RAND.randint(0, 3))
    self.metrics_dict['DummyService_duration_summary{quantile="0.95",'] = (my_dict['DummyService_duration_summary{quantile="0.75",']+RAND.randint(0, 5))
    self.metrics_dict['DummyService_duration_summary{quantile="0.98",'] = (my_dict['DummyService_duration_summary{quantile="0.95",']+RAND.randint(0, 5))
    self.metrics_dict['DummyService_duration_summary{quantile="0.99",'] = (my_dict['DummyService_duration_summary{quantile="0.98",']+RAND.randint(0, 5))
    self.metrics_dict['DummyService_duration_summary{quantile="0.999",'] = (my_dict['DummyService_duration_summary{quantile="0.99",']+RAND.randint(0, 10))
    self.metrics_dict['DummyService_duration_non_cumulative_bucket{le="10.0",'] += (5-RAND.randint(0, 10))
    self.metrics_dict['DummyService_duration_non_cumulative_bucket{le="20.0",'] += (5-RAND.randint(0, 10))
    self.metrics_dict['DummyService_duration_non_cumulative_bucket{le="30.0",'] += (5-RAND.randint(0, 10))
    self.metrics_dict['DummyService_duration_non_cumulative_bucket{le="40.0",'] += (5-RAND.randint(0, 10))
    self.metrics_dict['DummyService_duration_non_cumulative_bucket{le="50.0",'] += (5-RAND.randint(0, 10))
    self.metrics_dict['DummyService_duration_non_cumulative_bucket{le="60.0",'] += (5-RAND.randint(0, 10))
    self.metrics_dict['DummyService_duration_non_cumulative_bucket{le="70.0",'] += (5-RAND.randint(0, 10))
    self.metrics_dict['DummyService_duration_non_cumulative_bucket{le="80.0",'] += (5-RAND.randint(0, 10))
    self.metrics_dict['DummyService_duration_non_cumulative_bucket{le="90.0",'] += (5-RAND.randint(0, 10))
    self.metrics_dict['DummyService_duration_non_cumulative_bucket{le="+Inf",'] += (5-RAND.randint(0, 10))
    self.metrics_dict['DummyService_duration_cumulative_bucket{le="10.0",'] += my_dict['DummyService_duration_non_cumulative_bucket{le="10.0",']
    self.metrics_dict['DummyService_duration_cumulative_bucket{le="20.0",'] = my_dict['DummyService_duration_non_cumulative_bucket{le="20.0",'] + my_dict['DummyService_duration_cumulative_bucket{le="10.0",']
    self.metrics_dict['DummyService_duration_cumulative_bucket{le="30.0",'] = my_dict['DummyService_duration_non_cumulative_bucket{le="30.0",'] + my_dict['DummyService_duration_cumulative_bucket{le="20.0",']
    self.metrics_dict['DummyService_duration_cumulative_bucket{le="40.0",'] = my_dict['DummyService_duration_non_cumulative_bucket{le="40.0",'] + my_dict['DummyService_duration_cumulative_bucket{le="30.0",']
    self.metrics_dict['DummyService_duration_cumulative_bucket{le="50.0",'] = my_dict['DummyService_duration_non_cumulative_bucket{le="50.0",'] + my_dict['DummyService_duration_cumulative_bucket{le="40.0",']
    self.metrics_dict['DummyService_duration_cumulative_bucket{le="60.0",'] = my_dict['DummyService_duration_non_cumulative_bucket{le="60.0",'] + my_dict['DummyService_duration_cumulative_bucket{le="50.0",']
    self.metrics_dict['DummyService_duration_cumulative_bucket{le="70.0",'] = my_dict['DummyService_duration_non_cumulative_bucket{le="70.0",'] + my_dict['DummyService_duration_cumulative_bucket{le="60.0",']
    self.metrics_dict['DummyService_duration_cumulative_bucket{le="80.0",'] = my_dict['DummyService_duration_non_cumulative_bucket{le="80.0",'] + my_dict['DummyService_duration_cumulative_bucket{le="70.0",']
    self.metrics_dict['DummyService_duration_cumulative_bucket{le="90.0",'] = my_dict['DummyService_duration_non_cumulative_bucket{le="90.0",'] + my_dict['DummyService_duration_cumulative_bucket{le="80.0",']
    self.metrics_dict['DummyService_duration_cumulative_bucket{le="+Inf",'] = my_dict['DummyService_duration_non_cumulative_bucket{le="+Inf",'] + my_dict['DummyService_duration_cumulative_bucket{le="90.0",']
  def get_metrics(self):
    return_string = ''
    for key in self.metrics_dict:
      return_string += key+'process_id="'+str(PROCESS_ID)+'",process_name="'+PROCESS_NAME+'"} '+str(self.metrics_dict[key])+"\n"
    return return_string

@app.route('/')
def hello_world():
    return 'Welcome to OpsSchool metrics Dummy exporter <br> To get the dummy metrics go to the "/metrics" route!'


@app.route('/isUp')
def goaway():
    return 'DUMMY EXPORTER IS UP!'

@app.route('/metrics')
def metrics():
    return_data = metrics.get_metrics()
    return return_data

if __name__ == '__main__':
    metrics=DummyMetrics()
    app.run(debug=True, host='0.0.0.0')
