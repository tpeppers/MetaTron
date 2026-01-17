"""Core prompt generation engine."""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from genesis.templates.loader import TemplateLoader
from genesis.fonts.ascii_art import ASCIIRenderer
from genesis.voice.gandalf import GandalfVoice


@dataclass
class PromptConfig:
    """Configuration for prompt generation."""

    words: list[str] = field(default_factory=list)
    font: str = "banner"
    voice: str = "gandalf"
    include_ascii_header: bool = True
    template_name: str = "genesis_prompt.j2"


class PromptEngine:
    """Central orchestrator for prompt generation."""

    def __init__(self, template_dir: Optional[Path] = None):
        """Initialize the prompt engine.

        Args:
            template_dir: Optional custom template directory.
        """
        self.loader = TemplateLoader(template_dir)
        self.ascii_renderer = ASCIIRenderer()
        self.voice = GandalfVoice()

    def generate(self, config: PromptConfig) -> str:
        """Generate a prompt from configuration.

        Args:
            config: Prompt configuration options.

        Returns:
            Generated prompt string.
        """
        context = {
            "words": config.words,
            "font": config.font,
        }

        # Generate ASCII header if requested
        if config.include_ascii_header and config.words:
            header = self.ascii_renderer.render_genesis_header(
                config.words,
                font=config.font
            )
            context["ascii_header"] = header
        else:
            context["ascii_header"] = ""

        # Apply voice transformation
        if config.voice == "gandalf":
            context["voice"] = self.voice
            context["opening"] = self.voice.opening_proclamation()
            context["closing"] = self.voice.closing_proclamation()

        # Render template
        return self.loader.render(config.template_name, context)

    def generate_quine(self, output_path: Optional[Path] = None) -> str:
        """Generate a self-reproducing prompt.

        Args:
            output_path: Optional path to write the quine output.

        Returns:
            Quine prompt string.
        """
        from genesis.core.quine import QuineGenerator

        generator = QuineGenerator()
        quine_output = generator.generate()

        if output_path:
            output_path.write_text(quine_output, encoding="utf-8")

        return quine_output
