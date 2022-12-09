from flask import Blueprint, render_template, flash
from models.model_function import get_user_details, roles_edit
from models.BuildingForm import RoleForm

user = Blueprint('user', __name__)

@user.route('/user/<int:user_id>', methods=['GET', 'POST'])
def user_profile(user_id):
    user = get_user_details(user_id)

    if user is None:
        return render_template('404.html')
    
    form = RoleForm()

    if form.validate_on_submit():
        role = form.role.data

        info = roles_edit(user_id, role)
        if info == None:
            flash('Role Not Updated', 'danger')
        else:
            flash('Role updated', 'success')
    # return redirect('/user/{}'.format(user_id))
    return render_template('user.html', user=user, form=form)

