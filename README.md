# Autonomous LLM Simulator

This project is a self-contained system that emulates an LLM operating autonomously: it continuously generates prompts for itself, plans required sub-tasks, executes them, and iterates.

## About The Project

The **Autonomous LLM Simulator** is designed to simulate an autonomous Large Language Model (LLM) agent. Its core capabilities include:

*   **Self-Prompting:** Generates its own prompts based on an initial objective.
*   **Task Planning:** Creates a plan of tasks to achieve the goal of a prompt.
*   **Sandboxed Execution:** Executes tasks in a simulated environment.
*   **Iterative Loop:** Observes results and continues to self-prompt and execute until a completion condition is met.
*   **Safe & Observable:** Ensures safe execution and provides clear, structured logging.

This project is currently in a mock phase, using a `MockLLMClient` to simulate LLM interactions without needing an actual API key.

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

*   Python 3.10+

### Installation

1.  **Clone the repo**
    ```sh
    git clone https://github.com/your-org/autonomous-llm-simulator.git
    cd autonomous-llm-simulator
    ```
2.  **Create and activate a virtual environment**
    ```sh
    python -m venv venv
    source venv/bin/activate
    ```
3.  **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```
    *(Note: Currently, no external dependencies are required for the mock version.)*

## Usage

The simulator is run from the command line. You must provide a high-level objective for the agent to accomplish.

```sh
python -m src.cli.run_simulator "Develop a plan to learn a new programming language"
```

### Command-Line Arguments

*   `objective` (required): The high-level objective for the simulator.
*   `--max-iterations` (optional): The maximum number of tasks to execute. Default: `5`.
*   `--llm-provider` (optional): The LLM provider to use. Default: `mock`.

## Running Tests

To run the test suite, use `pytest`:

```sh
pytest
```

## Project Structure

The project is organized as follows:

```
.
├── docs/                  # Documentation and architectural diagrams
├── src/                   # Source code
│   ├── cli/               # Command-line interface
│   ├── error_handling/    # Global error handling
│   ├── llms/              # LLM client integrations (currently mock)
│   ├── models/            # Database schemas
│   ├── workflow/          # Core simulation logic
│   └── logger.py          # Centralized logging configuration
├── tests/                 # Unit and integration tests
├── requirements.txt       # Python dependencies
└── README.md              # This file
```

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Project Link: [https://github.com/your-org/autonomous-llm-simulator](https://github.com/your-org/autonomous-llm-simulator)
