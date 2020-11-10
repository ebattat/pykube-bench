import time
import subprocess
import os


kube_server_log = 'kube_server.log'
metric_cmd = 'kubectl -n cpu-example top pod cpu-demo'.split()
first_line = 'CPU(cores), MEMORY(bytes)\n'

if os.path.exists(kube_server_log):
    os.remove(kube_server_log)

with open(kube_server_log, 'w') as kube_server_log_file:
    kube_server_log_file.write(first_line)

for i in range(10):
    kube_server_log_file = open(kube_server_log, 'a')
    process = subprocess.Popen(metric_cmd, stdout=subprocess.PIPE)
    output, err = process.communicate()
    result = output.decode('ascii').split()
    kube_server_log_file.write(f'{result[4][:-1]}, {result[5][:-2]}\n')
    time.sleep(1)

kube_server_log_file.close()
