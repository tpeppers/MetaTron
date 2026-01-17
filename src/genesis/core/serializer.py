"""Repository serialization - capturing the essence of a codebase."""

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterator


# Ephemera to exclude - things that don't define the soul of a project
EPHEMERA = {
    "__pycache__",
    ".git",
    ".gitignore",
    "*.pyc",
    "*.pyo",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    "*.egg-info",
    "dist",
    "build",
    ".venv",
    "venv",
    ".env",
}


@dataclass
class FileEntry:
    """A single scroll in the repository."""

    path: str
    content: str

    def to_dict(self) -> dict:
        """Convert to dictionary representation."""
        return {
            "path": self.path,
            "content": self.content,
        }


@dataclass
class RepoManifest:
    """The complete memory of a repository - all its scrolls gathered."""

    files: list[FileEntry] = field(default_factory=list)
    root_path: str = ""

    def to_dict(self) -> dict:
        """Convert to dictionary representation."""
        return {
            "root_path": self.root_path,
            "files": [f.to_dict() for f in self.files],
        }

    def to_json(self, indent: int = 2) -> str:
        """Serialize to JSON string."""
        return json.dumps(self.to_dict(), indent=indent)


class RepoSerializer:
    """Gathers the scrolls of a repository into a single manifest."""

    def __init__(self, root_path: Path | None = None):
        """Initialize the gatherer.

        Args:
            root_path: Root path of repository. Defaults to current directory.
        """
        self.root_path = root_path or Path.cwd()

    def _is_essential(self, path: Path) -> bool:
        """Determine if a path represents essential code, not ephemera."""
        for part in path.parts:
            if part in EPHEMERA:
                return False
            for pattern in EPHEMERA:
                if "*" in pattern and path.match(pattern):
                    return False
        return True

    def _gather_scrolls(self) -> Iterator[Path]:
        """Wander through the repository, gathering all essential scrolls."""
        for path in self.root_path.rglob("*"):
            if path.is_file() and self._is_essential(path.relative_to(self.root_path)):
                yield path

    def serialize(self) -> RepoManifest:
        """Read the repository and remember it.

        Returns:
            RepoManifest containing the essence of all files.
        """
        files = []

        for file_path in sorted(self._gather_scrolls()):
            try:
                content = file_path.read_text(encoding="utf-8")
                rel_path = file_path.relative_to(self.root_path)
                files.append(FileEntry(
                    path=str(rel_path).replace("\\", "/"),
                    content=content,
                ))
            except (UnicodeDecodeError, PermissionError):
                # Some things are not meant to be read as text
                continue

        return RepoManifest(
            files=files,
            root_path=str(self.root_path.name),
        )

    def to_json(self, indent: int = 2) -> str:
        """Serialize to JSON directly.

        Returns:
            JSON string of repository manifest.
        """
        return self.serialize().to_json(indent=indent)
