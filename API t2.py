# Using flask to make an api

#from flask import Flask, jsonify, request


from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        return render_template('data.html',form_data = form_data)


app.run(host='localhost', port=5000)




'''

@app.route('/', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
  
        data = "hello world"

        return jsonify({'data': num**2},{'data': data})

'''  
'''

@app.route('/home/<int:num>', methods = ['GET'])
def disp(num):
  
    return jsonify({'data': num**2})
  
'''
'''
# driver function
if __name__ == '__main__':
  
    app.run(debug = True)

'''    