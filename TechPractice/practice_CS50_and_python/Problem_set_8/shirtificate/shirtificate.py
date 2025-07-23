from fpdf import FPDF

class pdf(FPDF):
    def __init__(self,name, Oname):
        self.file = FPDF()
        self.file.add_page()
        self.file.set_font("helvetica", "B", 50)
        self.file.cell(0, 60, 'CS50 Shirtificate', new_x='LMARGIN', new_y='NEXT', align='C')
        self.file.image("shirtificate.png", w=self.file.epw)
        self.file.set_font_size(30)
        self.file.set_text_color(255,255,255)
        self.file.text(x=47, y=140, txt=f"{name} took CS50")
        self.file.output(Oname)

def main():
    UName = input("Name: ")
    file = pdf(UName, "shirtificate.pdf")

if __name__ == "__main__":
    main()