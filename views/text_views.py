from flask import Blueprint, render_template

text_views = Blueprint('text', __name__)

@text_views.route('/privacy_policy/')
def privacy_policy():
    return render_template('text/privacy_policy.html')