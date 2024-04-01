from flask import (
    Blueprint,
    render_template,
    request,
    make_response,
    session,
    flash,
    redirect,
    url_for,
    current_app,
    send_from_directory,
)
from flask_login import current_user, login_required
from apps.detector.models import UserImage, Favorite
from apps.crud.models import User
from apps.app import db
from apps.detector.forms import UploadImageForm, DeleteForm
from apps.crud.forms import UpdateForm
from flask_paginate import Pagination, get_page_args
import uuid
from pathlib import Path

dt = Blueprint("detector", __name__, template_folder="templates")


@dt.route("/", methods=["GET"])
def index():
    images = UserImage.query.order_by(UserImage.id.desc()).all()
    originals = (
        UserImage.query.order_by(UserImage.id.desc())
        .filter(UserImage.sexual == 4)
        .all()
    )

    return render_template("detector/index.html", images=images, originals=originals)


@dt.route("/images/<path:filename>")
def image_file(filename):
    return send_from_directory(current_app.config["UPLOAD_FOLDER"], filename)


@dt.route("/upload", methods=["GET", "POST"])
@login_required
def upload_images():
    form = UploadImageForm()

    if form.validate_on_submit():
        file = form.image.data
        ext = Path(file.filename).suffix
        image_uuid_file_name = str(uuid.uuid4()) + ext

        image_path = Path(current_app.config["UPLOAD_FOLDER"], image_uuid_file_name)
        file.save(image_path)

        user_image = UserImage(
            user_id=current_user.id,
            image_path=image_uuid_file_name,
            image_name=form.title.data,
            explain=form.explain.data,
            category=form.category.data,
            size=form.size.data,
            condition=form.condition.data,
            type=form.type.data,
            price=form.price.data,
            send=form.send.data,
            sexual=form.sexual.data,
        )

        db.session.add(user_image)
        db.session.commit()

        return redirect(url_for("detector.index"))
    return render_template("detector/toukou.html", form=form)




@dt.route("/mypage")
@login_required
def mypage():
    users = User.query.filter_by(id=current_user.id).first()
    user_images = UserImage.query.filter_by(user_id=current_user.id).order_by(UserImage.created_at.desc()).all()

    delete_form = DeleteForm()

    postNum = UserImage.query.filter_by(user_id=current_user.id).count()
    badge = False

    original = UserImage.query.filter_by(user_id=current_user.id, sexual=4).count()
    badge_o = False

    if postNum >= 5:
        badge = True
    else:
        badge = False

    if original >= 5:
        badge_o = True
    else:
        badge_o = False

    return render_template(
        "detector/mypage.html",
        users=users,
        user_images=user_images,
        delete_form=delete_form,
        badge=badge,
        badge_o=badge_o,
        postNum=postNum,
    )


@dt.route("/images/delete/<string:image_id>", methods=["POST"])
@login_required
def delete_image(image_id):
    try:
        delete = UserImage.query.filter(UserImage.id == image_id).first()
        db.session.delete(delete)
        db.session.commit()

    except:
        db.session.rollback()

    return redirect(url_for("detector.mypage"))


@dt.route("/editprofile/<int:id>", methods=["POST", "GET"])
@login_required
def editprofile(id):
    user = User.query.filter_by(id=id).first()
    updateform = UpdateForm()

    if request.method == "POST":
        if updateform.validate_on_submit():
            file = updateform.image.data
            ext = Path(file.filename).suffix
            image_uuid_file_name = str(uuid.uuid4()) + ext

            image_path = Path(current_app.config["UPLOAD_FOLDER"], image_uuid_file_name)
            file.save(image_path)

            user.icon_path = (image_uuid_file_name,)
            user.username = (updateform.username.data,)
            user.profile = (updateform.explain.data,)
            user.address = (updateform.address.data,)
            user.phone = updateform.phone.data

            db.session.commit()
            return redirect(url_for("detector.mypage"))

    return render_template(
        "detector/editprofile.html", user=user, updateform=updateform
    )


@dt.route("/notices")
def notices():
    return render_template("detector/notice.html")


@dt.route("/todo")
def todo():
    return render_template("detector/todo.html")


@dt.route("/article")
def article():
    return render_template("detector/article.html")
