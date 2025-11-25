# T8: Test & validate simulator

import unittest
from unittest.mock import patch, MagicMock

from src.workflow.simulator import AutonomousSimulator

class TestAutonomousSimulator(unittest.TestCase):
    """
    Unit tests for the AutonomousSimulator.
    """

    def test_initialization(self):
        """
        Tests that the simulator initializes correctly.
        """
        objective = "Test objective"
        simulator = AutonomousSimulator(objective=objective)
        self.assertEqual(simulator.objective, objective)
        self.assertIsNotNone(simulator.llm_client)
        self.assertEqual(simulator.task_list, [])
        self.assertEqual(simulator.completed_tasks, [])

    @patch('src.workflow.simulator.get_llm_client')
    def test_run_simulation(self, mock_get_llm_client):
        """
        Tests the simulation loop runs without errors.
        """
        # Configure the mock LLM client
        mock_llm = MagicMock()
        mock_llm.generate_text.side_effect = [
            "1. Task 1: Do something.",
            "Execution of Task 1 successful.",
        ]
        mock_get_llm_client.return_value = mock_llm

        objective = "Test simulation run"
        simulator = AutonomousSimulator(objective=objective)
        
        # We can run with max_iterations=1 to test one loop
        simulator.run_simulation(max_iterations=1)

        # Check that the plan was generated and a task was executed
        self.assertEqual(len(simulator.completed_tasks), 1)
        self.assertEqual(simulator.completed_tasks[0]['task'], 'Do something.')
        self.assertEqual(mock_llm.generate_text.call_count, 2)

if __name__ == '__main__':
    unittest.main()
