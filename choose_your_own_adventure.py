"""Choose‑Your‑Own‑Adventure game engine (stub).

This module provides placeholder functions for a text‑based adventure game.
You will implement story loading and game logic in later ships.  For now,
the functions raise `NotImplementedError` and the script prints a greeting
when executed directly.
"""

def load_story(file_path: str) -> dict:
    """Load a story definition from a file and return it as a data structure.

    The story file might be JSON, YAML or a custom format.  In Ship 4 you
    will parse the file and return a dictionary or another structure
    representing the narrative.

    Args:
        file_path: Path to the story file.

    Returns:
        A dictionary describing the story and its choices.
    """
    raise NotImplementedError("load_story is not yet implemented")


def start_game(story: dict) -> None:
    """Begin the adventure using the provided story data.

    This function will handle user input, present choices and traverse
    the story graph.  For Ship 3 it is unimplemented and will be filled
    in during later ships.

    Args:
        story: The story data structure returned by `load_story`.
    """
    raise NotImplementedError("start_game is not yet implemented")


def main() -> None:
    """Entry point for the adventure game.

    When run directly, this prints a greeting.  You will replace this
    with calls to `load_story` and `start_game` after implementing them.
    """
    print("Welcome to the Choose‑Your‑Own‑Adventure game!")


if __name__ == "__main__":
    main()