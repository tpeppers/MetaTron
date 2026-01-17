"""Quine generation - self-reproducing prompts."""

from pathlib import Path
from typing import Optional

from genesis.core.serializer import RepoSerializer, RepoManifest
from genesis.templates.loader import TemplateLoader


class QuineGenerator:
    """Generates self-reproducing prompts."""

    def __init__(
        self,
        root_path: Optional[Path] = None,
        template_dir: Optional[Path] = None,
    ):
        """Initialize quine generator.

        Args:
            root_path: Root path of repository to serialize.
            template_dir: Optional custom template directory.
        """
        self.root_path = root_path or Path.cwd()
        self.serializer = RepoSerializer(self.root_path)
        self.loader = TemplateLoader(template_dir)

    def generate(self) -> str:
        """Generate a self-reproducing prompt.

        The generated prompt, when given to Claude Code, will
        recreate the entire repository structure.

        Returns:
            Quine prompt string.
        """
        manifest = self.serializer.serialize()

        context = {
            "manifest": manifest,
            "files": manifest.files,
            "total_checksum": manifest.total_checksum,
            "root_name": manifest.root_path,
            "file_count": len(manifest.files),
        }

        return self.loader.render("quine_prompt.j2", context)

    def verify(self, generated_path: Path) -> bool:
        """Verify a generated repository matches the original.

        Args:
            generated_path: Path to generated repository.

        Returns:
            True if checksums match, False otherwise.
        """
        original_manifest = self.serializer.serialize()

        generated_serializer = RepoSerializer(generated_path)
        generated_manifest = generated_serializer.serialize()

        return original_manifest.total_checksum == generated_manifest.total_checksum

    def get_manifest(self) -> RepoManifest:
        """Get the repository manifest.

        Returns:
            RepoManifest of current repository.
        """
        return self.serializer.serialize()
