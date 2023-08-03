from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(75, 75, 75)
    pdf.cell(w=180, h=12, txt=row["Topic"], 
            align="L", ln=0)
    #pdf.cell(w=100, h=12, txt=f"{i+1}", align="L", ln=1)
    pdf.line(x1=10, y1=21, x2=200, y2=21)
    
    #set the footer
    pdf.ln(277)
    pdf.set_font(family="Times", style="I", size=12)
    pdf.cell(w=0, h=10, txt=f"{row['Topic']} - 1", align="R")
    
    for i in range(row["Pages"] - 1):
        pdf.add_page()
        #set the footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=12)
        pdf.set_text_color(75, 75, 75)
        pdf.cell(w=0, h=10, txt=f"{row['Topic']} - {i+2}", align="R")
        

pdf.output("output2.pdf")