from flask import Blueprint, render_template
from functions import login_required

solving_tests_bp = Blueprint('solving_tests', __name__)


@solving_tests_bp.route('/reasoning/', methods=['GET', 'POST'], endpoint='reasoning')
@login_required
def reasoning():
    return render_template('reasoning.html')


@solving_tests_bp.route('/compare_items', methods=['GET', 'POST'], endpoint='compare_items')
@login_required
def compare_items():
    return render_template('compare_items.html')
