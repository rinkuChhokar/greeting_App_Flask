from flask import Flask, render_template, request,flash   
    
app=Flask(__name__,template_folder='templates')
app.secret_key = 'super secret key'

@app.route("/")
def index():
    flash("What's your Name?")
    return render_template("index.html")


@app.route("/greet",methods=["POST","GET"])
def greet():
    if request.form['name_input']=="":
        flash("No input, Please enter your name first")

    else:

        flash("Hi "+str(request.form['name_input'])+", great to see you!")
        request.form['name_input']
       
   
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)    
