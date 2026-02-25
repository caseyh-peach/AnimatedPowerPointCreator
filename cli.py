"""Command-line interface for AnimatedPowerPointCreator."""

from pathlib import Path

import click

from animated_pptx_creator import AnimatedPowerPointCreator


@click.command()
@click.option("--template", default=None, help="Path to a .pptx template file.")
@click.option(
    "--output",
    "-o",
    default="output.pptx",
    help="Output file path (default: output.pptx).",
)
@click.option(
    "--transition",
    "-t",
    default="fade",
    help="Default transition between slides.",
)
@click.option(
    "--animation",
    "-a",
    default="fade_in",
    help="Default entrance animation for slide content.",
)
@click.option("--title", default="My Presentation", help="Title slide text.")
def create(template, output, transition, animation, title):
    """Generate an animated PowerPoint presentation."""
    creator = AnimatedPowerPointCreator(template=template)

    creator.add_slide(
        layout="title",
        title=title,
        subtitle="Created with AnimatedPowerPointCreator",
        animation=animation,
    )

    creator.set_transition(0, transition)

    path = creator.save(output)
    click.echo(f"Presentation saved to {path}")


if __name__ == "__main__":
    create()
