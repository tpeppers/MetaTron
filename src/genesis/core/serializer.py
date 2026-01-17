"""Repository serialization for quine generation."""

import hashlib
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterator


# Patterns to exclude from serialization
EXCLUDE_PATTERNS = {
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
    """A single file entry in the repository."""

    path: str
    content: str
    checksum: str = ""

    def __post_init__(self):
        if not self.checksum:
            self.checksum = self._compute_checksum()

    def _compute_checksum(self) -> str:
        """Compute SHA256 checksum of content."""
        return hashlib.sha256(self.content.encode("utf-8")).hexdigest()[:16]

    def to_dict(self) -> dict:
        """Convert to dictionary representation."""
        return {
            "path": self.path,
            "content": self.content,
            "checksum": self.checksum,
        }


@dataclass
class RepoManifest:
    """Complete repository manifest."""

    files: list[FileEntry] = field(default_factory=list)
    root_path: str = ""
    total_checksum: str = ""

    def compute_total_checksum(self) -> str:
        """Compute checksum of entire repository."""
        combined = "".join(f.checksum for f in sorted(self.files, key=lambda x: x.path))
        return hashlib.sha256(combined.encode("utf-8")).hexdigest()[:32]

    def to_dict(self) -> dict:
        """Convert to dictionary representation."""
        return {
            "root_path": self.root_path,
            "total_checksum": self.total_checksum or self.compute_total_checksum(),
            "files": [f.to_dict() for f in self.files],
        }

    def to_json(self, indent: int = 2) -> str:
        """Serialize to JSON string."""
        return json.dumps(self.to_dict(), indent=indent)


class RepoSerializer:
    """Serializes a repository to a manifest."""

    def __init__(self, root_path: Path | None = None):
        """Initialize serializer.

        Args:
            root_path: Root path of repository. Defaults to current directory.
        """
        self.root_path = root_path or Path.cwd()

    def _should_include(self, path: Path) -> bool:
        """Check if path should be included in manifest."""
        # Check each part of the path against exclusions
        for part in path.parts:
            if part in EXCLUDE_PATTERNS:
                return False
            # Check glob patterns
            for pattern in EXCLUDE_PATTERNS:
                if "*" in pattern and path.match(pattern):
                    return False
        return True

    def _iter_files(self) -> Iterator[Path]:
        """Iterate over all files in repository."""
        for path in self.root_path.rglob("*"):
            if path.is_file() and self._should_include(path.relative_to(self.root_path)):
                yield path

    def serialize(self) -> RepoManifest:
        """Serialize repository to manifest.

        Returns:
            RepoManifest containing all files.
        """
        files = []

        for file_path in sorted(self._iter_files()):
            try:
                content = file_path.read_text(encoding="utf-8")
                rel_path = file_path.relative_to(self.root_path)
                files.append(FileEntry(
                    path=str(rel_path).replace("\\", "/"),
                    content=content,
                ))
            except (UnicodeDecodeError, PermissionError):
                # Skip binary files or inaccessible files
                continue

        manifest = RepoManifest(
            files=files,
            root_path=str(self.root_path.name),
        )
        manifest.total_checksum = manifest.compute_total_checksum()

        return manifest

    def to_json(self, indent: int = 2) -> str:
        """Serialize repository directly to JSON.

        Returns:
            JSON string of repository manifest.
        """
        return self.serialize().to_json(indent=indent)
