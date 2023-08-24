import unittest
from airflow.models import DagBag

class TestOrderFulfillmentDAG(unittest.TestCase):

    def setUp(self):
        self.dagbag = DagBag(include_examples=False)
        self.dag_id = 'orders_dag'
        self.dag = self.dagbag.get_dag(self.dag_id)

    def test_dag_load(self):
        self.assertNotEqual(self.dag, None)
        self.assertEqual(self.dag.dag_id, self.dag_id)

    def test_tasks(self):
        task_ids = ['start_task', 'process_orders_task', 'generate_invoice_task', 'end_task']
        for task_id in task_ids:
            task = self.dag.get_task(task_id)
            self.assertIsNotNone(task)
            self.assertTrue(task.has_dag(self.dag))
            self.assertTrue(task.upstream_task_ids, msg=f"{task_id} has no upstream tasks")
            self.assertTrue(task.downstream_task_ids, msg=f"{task_id} has no downstream tasks")

if __name__ == '__main__':
    unittest.main()