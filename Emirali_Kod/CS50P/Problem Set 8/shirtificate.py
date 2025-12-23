from fpdf import FPDF

#create FPDF object
#Layout ("P", "L")
#Unit("mm", "cm", "in")
#format ("A3", "A4" (default), "A5", "Letter", "Legal", (100,150))

class PDF(FPDF):
    def header(self):
        pdf.set_font("Times", "", 30)
        text = "CS50 Shirtificate"
        text_width = self.get_string_width(text)
        self.set_xy((210 - text_width) / 2, 10)
        self.cell(text_width, 10, text, border=0, align="C")

        image_width = 200
        image_height = 180
        x = (210 - image_width) / 2
        y = 25
        self.image("shirtificate.png", x=x, y=y, w=image_width, h=image_height)


        pdf.set_font("Times", "", 35)
        pdf.set_text_color("#FFFFFF")
        name = input("Name: ")
        text2 = f"{name} took CS50"
        text2_width = self.get_string_width(text)
        self.set_xy((210 - text2_width) / 2, 100)
        self.cell(text2_width, 10, text2, border=0, align="C")


pdf = PDF(orientation="portrait", unit="mm", format="A4")
# Add a page
pdf.add_page()
pdf.output("pdf_1.pdf")

