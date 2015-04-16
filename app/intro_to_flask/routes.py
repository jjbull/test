from intro_to_flask import app
from flask import Flask, render_template, request, flash, session,redirect,url_for
from forms import ContactForm,SignupForm, SigninForm
from models import db,User

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()
 
  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('contact.html', form=form)
    else:
      return 'Form posted.'
 
  elif request.method == 'GET':
    return render_template('contact.html', form=form)
  
  
@app.route('/signup', methods=['GET', 'POST'])
def signup():
  form = SignupForm()
   
  if request.method == 'POST':
    if form.validate() == False:
      return render_template('signup.html', form=form)
    else:
      newuser = User(form.firstname.data, form.lastname.data, form.email.data, form.password.data)
      db.session.add(newuser)
      db.session.commit()
       
      session['email'] = newuser.email
      session['name']= newuser.firstname
      return redirect(url_for('profile'))
   
  elif request.method == 'GET':
    return render_template('signup.html', form=form)
  
  
@app.route('/profile/')
def profile():
 
  if 'email' not in session:
    return redirect(url_for('signin'))
 
  user = User.query.filter_by(email = session['email']).first()
 
  if user is None:
    return redirect(url_for('signin'))
  else:
    return render_template('profile.html')
  
@app.route('/signin', methods=['GET', 'POST'])
def signin():
  form = SigninForm()
   
  if request.method == 'POST':
    if form.validate() == False:
      return render_template('signin.html', form=form)
    else:
      session['email'] = form.email.data
      return redirect(url_for('profile'))
                 
  elif request.method == 'GET':
    return render_template('signin.html', form=form)
  
@app.route('/signout')
def signout():
 
  if 'email' not in session:
    return redirect(url_for('signin'))
     
  session.pop('email', None)
  return redirect(url_for('home'))

@app.route('/test')
def test():
    return """<http><body><form action="buy" method="POST">
<script
    src="https://checkout.stripe.com/checkout.js" class="stripe-button"
    data-key="pk_test_w3qNBkDR8A4jkKejBmsMdH34"
    data-amount="999"
    data-name="jeffknupp.com"
    data-description="Writing Idiomatic Python 3 PDF ($9.99)">
</script>
<input type="hidden" name="product_id" value="2" />
</form>
</body>
</html>
"""