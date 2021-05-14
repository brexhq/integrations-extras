import os

import pytest

from datadog_checks.dev.docker import docker_run

from .common import DOCKER_DIR, ENDPOINT, URL

INSTANCE = {
    "stats_endpoint": ENDPOINT,
}


@pytest.fixture(scope="session")
def dd_environment():

    with docker_run(os.path.join(DOCKER_DIR, "docker-compose.yaml"), endpoints=URL):
        yield INSTANCE


@pytest.fixture
def instance():
    return INSTANCE.copy()
