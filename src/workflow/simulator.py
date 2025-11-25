# T4: Implement core simulation loop

import time
from typing import List, Dict

from src.logger import get_logger
from src.llms.llm_client import get_llm_client

log = get_logger(__name__)

class AutonomousSimulator:
    """
    The core of the autonomous LLM simulator.
    """

    def __init__(self, objective: str, llm_provider: str = "mock", llm_api_key: str = None):
        """
        Initializes the simulator.
        """
        self.objective = objective
        self.llm_client = get_llm_client(provider=llm_provider, api_key=llm_api_key)
        self.task_list = []
        self.completed_tasks = []
        log.info(f"Initialized AutonomousSimulator with objective: '{self.objective}'")

    def _generate_initial_plan(self):
        """
        Generates the initial plan based on the objective.
        """
        prompt = f"Based on the objective '{self.objective}', create a plan of tasks to accomplish it. Plan:"
        plan_text = self.llm_client.generate_text(prompt)
        self.task_list = self._parse_plan(plan_text)
        log.info(f"Generated initial plan with {len(self.task_list)} tasks.")

    def _parse_plan(self, plan_text: str) -> List[str]:
        """
        Parses the text of a plan into a list of tasks.
        """
        tasks = [
            task.strip() for task in plan_text.strip().split("\n") if task.strip()
        ]
        # A more robust implementation would parse numbered lists, etc.
        return [t.split(":", 1)[1].strip() for t in tasks if ":" in t]


    def run_simulation(self, max_iterations: int = 5):
        """
        Runs the main simulation loop.
        """
        log.info("Starting simulation loop.")
        self._generate_initial_plan()

        iteration = 0
        while self.task_list and iteration < max_iterations:
            task = self.task_list.pop(0)
            log.info(f"Executing task: '{task}'")

            # Simulate task execution by asking the LLM to "execute" it
            execution_prompt = f"Execute the following task: '{task}'. Result:"
            result = self.llm_client.generate_text(execution_prompt)

            self.completed_tasks.append({"task": task, "result": result})
            log.info(f"Task completed. Result: '{result}'")

            # In a real implementation, we might generate new tasks based on the result
            # For this mock, we'll just work through the initial list.

            time.sleep(1)  # To make the simulation observable
            iteration += 1

        log.info("Simulation loop finished.")
        if not self.task_list:
            log.info("All tasks completed.")
        else:
            log.warning("Max iterations reached, but tasks remain.")

        self._print_summary()

    def _print_summary(self):
        """
        Prints a summary of the completed tasks.
        """
        print("\n--- Simulation Summary ---")
        print(f"Objective: {self.objective}")
        print("\nCompleted Tasks:")
        for i, task_info in enumerate(self.completed_tasks, 1):
            print(f"  {i}. Task: {task_info['task']}")
            print(f"     Result: {task_info['result']}")
        print("--------------------------\n")
