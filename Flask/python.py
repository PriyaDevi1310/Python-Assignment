\
from flask import Flask, render_template,redirect, url_for, request
import requests
import jinja2
import os
from jinja2 import Template
from fpdf import FPDF

app = Flask(__name__)

@app.route('/')
def display():
		return render_template('imagesearch.html')
@app.route('/latexview')
def latexview():
		return render_template('latexview.html')		
	
# @app.route('/search')
# def search():
# 		for i in range(0,9):
# 			url = request.form['imageurl'+str(i)]
# 			filename = url.split('/')[-1]
# 			filename1 = filename.split('?')[0]+'.jpg'
# 			r = requests.get(url, allow_redirects=True)
# 			open(filename1, 'wb').write(r.content)

# 		return render_template('imagesearch.html')    

@app.route('/imagepost',methods = ['POST', 'GET'])
def imagepost():

	 if request.method == 'POST':
				 searchtype = request.form['type']
				 image=''
				 width=''
				 height=''
		 #return redirect(url_for('success',name = user))
				 for i in range(0,10):
					 url = request.form['imageurl'+str(i)]
					 filename = url.split('/')[-1]
					 filename1 = filename.split('?')[0]+'.jpg'
					 r = requests.get(url, allow_redirects=True)
					 open(filename1, 'wb').write(r.content)
					 image=filename1+','+image
					 width=request.form['width'+str(i)]+','+width
					 height=request.form['height'+str(i)]+','+height
#--------------------------------------------------
				 imagearray=image.split(',')
				 widtharray=width.split(',')
				 heightarray=height.split(',')
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

				 outfile = 'static/imagesearch1.tex'
				 template = latex_jinja_env.get_template('jinja-test.tex')
				 render=template.render(header=searchtype,image=imagearray,width=widtharray,height=heightarray)
				 f = open(outfile, 'w')
				 f.write(render)
				 f.close()


# open the text file in read mode
				 f = open("imagesearch1.tex", "r")
	
# insert the texts in pdf
				 for x in f:
					 pdf.cell(200, 10, txt = x, ln = 1, align = 'C')


				 pdf.output("mygfg.pdf")
				 
				 return render_template('latexview.html')
		
		

		#return render_template('imagesearch.html')   

if __name__=='__main__':
		app.run()