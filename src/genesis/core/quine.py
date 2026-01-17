"""Quine generation - a codebase dreaming itself into words."""

from pathlib import Path
from typing import Optional

from genesis.core.serializer import RepoSerializer, RepoManifest
from genesis.templates.loader import TemplateLoader


class QuineGenerator:
    """
    Transforms a repository into a self-describing prompt.

    Not for exact reproduction, but for transmission of essence.
    The prompt is meant to be read by Claude Code, who will
    understand what wishes to exist and give it form.
    """

    def __init__(
        self,
        root_path: Optional[Path] = None,
        template_dir: Optional[Path] = None,
    ):
        """Initialize the dreamer.

        Args:
            root_path: Root of the codebase to dream.
            template_dir: Where the templates live.
        """
        self.root_path = root_path or Path.cwd()
        self.serializer = RepoSerializer(self.root_path)
        self.loader = TemplateLoader(template_dir)

    def generate(self) -> str:
        """
        Generate a prompt that contains the complete essence of this codebase.

        When read by Claude Code, the prompt invokes the codebase into being.
        No explicit instructions needed - the code speaks for itself.

        Returns:
            A dreaming prompt, ready to be interpreted.
        """
        manifest = self.serializer.serialize()

        context = {
            "manifest": manifest,
            "files": manifest.files,
            "root_name": manifest.root_path,
            "file_count": len(manifest.files),
        }

        return self.loader.render("quine_prompt.j2", context)

    def get_manifest(self) -> RepoManifest:
        """Retrieve the manifest of scrolls.

        Returns:
            The gathered memory of this repository.
        """
        return self.serializer.serialize()
