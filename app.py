from flask import Flask,render_template,url_for,request
app=Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')

def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt',mode='a') as database:
        email=data['email']
        subject=data['subject']
        message=data['message']
        database.write(f'\n {email},{subject},{message}')

@app.route('/submit_form',methods=['GET','POST'])
def submit_form():
    if request.method=='POST':
        data=request.form.to_dict()
        write_to_file(data)
        return 'Form Submitted'
    else:
        return 'Something went wrong' 
if __name__=='__main__':
    app.run(debug=True)
