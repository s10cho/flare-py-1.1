import os
import datetime
import subprocess
from fabric.api import *
from config import FlarePath, FlareDocker, FlareDeploy

class FlareServer():

    EER_SETUP = [
        FlareDeploy.DEPLOY_TEMP_EER_PATH,
        FlareDeploy.DEPLOY_EER_TAR_NAME
    ]

    def __init__(self):
        pass

    def convert_docker_monitoring_data(self, fileName, downloadPath):
        cpu = []
        mem = []
        time = []
        log_path = downloadPath + '/' + fileName
        datafile_path = downloadPath + '/dockerData.js'

        log_info = fileName.replace('.log', '').replace('_', '-').split('-')
        cpu_core = int(log_info[1].split('C')[0])
        memory_size = int(log_info[1].split('C')[1].split('G')[0])
        start_time = log_info[3]

        label_time = datetime.datetime.strptime(start_time, '%Y%m%d%H%M%S')

        log_file = open(log_path, 'r', encoding='UTF8')
        for line in log_file:
            label_time = label_time + datetime.timedelta(seconds=0.5)
            values = line.split()

            time.append(label_time.strftime('%H:%M:%S'))
            cpu.append(round(float(values[1][0:-1]) / cpu_core, 2))
            mem.append(round(float(values[2][0:-3]), 2))
        log_file.close()

        jsonData = {
            'time': time,
            'cpu': cpu,
            'mem': mem,
            'cpu_core': cpu_core,
            'memory_size': memory_size
        }

        data_file = open(datafile_path, 'w', encoding='UTF8')
        data_file.write('var data = ' + str(jsonData).replace('\'', '\"'))
        data_file.close()
