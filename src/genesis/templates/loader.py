"""Jinja2 template loading and rendering."""

from pathlib import Path
from typing import Any, Optional

from jinja2 import Environment, FileSystemLoader, select_autoescape


def _get_default_template_dir() -> Path:
    """Get the default template directory."""
    # First check if we're in a package context
    package_dir = Path(__file__).parent.parent.parent.parent / "templates"
    if package_dir.exists():
        return package_dir

    # Fall back to current working directory
    cwd_templates = Path.cwd() / "templates"
    if cwd_templates.exists():
        return cwd_templates

    # Return package dir even if doesn't exist (will error on render)
    return package_dir


class TemplateLoader:
    """Handles Jinja2 template loading and rendering."""

    def __init__(self, template_dir: Optional[Path] = None):
        """Initialize the template loader.

        Args:
            template_dir: Optional custom template directory.
        """
        self.template_dir = template_dir or _get_default_template_dir()

        self.env = Environment(
            loader=FileSystemLoader(self.template_dir),
            autoescape=select_autoescape(["html", "xml"]),
            trim_blocks=True,
            lstrip_blocks=True,
        )

        # Register custom filters
        self._register_filters()

    def _register_filters(self):
        """Register custom Jinja2 filters."""
        self.env.filters["gandalf"] = self._gandalf_filter
        self.env.filters["indent_block"] = self._indent_block_filter

    @staticmethod
    def _gandalf_filter(text: str) -> str:
        """Transform text using Gandalf voice."""
        from genesis.voice.gandalf import GandalfVoice
        voice = GandalfVoice()
        return voice.transform(text)

    @staticmethod
    def _indent_block(text: str, spaces: int = 4) -> str:
        """Indent a block of text."""
        indent = " " * spaces
        return "\n".join(indent + line for line in text.split("\n"))

    @staticmethod
    def _indent_block_filter(text: str, width: int = 4) -> str:
        """Jinja2 filter to indent text block."""
        indent = " " * width
        lines = text.split("\n")
        return "\n".join(indent + line if line.strip() else line for line in lines)

    def render(self, template_name: str, context: dict[str, Any]) -> str:
        """Render a template with context.

        Args:
            template_name: Name of template file.
            context: Dictionary of template variables.

        Returns:
            Rendered template string.
        """
        template = self.env.get_template(template_name)
        return template.render(**context)

    def render_string(self, template_str: str, context: dict[str, Any]) -> str:
        """Render a template string with context.

        Args:
            template_str: Template as string.
            context: Dictionary of template variables.

        Returns:
            Rendered string.
        """
        template = self.env.from_string(template_str)
        return template.render(**context)

    def list_templates(self) -> list[str]:
        """List available templates.

        Returns:
            List of template names.
        """
        return self.env.list_templates()
