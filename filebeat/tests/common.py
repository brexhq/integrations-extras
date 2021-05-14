import os

from datadog_checks.dev.docker import get_docker_hostname

HERE = os.path.dirname(os.path.abspath(__file__))
DOCKER_DIR = os.path.join(HERE, "docker")
HOST = get_docker_hostname()
URL = 'http://{}:5066'.format(HOST)
ENDPOINT = '{}/stats'.format(URL)
BAD_ENDPOINT = 'http://{}:1234/stats'.format(HOST)
