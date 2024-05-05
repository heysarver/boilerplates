from . import pages_blueprint

@pages_blueprint.route('/')
def home():
    return render_template('home.html')
