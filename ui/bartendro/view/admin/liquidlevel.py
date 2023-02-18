from bartendro import app, db
from flask import Flask, request, render_template
from flask_login import login_required


@app.route('/admin/liquidlevel')
@login_required
def admin_liquidlevel():
    driver = app.driver
    count = driver.count()
    thresholds = []
    for disp in range(count):
        low, out = driver.get_liquid_level_thresholds(disp)
        thresholds.append((low, out))

    return render_template("admin/liquidlevel",
                           options=app.options,
                           count=count,
                           title="Liquid level calibration",
                           thresholds=thresholds)
