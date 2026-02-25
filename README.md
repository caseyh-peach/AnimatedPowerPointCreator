# AnimatedPowerPointCreator

A Python tool for creating PowerPoint presentations with rich animations, transitions, and dynamic content programmatically.

## Features

- **Slide Transitions** — Apply fade, push, wipe, and other transition effects between slides
- **Element Animations** — Animate text, shapes, and images with entrance, emphasis, and exit effects
- **Timing Control** — Fine-tune animation delays, durations, and sequencing
- **Template Support** — Start from built-in templates or your own `.pptx` files
- **Batch Generation** — Generate multiple animated presentations from data sources
- **CLI & API** — Use from the command line or import as a Python library

## Quick Start

### Installation

```bash
pip install -r requirements.txt
```

### Basic Usage

```python
from animated_pptx_creator import AnimatedPowerPointCreator

creator = AnimatedPowerPointCreator()

# Add a title slide with a fade-in animation
creator.add_slide(
    layout="title",
    title="Welcome",
    subtitle="Created with AnimatedPowerPointCreator",
    animation="fade_in",
)

# Add a content slide with bullet animations
creator.add_slide(
    layout="content",
    title="Key Points",
    bullets=["First point", "Second point", "Third point"],
    animation="fly_in_left",
    stagger_delay=0.3,
)

# Add a transition between slides
creator.set_transition(slide_index=1, transition="push", duration=0.5)

# Save the presentation
creator.save("my_presentation.pptx")
```

### Command Line

```bash
python animated_pptx_creator.py --template default --output presentation.pptx
```

## Project Structure

```
AnimatedPowerPointCreator/
├── animated_pptx_creator.py   # Main library module
├── cli.py                     # Command-line interface
├── templates/                 # Built-in slide templates
├── examples/                  # Example scripts
├── requirements.txt           # Python dependencies
└── README.md
```

## Requirements

- Python 3.9+
- python-pptx

## License

MIT
