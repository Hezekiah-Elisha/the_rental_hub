from flask import Blueprint, render_template, flash
from models.model_function import get_user_details, roles_edit, get_rentor_info, add_rentor_info
from models.BuildingForm import RoleForm, RentorCompleteForm

user = Blueprint('user', __name__)


@user.route('/user/<int:user_id>', methods=['GET', 'POST'])
def user_profile(user_id):
    user = get_user_details(user_id)

    if user is None:
        return render_template('404.html')

    form = RoleForm()
    form2 = RentorCompleteForm()

    if form.validate_on_submit():
        role = form.role.data

        info = roles_edit(user_id, role)
        if info is None:
            flash('Role Not Updated', 'danger')
        else:
            flash('Role updated', 'success')
    
    if form2.validate_on_submit():
        id_number = form2.id_number.data
        location = form2.location.data
        
        rentor_info = add_rentor_info(user_id, id_number, location)

        if rentor_info is None:
            flash('Rentor Not Updated', 'danger')
        else:
            flash('Rentor info updated', 'success')
    # return redirect('/user/{}'.format(user_id))
    return render_template('user.html', user=user, form=form, info=get_rentor_info, form2=form2)
