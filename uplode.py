import os,json
from flask import Flask, render_template, request
from werkzeug import secure_filename
from database import connection
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploaded_files'
@app.route('/')
def registeration_form():
   #return render_template('uploadfile.html')
   return render_template('register.html')


@app.route('/register', methods = ['POST'])
def register():
	userName = request.form["user"]
	userpass = request.form["password"]
	print userName,userpass
	try:
		c, conn = connection()
		query="""insert register(userName,userPass) values (%s,%s)"""
		c.execute(query,(userName,userpass))
		conn.commit()
		c.close()
		conn.close()
		return render_template('login.html')
	except Exception as e:
		print "inside exe"
		#return(str(e))
	#return render_template('login.html')

@app.route('/login', methods = ['POST'])
def login():
	userName = request.form["user"]
	userpass = request.form["password"]
	print userName,userpass
	try:
		c, conn = connection()
		sqlquery = ("select * from register")
		c.execute(sqlquery)
		rows = c.fetchall()

		print rows
		print type(rows)
		#res_list = [x[0] for x in rows]#
		for i in rows:
			print i[1],i[2]
			if userName==i[1] and userpass==i[2]:
				print "valid user"
				return render_template('uploadfile.html')
			else:
				valid=1
		if valid==1:
			return "invalid user"

	except Exception as e:
		print "inside exe getAllFiles"
		print (str(e))
	#return render_template('uploadfile.html')

@app.route('/uploader', methods = ['POST'])
def upload_file1():
   if request.method == 'POST':
    	f = request.files['file']
    	nameOfFile = str(f.filename)
      	print f
      	try:
        	c, conn = connection()
        	f.save(os.path.join(app.config['UPLOAD_FOLDER'], nameOfFile))
        	# sqlquery = ("select * from filestore2")
        	# c.execute(sqlquery)
        	# rows = c.fetchall()
        	# print rows
        	query="""insert filestore2(f_name) values (%s)"""
        	c.execute(query,[nameOfFile])
        	conn.commit()
        	c.close()
        	conn.close()
        	result = getAllFiles()
        	return render_template('uploaded.html',data=result)

        except Exception as e:
        	print "inside exe"
        	return(str(e))

def getAllFiles():
    print "inside get_All_Files"
    allFiles = []
    try:
        c, conn = connection()
        sqlquery = ("select f_name from filestore2")
        c.execute(sqlquery)
        rows = c.fetchall()
        
        res_list = [x[0] for x in rows]
        
        for name in res_list:
         # if data[2]==id: #  
           file_name1 = {'name':name}
           #file_name1 = {'date':date} #
           allFiles.append(file_name1)
        
        print allFiles 
        conn.commit()
        c.close()
        conn.close()
        return (allFiles)
    except Exception as e:
        print "inside exe getAllFiles"
        print (str(e))
        return(str(e))
      	
if __name__ == '__main__':
   app.run(debug = True)