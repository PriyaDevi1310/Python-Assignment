import jinja2
import os
from jinja2 import Template
from fpdf import FPDF
# save FPDF() class into 
# a variable pdf
pdf = FPDF()   
   
# Add a page
pdf.add_page()
   
# set style and size of font 
# that you want in the pdf
pdf.set_font("Arial", size = 15)
  

   
latex_jinja_env = jinja2.Environment(
    block_start_string = '\BLOCK{',
    block_end_string = '}',
    variable_start_string = '\VAR{',
    variable_end_string = '}',
    comment_start_string = '\#{',
    comment_end_string = '}',
    line_statement_prefix = '%%',
    line_comment_prefix = '%#',
    trim_blocks = True,
    autoescape = False,
    loader = jinja2.FileSystemLoader(os.path.abspath('.'))
)
outfile = 'imagesearch1.tex'
template = latex_jinja_env.get_template('jinja-test.tex')
render=template.render(section1='Long Form', section2='Short Form')
f = open(outfile, 'w')
f.write(render)
f.close()


# open the text file in read mode
f = open("imagesearch1.tex", "r")
  
# insert the texts in pdf
for x in f:
    pdf.cell(200, 10, txt = x, ln = 1, align = 'C')


pdf.output("mygfg.pdf")   
