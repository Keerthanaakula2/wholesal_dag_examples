import pytest
from airflow.models import DagBag
from airflow.utils.dates import days_ago

@pytest.fixture
def dag_bag():
    return DagBag(include_examples=False)

@pytest.fixture
def dag(dag_bag):
    return