import pytest
from airflow.models import DagBag
from airflow.utils.dates import days_ago

@pytest.fixture
def dag_bag():
    return DagBag(include_examples=False)

@pytest.fixture
def dag(dag_bag):
    return dag_bag.get_dag('inventory_management_dag')

def test_dag_load(dag_bag):
    assert dag_bag.dags is not None
    assert 'inventory_management_dag' in dag_bag.dags

def test_task_count(dag):
    assert len(dag.tasks) == 4

def test_dependencies(dag):
    tasks = dag.tasks
    assert tasks[1].upstream_task_ids == ['start_task']
    assert tasks[2].upstream_task_ids == ['ingest_inventory_data_task']
    assert tasks[3].upstream_task_ids == ['analyze_inventory_task']

def test_start_date(dag):
    assert dag.start_date == days_ago(1)