import time
import argparse
import datetime

from nnicli import Experiment

def main(args):
    exp = Experiment()

    exp.start_experiment(args.config, port=args.port)

    status = exp.get_experiment_status()
    prev_job = None
    while status['status'] != 'DONE':
        jobs = exp.list_trial_jobs()
        if jobs:
            index = len(jobs) - 1
            job = jobs[index]
            if not prev_job or prev_job.trialJobId != job.trialJobId:
                print('\nTrial Number: %s' % index)
                print('Trial ID: %s' % job.trialJobId)
                print('Hyperparameters: %s' % job.hyperParameters[0].parameters)
            if not prev_job or (prev_job.trialJobId == job.trialJobId and prev_job.status != job.status):
                print('Status: %s' % job.status)
                if job.status == 'SUCCEEDED':
                    start = datetime.datetime.fromtimestamp(round(job.startTime / 1000))
                    end = datetime.datetime.fromtimestamp(round(job.endTime / 1000))
                    print('Duration: %s' % (end - start))
            prev_job = job
        
        status = exp.get_experiment_status()
        time.sleep(5)

    exp.stop_experiment()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', default=9000, help='NNI port')
    required_argument_group = parser.add_argument_group('required arguments')
    required_argument_group.add_argument('--config', help='NNI configuration', required=True)

    main(parser.parse_args())