from flask import Flask, jsonify, request, render_template, make_response 
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from hitode_view import hitode
from hitode_control.user_mgmt import User

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'queenoyster_server'

app.register_blueprint(hitode.hitode_matching, url_prefix='/hitode')
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = 'strong'

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

# 미 로그인자 활동 신청시, 메세지 뿌려주기
@login_manager.unauthorized_handler
def unauthorized():
    return make_response(jsonify(success = False), 401)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080', debug=True)