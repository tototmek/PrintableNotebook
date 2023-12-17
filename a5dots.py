from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A5
from reportlab.lib.units import mm
from reportlab.lib.colors import Color
from math import floor


def create_pdf(filename, pagesize, dot_radius, margin, stride):
    c = canvas.Canvas(filename, pagesize=pagesize)
    color = Color(0, 0, 0, 0.06)
    c.setFillColor(color)

    count_x = floor((pagesize[0] - 2 * margin[0]) / stride[0])
    count_y = floor((pagesize[1] - 2 * margin[1]) / stride[1])
    margin_x = 0.5 * (pagesize[0] - (count_x * stride[0]))
    margin_y = 0.5 * (pagesize[1] - (count_y * stride[1]))

    for x in range(count_x + 1):
        for y in range(count_y + 1):
            c.circle(
                x * stride[0] + margin_x,
                y * stride[1] + margin_y,
                dot_radius,
                stroke=0,
                fill=1,
            )
    c.save()


if __name__ == "__main__":
    create_pdf(
        "a5dots.pdf",
        pagesize=A5,
        dot_radius=0.5 * mm,
        margin=(20 * mm, 25 * mm),
        stride=(5 * mm, 5 * mm),
    )
