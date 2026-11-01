from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(
    report_data,
    output_file
):

    doc = SimpleDocTemplate(
        output_file
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "AI Startup Co-Founder Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 20)
    )

    for section, text in report_data.items():

        content.append(
            Paragraph(
                section.replace("_", " ").title(),
                styles["Heading2"]
            )
        )

        content.append(
            Paragraph(
                str(text),
                styles["BodyText"]
            )
        )

        content.append(
            Spacer(1, 10)
        )

    doc.build(content)