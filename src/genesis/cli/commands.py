"""CLI commands for Genesis."""

from pathlib import Path
from typing import Optional

import click

from genesis import __version__
from genesis.core.engine import PromptEngine, PromptConfig
from genesis.fonts.ascii_art import ASCIIRenderer
from genesis.voice.gandalf import GandalfVoice


@click.group()
@click.version_option(version=__version__, prog_name="genesis")
def cli():
    """Genesis - A self-referential prompt factory.

    Generate prompts with ASCII art headers and wizard-speak,
    or create self-reproducing quine prompts.
    """
    pass


@cli.command()
@click.argument("words", nargs=-1, required=True)
@click.option(
    "--font", "-f",
    default="banner",
    help="ASCII art font to use for header.",
)
@click.option(
    "--voice", "-v",
    type=click.Choice(["gandalf", "none"]),
    default="gandalf",
    help="Narrative voice style.",
)
@click.option(
    "--no-header",
    is_flag=True,
    help="Omit ASCII art header.",
)
@click.option(
    "--output", "-o",
    type=click.Path(),
    help="Output file path.",
)
def create(
    words: tuple[str, ...],
    font: str,
    voice: str,
    no_header: bool,
    output: Optional[str],
):
    """Generate a prompt from words of creation.

    Example: genesis create let there be light
    """
    config = PromptConfig(
        words=list(words),
        font=font,
        voice=voice if voice != "none" else "",
        include_ascii_header=not no_header,
    )

    engine = PromptEngine()
    prompt = engine.generate(config)

    if output:
        Path(output).write_text(prompt, encoding="utf-8")
        click.echo(f"Prompt written to: {output}")
    else:
        click.echo(prompt)


@cli.command()
@click.option(
    "--output", "-o",
    type=click.Path(),
    help="Output file path for quine.",
)
@click.option(
    "--root", "-r",
    type=click.Path(exists=True),
    help="Root directory to serialize (defaults to current).",
)
def quine(output: Optional[str], root: Optional[str]):
    """Generate a self-reproducing prompt.

    The generated prompt contains the complete repository source
    and instructions for Claude Code to recreate it.

    Example: genesis quine --output genesis_quine.md
    """
    from genesis.core.quine import QuineGenerator

    root_path = Path(root) if root else Path.cwd()
    generator = QuineGenerator(root_path=root_path)

    quine_output = generator.generate()

    if output:
        Path(output).write_text(quine_output, encoding="utf-8")
        click.echo(f"Quine written to: {output}")
        manifest = generator.get_manifest()
        click.echo(f"Files serialized: {len(manifest.files)}")
        click.echo(f"Checksum: {manifest.total_checksum}")
    else:
        click.echo(quine_output)


@cli.command()
@click.argument("text")
@click.option(
    "--font", "-f",
    default="banner",
    help="ASCII art font to use.",
)
def ascii(text: str, font: str):
    """Render text as ASCII art.

    Example: genesis ascii "GENESIS" --font doom
    """
    renderer = ASCIIRenderer()

    if not renderer.validate_font(font):
        click.echo(f"Font '{font}' not found. Using 'standard'.", err=True)
        font = "standard"

    result = renderer.render(text, font=font)
    click.echo(result)


@cli.command()
@click.option(
    "--all", "-a", "show_all",
    is_flag=True,
    help="Show all available fonts (not just recommended).",
)
@click.option(
    "--preview", "-p",
    type=str,
    help="Preview fonts with sample text.",
)
def fonts(show_all: bool, preview: Optional[str]):
    """List available ASCII art fonts.

    Example: genesis fonts --preview HELLO
    """
    renderer = ASCIIRenderer()

    if show_all:
        font_list = renderer.list_fonts()
        click.echo(f"All available fonts ({len(font_list)}):")
    else:
        font_list = renderer.list_recommended_fonts()
        click.echo(f"Recommended fonts ({len(font_list)}):")

    if preview:
        for font_name in font_list:
            click.echo(f"\n--- {font_name} ---")
            try:
                click.echo(renderer.render(preview, font=font_name))
            except Exception:
                click.echo("(rendering failed)")
    else:
        for font_name in font_list:
            click.echo(f"  {font_name}")


@cli.command()
@click.argument("text")
def transform(text: str):
    """Transform text using Gandalf voice.

    Example: genesis transform "The code has a bug"
    """
    voice = GandalfVoice()
    result = voice.transform(text)
    click.echo(result)


@cli.command()
def info():
    """Show Genesis information and paths."""
    click.echo(f"Genesis v{__version__}")
    click.echo(f"Working directory: {Path.cwd()}")

    # Check template directory
    from genesis.templates.loader import _get_default_template_dir
    template_dir = _get_default_template_dir()
    click.echo(f"Template directory: {template_dir}")
    click.echo(f"Templates exist: {template_dir.exists()}")


if __name__ == "__main__":
    cli()
