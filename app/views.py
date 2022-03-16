"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
from app import app, db
from flask import render_template, request, redirect, url_for, flash,send_from_directory
from werkzeug.utils import secure_filename
from .forms import Newproperty
from .models import Properties
import os

###h
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route('/property',methods=['POST','GET'])
def property_():
    """For displaying the form to add a new property"""
    form=Newproperty()
    if request.method == 'POST' :
        if form.validate_on_submit():
            image = form.image.data 
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            property_=Properties(title=form.title.data, num_of_bedrooms=form.nobed.data,num_of_bathrooms=form.nobath.data,ptype=form.ptype.data,location=form.location.data,price=form.price.data,description=form.description.data,photo=filename)
            db.session.add(property_)
            db.session.commit()

            flash('Property Saved', 'success')
            return redirect(url_for('properties'))
        else:
            flash_errors(form)
    return render_template('NewProperty.html',form=form) 


@app.route('/properties')
def properties():
    return render_template('properties.html', properties = Properties.query.all() )


@app.route('/property/<propertyid>')
def get_property(propertyid):
    property_id = Properties.query.filter_by(id=propertyid).first()
    return render_template('property.html', property=property_id)


@app.route('/uploads/<filename>')
def get_image(filename):
    rootdir = os.getcwd()
    return send_from_directory(os.path.join(rootdir,app.config['UPLOAD_FOLDER']), filename)

###
# The functions below should be applicable to all Flask apps.
###

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % ( getattr(form, field).label.text,error), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
