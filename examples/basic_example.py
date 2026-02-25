"""Basic example: create a short animated presentation."""

from animated_pptx_creator import AnimatedPowerPointCreator


def main():
    creator = AnimatedPowerPointCreator()

    creator.add_slide(
        layout="title",
        title="Quarterly Review",
        subtitle="Q4 2025",
        animation="fade_in",
    )

    creator.add_slide(
        layout="content",
        title="Highlights",
        bullets=[
            "Revenue up 15 %",
            "Customer satisfaction at 92 %",
            "Launched 3 new products",
        ],
        animation="fly_in_left",
        stagger_delay=0.4,
    )

    creator.add_slide(
        layout="content",
        title="Next Steps",
        bullets=[
            "Expand into APAC market",
            "Hire 20 engineers",
            "Ship v2.0 by March",
        ],
        animation="zoom_in",
        stagger_delay=0.3,
    )

    for i in range(1, 3):
        creator.set_transition(i, "push", 0.5)

    creator.save("quarterly_review.pptx")
    print("Done — open quarterly_review.pptx in PowerPoint.")


if __name__ == "__main__":
    main()
