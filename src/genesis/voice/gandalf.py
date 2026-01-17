"""Gandalf voice transformation for narrative style."""

import re
from typing import Optional


class GandalfVoice:
    """Transforms text into a Gandalf-like wizard narrative voice."""

    # Vocabulary mappings for wizard-speak
    VOCABULARY = {
        # Technical terms -> wizard terms
        "code": "runes",
        "codes": "runes",
        "coding": "inscribing runes",
        "file": "scroll",
        "files": "scrolls",
        "function": "incantation",
        "functions": "incantations",
        "variable": "vessel",
        "variables": "vessels",
        "class": "order",
        "classes": "orders",
        "method": "ritual",
        "methods": "rituals",
        "error": "dark omen",
        "errors": "dark omens",
        "bug": "gremlin",
        "bugs": "gremlins",
        "debug": "exorcise",
        "debugging": "exorcising",
        "compile": "forge",
        "compiling": "forging",
        "compiled": "forged",
        "run": "invoke",
        "running": "invoking",
        "execute": "cast",
        "executing": "casting",
        "executed": "cast",
        "test": "trial",
        "tests": "trials",
        "testing": "conducting trials",
        "repository": "tome",
        "repositories": "tomes",
        "directory": "chamber",
        "directories": "chambers",
        "folder": "chamber",
        "folders": "chambers",
        "module": "grimoire",
        "modules": "grimoires",
        "package": "artifact",
        "packages": "artifacts",
        "library": "ancient library",
        "libraries": "ancient libraries",
        "import": "summon",
        "imports": "summons",
        "importing": "summoning",
        "export": "bestow",
        "exports": "bestows",
        "server": "tower",
        "servers": "towers",
        "database": "vault",
        "databases": "vaults",
        "user": "seeker",
        "users": "seekers",
        "developer": "wizard",
        "developers": "wizards",
        "programmer": "wizard",
        "programmers": "wizards",
        "computer": "thinking machine",
        "computers": "thinking machines",
        "algorithm": "spell",
        "algorithms": "spells",
        "data": "essence",
        "string": "inscription",
        "strings": "inscriptions",
        "integer": "counting stone",
        "integers": "counting stones",
        "boolean": "truth rune",
        "booleans": "truth runes",
        "array": "quiver",
        "arrays": "quivers",
        "list": "scroll of many",
        "lists": "scrolls of many",
        "dictionary": "book of mappings",
        "dictionaries": "books of mappings",
        "loop": "cycle of repetition",
        "loops": "cycles of repetition",
        "if": "should it be that",
        "else": "otherwise",
        "return": "yield forth",
        "print": "proclaim",
        "log": "chronicle",
        "logging": "chronicling",
    }

    # Opening proclamations
    OPENINGS = [
        "Hearken well, for I shall speak of matters most arcane...",
        "In the tongue of the ancient wizards, let me illuminate...",
        "As the Grey Wanderer once taught, wisdom comes to those who listen...",
        "From the depths of the Codex Eternal, I reveal...",
        "By the light of the Two Trees, attend to these words...",
    ]

    # Closing proclamations
    CLOSINGS = [
        "Thus it has been inscribed, and thus it shall be.",
        "Go now, and may your runes compile true.",
        "The way is clear. Walk it with wisdom.",
        "Remember: even the smallest incantation can change the world.",
        "Until the stars fade, these truths shall endure.",
    ]

    def __init__(self, intensity: float = 1.0):
        """Initialize the voice transformer.

        Args:
            intensity: How strongly to apply transformations (0.0-1.0).
        """
        self.intensity = max(0.0, min(1.0, intensity))

    def transform(self, text: str) -> str:
        """Transform text using wizard vocabulary.

        Args:
            text: Input text to transform.

        Returns:
            Transformed text with wizard vocabulary.
        """
        result = text

        # Apply vocabulary substitutions
        for original, replacement in self.VOCABULARY.items():
            # Use word boundaries for accurate replacement
            pattern = rf"\b{re.escape(original)}\b"
            result = re.sub(pattern, replacement, result, flags=re.IGNORECASE)

        return result

    def opening_proclamation(self, index: Optional[int] = None) -> str:
        """Get an opening proclamation.

        Args:
            index: Specific proclamation index, or None for first.

        Returns:
            Opening proclamation string.
        """
        if index is not None:
            return self.OPENINGS[index % len(self.OPENINGS)]
        return self.OPENINGS[0]

    def closing_proclamation(self, index: Optional[int] = None) -> str:
        """Get a closing proclamation.

        Args:
            index: Specific proclamation index, or None for first.

        Returns:
            Closing proclamation string.
        """
        if index is not None:
            return self.CLOSINGS[index % len(self.CLOSINGS)]
        return self.CLOSINGS[0]

    def wrap_in_narrative(self, text: str, opening_idx: int = 0, closing_idx: int = 0) -> str:
        """Wrap text in narrative opening and closing.

        Args:
            text: Text to wrap.
            opening_idx: Index of opening to use.
            closing_idx: Index of closing to use.

        Returns:
            Text wrapped in narrative bookends.
        """
        opening = self.opening_proclamation(opening_idx)
        closing = self.closing_proclamation(closing_idx)
        transformed = self.transform(text)

        return f"{opening}\n\n{transformed}\n\n{closing}"
