lo=sorted(df["location"].unique())
    return render_template('index1.html',lo=lo)