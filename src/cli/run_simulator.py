# T7: Build CLI / simple UI

import argparse
from src.workflow.simulator import AutonomousSimulator

def main():
    """
    Main function to run the autonomous LLM simulator from the command line.
    """
    parser = argparse.ArgumentParser(
        description="Run the Autonomous LLM Simulator."
    )
    parser.add_argument(
        "objective",
        type=str,
        help="The high-level objective for the simulator to achieve.",
    )
    parser.add_argument(
        "--max-iterations",
        type=int,
        default=5,
        help="The maximum number of tasks to execute.",
    )
    parser.add_argument(
        "--llm-provider",
        type=str,
        default="mock",
        help="The LLM provider to use (e.g., 'mock', 'openai').",
    )

    args = parser.parse_args()

    # In a real app, the API key would be loaded securely (e.g., from env vars)
    llm_api_key = "dummy_key_for_now"

    simulator = AutonomousSimulator(
        objective=args.objective,
        llm_provider=args.llm_provider,
        llm_api_key=llm_api_key,
    )
    simulator.run_simulation(max_iterations=args.max_iterations)

if __name__ == "__main__":
    main()
