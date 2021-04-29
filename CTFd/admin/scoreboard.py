from flask import render_template

from CTFd.admin import admin
from CTFd.scoreboard import get_standings
from CTFd.utils.decorators import admins_only


@admin.route("/admin/scoreboard")
@admins_only
def scoreboard_listing():
    standings = get_standings(admin=True)
    return render_template("admin/scoreboard.html", standings=standings)


@admin.route("/admin/scoreboard/CSU")
@admins_only
def scoreboard_listing_csu():
    standings = get_standings(admin=True, isCSU=True)
    return render_template("admin/scoreboard.html", standings=standings)
