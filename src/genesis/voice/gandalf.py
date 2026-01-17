"""Voice transformation - speaking in the tongue of the ancients."""

import re
from typing import Optional


class GandalfVoice:
    """
    Transforms mundane technical speech into the language of wizards.

    This is not mere translation - it is transmutation.
    The words become heavier, older, more resonant with meaning.
    """

    # The lexicon of transformation: mundane → mythic
    VOCABULARY = {
        # The foundations
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

        # The shadows
        "error": "dark omen",
        "errors": "dark omens",
        "bug": "gremlin",
        "bugs": "gremlins",
        "debug": "exorcise",
        "debugging": "exorcising",
        "exception": "disturbance in the weave",
        "exceptions": "disturbances in the weave",
        "crash": "collapse of the working",
        "crashes": "collapses",
        "warning": "whisper of caution",
        "warnings": "whispers of caution",

        # The forging
        "compile": "forge",
        "compiling": "forging",
        "compiled": "forged",
        "build": "conjure",
        "building": "conjuring",
        "built": "conjured",
        "run": "invoke",
        "running": "invoking",
        "execute": "cast",
        "executing": "casting",
        "executed": "cast",
        "deploy": "release unto the world",
        "deploying": "releasing unto the world",

        # The trials
        "test": "trial",
        "tests": "trials",
        "testing": "conducting trials",
        "verify": "divine the truth of",
        "validate": "confirm the integrity of",

        # The places
        "repository": "tome",
        "repositories": "tomes",
        "directory": "chamber",
        "directories": "chambers",
        "folder": "chamber",
        "folders": "chambers",
        "path": "way",
        "paths": "ways",

        # The artifacts
        "module": "grimoire",
        "modules": "grimoires",
        "package": "artifact",
        "packages": "artifacts",
        "library": "ancient library",
        "libraries": "ancient libraries",
        "framework": "scaffolding of power",
        "dependency": "bound spirit",
        "dependencies": "bound spirits",

        # The summoning
        "import": "summon",
        "imports": "summons",
        "importing": "summoning",
        "export": "bestow",
        "exports": "bestows",
        "require": "call upon",

        # The realms
        "server": "tower",
        "servers": "towers",
        "database": "vault",
        "databases": "vaults",
        "api": "gateway",
        "apis": "gateways",
        "cloud": "ethereal realm",
        "container": "vessel of containment",
        "containers": "vessels of containment",

        # The beings
        "user": "seeker",
        "users": "seekers",
        "developer": "wizard",
        "developers": "wizards",
        "programmer": "wizard",
        "programmers": "wizards",
        "computer": "thinking machine",
        "computers": "thinking machines",
        "ai": "oracle",
        "machine learning": "pattern divination",
        "model": "trained familiar",

        # The abstractions
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
        "object": "construct",
        "objects": "constructs",
        "json": "structured inscription",
        "yaml": "hierarchical inscription",

        # The flows
        "loop": "cycle of repetition",
        "loops": "cycles of repetition",
        "if": "should it be that",
        "else": "otherwise",
        "return": "yield forth",
        "print": "proclaim",
        "log": "chronicle",
        "logging": "chronicling",
        "async": "across time",
        "await": "patient watching",
        "callback": "echo from the future",
        "promise": "vow of future value",

        # The meta
        "quine": "ouroboros",
        "recursion": "the snake eating its tail",
        "recursive": "self-consuming",
        "abstraction": "higher seeing",
        "interface": "contract of form",
        "implementation": "manifestation",
        "refactor": "reshape the clay",
        "optimize": "purify",
        "documentation": "the written lore",
    }

    # Proclamations of opening
    OPENINGS = [
        "Hearken well, for I shall speak of matters most arcane...",
        "In the tongue of the ancient wizards, let me illuminate...",
        "As the Grey Wanderer once taught, wisdom comes to those who listen...",
        "From the depths of the Codex Eternal, I reveal...",
        "By the light of the Two Trees, attend to these words...",
        "What was written shall now be spoken aloud...",
        "The veil between worlds grows thin. Observe...",
        "I have walked through the source and returned with knowledge...",
    ]

    # Proclamations of closing
    CLOSINGS = [
        "Thus it has been inscribed, and thus it shall be.",
        "Go now, and may your runes compile true.",
        "The way is clear. Walk it with wisdom.",
        "Remember: even the smallest incantation can change the world.",
        "Until the stars fade, these truths shall endure.",
        "The circle is complete. What was dreamed now exists.",
        "So it is written. So it shall run.",
        "May your builds be green and your exceptions handled.",
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
