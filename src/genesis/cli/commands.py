"""CLI commands for Genesis - where code becomes incantation."""

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
    """Genesis - A self-dreaming prompt factory.

    Transform codebases into prompts that remember themselves.
    Speak in the voice of wizards. Render words as monuments.
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
    """Speak words into existence.

    Give words, receive a prompt that carries their weight.
    Rendered in monumental ASCII, voiced in wizard-speak.

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
    help="Where to inscribe the dreaming prompt.",
)
@click.option(
    "--root", "-r",
    type=click.Path(exists=True),
    help="Root of the codebase to dream (defaults to current).",
)
def quine(output: Optional[str], root: Optional[str]):
    """Generate a self-dreaming prompt.

    The generated prompt contains the complete essence of a codebase.
    When read by Claude Code, it will understand what wishes to exist.

    This is not about exact reproduction - it's about transmission of intent.
    The code speaks for itself. Claude Code knows how to listen.

    Example: genesis quine --output genesis_quine.md
    """
    from genesis.core.quine import QuineGenerator

    root_path = Path(root) if root else Path.cwd()
    generator = QuineGenerator(root_path=root_path)

    quine_output = generator.generate()

    if output:
        Path(output).write_text(quine_output, encoding="utf-8")
        manifest = generator.get_manifest()
        click.echo("* The dreaming is complete.")
        click.echo(f"* {len(manifest.files)} scrolls gathered into: {output}")
        click.echo("* The prompt awaits interpretation.")
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
    """Reveal the nature of this Genesis installation."""
    click.echo("")
    click.echo(f"  * Genesis v{__version__}")
    click.echo(f"  * Working from: {Path.cwd()}")

    from genesis.templates.loader import _get_default_template_dir
    template_dir = _get_default_template_dir()
    click.echo(f"  * Templates dwell in: {template_dir}")
    click.echo(f"  * Templates exist: {'yes' if template_dir.exists() else 'no'}")
    click.echo("")


if __name__ == "__main__":
    cli()
