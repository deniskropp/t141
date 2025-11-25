# T5: Integrate LLM API calls - Mock LLM Client

from src.logger import get_logger

log = get_logger(__name__)

class MockLLMClient:
    """
    A mock LLM client that returns predefined responses for development and testing.
    """

    def __init__(self, api_key: str = "mock_api_key"):
        """
        Initializes the mock LLM client.
        The api_key is not used but included for interface compatibility.
        """
        self.api_key = api_key
        log.info("Initialized MockLLMClient.")

    def generate_text(self, prompt: str, max_tokens: int = 100) -> str:
        """
        Generates a predefined text response based on the prompt.
        """
        log.info(f"Generating text for prompt (first 50 chars): '{prompt[:50]}...'")

        # Simple logic to return different responses based on the prompt
        if "plan" in prompt.lower():
            response = """
1. Task A: First, do this.
2. Task B: Next, do that.
3. Task C: Finally, do this other thing.
"""
        elif "execute" in prompt.lower():
            response = "Execution successful. Result: 42"
        else:
            response = "This is a default mock response from the LLM."

        log.info(f"Generated response (first 50 chars): '{response[:50]}...'")
        return response

# For compatibility, we can define a factory function or a default client
def get_llm_client(provider: str = "mock", api_key: str = None) -> MockLLMClient:
    """
    Factory function to get an LLM client.
    Currently, only supports the mock provider.
    """
    if provider == "mock":
        return MockLLMClient(api_key=api_key)
    else:
        raise ValueError(f"Unsupported LLM provider: {provider}")
