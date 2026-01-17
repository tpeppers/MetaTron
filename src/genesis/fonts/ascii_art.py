"""ASCII art rendering using pyfiglet."""

from typing import Optional

import pyfiglet


class ASCIIRenderer:
    """Renders ASCII art text using various fonts."""

    # Recommended fonts for Genesis
    RECOMMENDED_FONTS = [
        "banner",
        "doom",
        "slant",
        "standard",
        "big",
        "block",
        "digital",
        "isometric1",
        "letters",
        "alligator",
    ]

    def __init__(self, default_font: str = "banner"):
        """Initialize the ASCII renderer.

        Args:
            default_font: Default font to use for rendering.
        """
        self.default_font = default_font

    def render(self, text: str, font: Optional[str] = None) -> str:
        """Render text as ASCII art.

        Args:
            text: Text to render.
            font: Font to use (defaults to instance default).

        Returns:
            ASCII art string.
        """
        font = font or self.default_font

        try:
            fig = pyfiglet.Figlet(font=font)
            return fig.renderText(text).rstrip()
        except pyfiglet.FontNotFound:
            # Fall back to standard font if requested font not found
            fig = pyfiglet.Figlet(font="standard")
            return fig.renderText(text).rstrip()

    def render_genesis_header(
        self,
        words: list[str],
        font: Optional[str] = None,
    ) -> str:
        """Render a stacked Genesis header with multiple words.

        Each word is rendered on its own line(s) in ASCII art,
        creating a vertical stack of stylized words.

        Args:
            words: List of words to render.
            font: Font to use for rendering.

        Returns:
            Stacked ASCII art header.
        """
        if not words:
            return ""

        font = font or self.default_font
        rendered_words = []

        for word in words:
            rendered = self.render(word.upper(), font=font)
            rendered_words.append(rendered)

        return "\n".join(rendered_words)

    def list_fonts(self) -> list[str]:
        """List all available fonts.

        Returns:
            List of font names.
        """
        return sorted(pyfiglet.FigletFont.getFonts())

    def list_recommended_fonts(self) -> list[str]:
        """List recommended fonts for Genesis.

        Returns:
            List of recommended font names.
        """
        available = set(self.list_fonts())
        return [f for f in self.RECOMMENDED_FONTS if f in available]

    def validate_font(self, font: str) -> bool:
        """Check if a font is available.

        Args:
            font: Font name to validate.

        Returns:
            True if font exists, False otherwise.
        """
        return font in self.list_fonts()

    def preview_fonts(self, text: str = "GENESIS") -> dict[str, str]:
        """Preview text in recommended fonts.

        Args:
            text: Text to preview.

        Returns:
            Dictionary mapping font name to rendered text.
        """
        previews = {}
        for font in self.list_recommended_fonts():
            try:
                previews[font] = self.render(text, font=font)
            except Exception:
                continue
        return previews
