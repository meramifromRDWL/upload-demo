"""hello_github: a minimal example package to test GitHub upload."""


def greet(name: str = "GitHub") -> str:
    """Return a greeting message."""
    return f"Hello, {name}! Uploaded from Trae Agent."


if __name__ == "__main__":
    print(greet())
