import sqlite3, json
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_login import LoginManager
from flask_session import Session
from tempfile import mkdtemp
from ex import login_required

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['SECRET_KEY'] = 'reds209ndsldssdsljdsldsdsljdsldksdksdsdfsfsfsfis'


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
db_all = sqlite3.connect('dba.db', check_same_thread=False)
db = db_all.cursor()


@app.route("/")
@app.route("/login", methods=['GET', 'POST'])
def login():
    session.clear()

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        row = db.execute("SELECT * FROM user WHERE username = "+"\'"+username+"\'")

        result = [item for t in row for item in t]
        if result[1] != username or result[2] != password:
            return redirect(url_for('login'))
        session["user_id"] = result[0]
        return redirect(url_for('sales'))
    else:
        return render_template('login.html')


final_profit = 0
final_price = 0


@login_manager.user_loader
def load_user(user_id):
    return session["user_id"]


@app.route("/sales", methods=["POST", "GET"])
@login_required
def sales():
    if request.method == "POST":
        global final_profit, final_price
        final_quantity = 0
        medicine = request.form.get("medicine")
        s = db.execute("SELECT quantity FROM inventory WHERE medicine = " + "\'" + medicine + "\'" + " AND user_id = " + str(session["user_id"]))
        quantity = s.fetchall()
        sd = db.execute("SELECT drugstore_name FROM inventory WHERE medicine = " + "\'" + medicine + "\'" + " AND user_id = " + str(session["user_id"]) + " AND no_of_goods = " + request.form.get("no_of_goods"))
        sdd = sd.fetchall()
        drug = ""
        for r in sdd:
            for row in r:
                drug = row
        query_input = db.execute("SELECT medicine FROM inventory WHERE user_id = " + str(session["user_id"]) + " AND medicine like " + "\'%" + medicine + "%\'")
        m = query_input.fetchall()

        l = []
        for r in m:
            for item in r:
                if item not in l:
                    l.append(item)

        for r in quantity:
            for row in r:
                final_quantity += row
        qq = db.execute("SELECT * FROM inventory WHERE medicine = " + "\'" + medicine + "\'" + " AND user_id = " + str(session["user_id"]) + " AND no_of_goods = " + request.form.get("no_of_goods"))
        ql = []
        qw = qq.fetchall()
        for e in qw:
            for y in e:
                ql.append(y)
        if not final_quantity >= int(request.form.get("quantity")):
            flash("you do not have enough quantity for this medicine", 'danger')
            """
        g = db.execute("SELECT sell_price  FROM inventory WHERE medicine =  " + "\'" + medicine + "\'" + " AND user_id = " + str(session["user_id"]) + " AND no_of_goods = " + request.form.get("no_of_goods"))
        gg = g.fetchall()
        price = []
        for d in gg:
            for t in d:
                price.append(t)
                """
        #expire_query = db.execute("SELECT expire_date FROM inventory WHERE medicine=" + "\'" + medicine + "\'" + " AND user_id = " + str(session["user_id"]) + " AND no_of_goods = " + request.form.get("no_of_goods"))
        #expire_query = e.fetchall()
        """
        expire_query = []
        for i in ee:
            for eq in i:
                expire_query.append(str(eq))
                """
        bb = db.execute("SELECT no_of_goods FROM inventory WHERE medicine = " + "\'" + medicine + "\'" + " AND user_id = " + str(session["user_id"]))
        nn = bb.fetchall()
        no_of_goods = []
        for f in nn:
            for t in f:
                no_of_goods.append(t)

        p = db.execute("SELECT cost_price - sell_price FROM inventory WHERE medicine = " + "\'" + medicine + "\'" + " AND user_id = " + str(session["user_id"]) + " AND no_of_goods = " + request.form.get("no_of_goods"))
        pr = p.fetchall()
        profit = ''
        for pp in pr:
            for f in pp:
                profit = -f
        c = db.execute("SELECT cost_price FROM inventory WHERE medicine = " + "\'" + medicine + "\'" + " AND user_id = " + str(session["user_id"]) + " AND no_of_goods = " + request.form.get("no_of_goods"))
        co = c.fetchall()
        cost_price = ''
        for cc in co:
            for f in cc:
                cost_price = f
        s = db.execute("SELECT sell_price FROM inventory WHERE medicine = " + "\'" + medicine + "\'" + " AND user_id = " + str(session["user_id"]) + " AND no_of_goods = " + request.form.get("no_of_goods"))
        se = s.fetchall()
        sell_price = ''
        for ss in se:
            for f in ss:
                sell_price = f


        sell = []
        for ss in se:
            for f in ss:
                sell.append(str(f))
        print(sell_price)
        pri = int("".join(sell)) * int(request.form.get("quantity"))
        col = int(request.form.get("quantity"))
        flag = 0
        for r in quantity:
            for row in r:
                print(row)
                if flag == 0:
                    if row > int(col):
                        o = db.execute("UPDATE inventory SET quantity = " + "\'" + str(row - col) + "\' " + " WHERE medicine =  " + "\'" + medicine + "\'" + " AND user_id = " + str(session["user_id"]) + " AND no_of_goods = " + request.form.get("no_of_goods"))
                        db_all.commit()
                        print(o.fetchall())
                        break
                    elif row == int(col):
                        db.execute("DELETE FROM inventory WHERE medicine = " + "\'" + request.form.get("medicine") + "\'" + " AND user_id = " + str(session["user_id"]) + " AND no_of_goods = " + request.form.get("no_of_goods"))
                        db_all.commit()
                        db.execute("DELETE FROM expire WHERE medicine = " + "\'" + request.form.get("medicine") + "\'" + " AND user_id = " + str(session["user_id"]) + " AND no_of_goods = " + str(no_of_goods))
                        db_all.commit()
                        break
                    else:
                        db.execute("DELETE FROM inventory WHERE medicine = " + "\'" + request.form.get("medicine") + "\'" + " AND user_id = " + str(session["user_id"]) + " AND no_of_goods = " + request.form.get("no_of_goods"))
                        db_all.commit()

                        db.execute("DELETE FROM expire WHERE medicine = " + "\'" + request.form.get("medicine") + "\'" + " AND user_id = " + str(session["user_id"]) + " AND no_of_goods = " + request.form.get("no_of_goods"))
                        db_all.commit()
                        col = int(col) - row
                        flag = 1
                else:
                    b = db.execute("SELECT no_of_goods FROM inventory WHERE medicine = " + "\'" + medicine + "\'" + " AND user_id = " + str(session["user_id"]) + " AND quantity = " + str(row))
                    db_all.commit()
                    n = b.fetchall()
                    no_of_goods = []
                    for f in n:
                        for t in f:
                            no_of_goods.append(t)
                    if row > int(col):

                        db.execute("UPDATE inventory SET quantity = " + "\'" + str(row - int(col)) + "\' " + " WHERE medicine =  " + "\'" + medicine + "\'" + " AND user_id = " + str(session["user_id"]) + " AND no_of_goods = " + request.form.get("no_of_goods"))
                        db_all.commit()
                        break
                    elif row == int(col):
                        db.execute("DELETE FROM inventory WHERE medicine = " + "\'" + request.form.get("medicine") + "\'" + " AND user_id = " + str(session["user_id"]) + " AND no_of_goods = " + str(no_of_goods))
                        db_all.commit()
                        db.execute("DELETE FROM expire WHERE medicine = " + "\'" + request.form.get("medicine") + "\'" + " AND user_id = " + str(session["user_id"]) + " AND no_of_goods = " + str(no_of_goods))
                        db_all.commit()
                        break
                    else:
                        db.execute("DELETE FROM inventory WHERE medicine = " + "\'" + request.form.get("medicine") + "\'" + " AND user_id = " + str(session["user_id"]) + " AND no_of_goods = " + str(no_of_goods))
                        db_all.commit()
                        db.execute("DELETE FROM expire WHERE medicine = " + "\'" + request.form.get("medicine") + "\'" + " AND user_id = " + str(session["user_id"]) + " AND no_of_goods = " + str(no_of_goods))
                        db_all.commit()
                        col = int(col) - row
                        flag = 1

        final_profit = final_profit + int(profit)
        final_price = final_price + pri
        if request.form.get("discount"):
            final_profit = final_profit / final_price
            final_price = final_price - request.form.get("discount")
            final_profit = final_profit * final_price

        db.execute("INSERT INTO invoice (user_id,medicine, quantity, price, final_price, cost_price, sell_price, expire_date, profit, drugstore_name, no_of_goods, invoice_no) VALUES (" + "\'" + str(session["user_id"]) + "\'" + "," + "\'" + str(medicine) + "\'" + "," + "\'" + request.form.get("quantity") + "\'" + "," + "\'" + str(pri) + "\'" + "," + "\'" + str(final_price) + "\'" + "," + "\'" + str(cost_price) + "\'" + "," + "\'" + str(sell_price) + "\'" + "," + "\'" + str(ql[6]) + "\'" + "," + "\'" + str(profit) + "\'" + "," + "\'" + str(drug) + "\'" + "," + "\'" + str(request.form.get("no_of_goods")) + "\'" + "," + "\'" + str(request.form.get("invoice_no")) + "\')")
        db_all.commit()
        invoice_query = db.execute("SELECT * FROM invoice WHERE user_id = " + "\'" + str(session["user_id"]) + "\'")

        q = invoice_query.fetchall()
        db.execute("INSERT INTO invoices(user_id, medicine, quantity, price, invoice_no) VALUES (" + "\'" + str(session["user_id"]) + "\'" + "," + "\'" + str(medicine) + "\'" + "," + "\'" + request.form.get("quantity") + "\'" + "," + "\'" + str(pri) + "\'" + "," + "\'" + request.form.get("invoice_no") + "\')")
        db_all.commit()
        n = db.execute("SELECT no_of_goods FROM inventory WHERE medicine = " + "\'" + medicine + "\'" + " AND user_id = " + str(session["user_id"]))
        no = n.fetchall()
        l2 = []
        for i in no:
            for e in i:
                if e not in l2:
                    l2.append(e)
        return redirect(url_for("sales_table"))
        #return render_template('sales.html', l=l, q=q, l2=l2, final_price=final_price,
                               #final_profit=final_profit)
    else:
        return render_template("sales.html")


@app.route("/sales/table", methods=["GET", "POST"])
@login_required
def sales_table():
    if request.method == "GET":
        q = db.execute("SELECT * FROM invoice WHERE user_id = "+"\'"+str(session["user_id"])+"\'")
        query = q.fetchall()
        f = db.execute("SELECT final_price FROM invoice WHERE user_id = "+"\'"+str(session["user_id"])+"\'")
        ff = f.fetchall()
        final = 0
        for row in ff:
            for r in row:
                final = r
        return render_template("sales.html", query=query, final=final)
    if request.method == "POST":

        return redirect(url_for("invoice"))


@app.route("/invoice", methods=["GET", "POST"])
@login_required
def invoice():
    if request.method == "POST":
        q = db.execute("SELECT * FROM invoice WHERE user_id = " + "\'" + str(session["user_id"]) + "\'")
        query = q.fetchall()

        db.execute("DELETE FROM invoice WHERE user_id = " + "\'" + str(session["user_id"]) + "\'")
        db_all.commit()
        return render_template("invoice.html", query=query)
    if request.method == "GET":
        return render_template("invoice.html")


@app.route("/cancel", methods=["GET", "POST"])
@login_required
def cancel():
    if request.method == "POST":

        q = db.execute("SELECT * FROM invoice WHERE user_id = " + "\'" + str(session["user_id"]) + "\'")
        query = q.fetchall()
        for row in query:
            print(row)
            print(row[2])
            rr = json.dumps(row[2])
            qq = db.execute("SELECT quantity FROM inventory WHERE user_id = " + "\'" + str(session["user_id"]) + "\'" + " AND no_of_goods = " + str(row[11]) + " AND medicine = " + rr)
            amount = qq.fetchall()
            quantity = 0
            for t in amount:
                for y in t:
                    quantity = y

            db.execute("UPDATE inventory SET quantity = " + "\'" + str(row[3] + quantity) + "\' " + " WHERE medicine =  " + "\'" + str(row[2]) + "\'" + " AND user_id = " + str(session["user_id"]) + " AND no_of_goods = " + str(row[11]))
            db_all.commit()

            db.execute("DELETE FROM invoices WHERE user_id = " + "\'" + str(session["user_id"]) + "\'" + " AND medicine = " + rr + " AND invoice_no = " + str(row[12]))
            db_all.commit()
        db.execute("DELETE FROM invoice WHERE user_id = " + "\'" + str(session["user_id"]) + "\'")
        db_all.commit()

        return redirect(url_for("sales"))
    if request.method == "GET":
        return render_template("sales.html")


@app.route("/expire_date")
@login_required
def expire_date():
    result = db.execute("SELECT * FROM expire WHERE user_id = " + "\'" + str(session["user_id"]) + "\'" + " AND date(main.expire.expire_date) < date ('now');")
    query = result.fetchall()
    return render_template('expire_date.html', query=query)


@app.route("/activity")
@login_required
def activity():
    return render_template("activity.html")


@app.route("/inventory")
@login_required
def inventory():
    no = []
    result = db.execute("SELECT * FROM inventory WHERE user_id = " + str(session["user_id"]))
    query = result.fetchall()
    goods = db.execute("SELECT no_of_goods FROM inventory WHERE user_id = " + str(session["user_id"]))
    n = goods.fetchall()
    for i in n:
        for r in i:
            if r not in no:
                no.append(r)

    print(no)
    return render_template('inventory.html', query=query, no=no)


@app.route("/add_new_goods", methods=["GET", "POST"])
@login_required
def add_new_goods():
    if request.method == "POST":
        medicine = request.form.get("medicine")
        quantity = request.form.get("quantity")
        cost_price = request.form.get("cost_price")
        sell_price = request.form.get("sell_price")
        no_of_goods = request.form.get("no_of_goods")
        expire_request = request.form.get("expire_date")
        buy_date = request.form.get("buy_date")
        """
        exist = db.execute("SELECT medicine FROM inventory WHERE medicine = " + "\'" + medicine + "\'" + " AND user_id = " + str(session["user_id"]))
        m = ''
        for r in exist:
            for i in r:
                if i == medicine:
                    m = i
                    break
        print(m)
        drugstore_exist = db.execute("SELECT drugstore_name FROM inventory WHERE medicine = " + "\'" + medicine + "\'" + " AND user_id = " + str(session["user_id"]))
        drugstore = ''
        for row in drugstore_exist:
            for item in row:
                if item == request.form.get("drugstore_name"):
                    drugstore = item
                    break

        print(drugstore)
        if m == medicine and drugstore:
            db.execute("UPDATE inventory SET sell_price = " + "\'" + str(sell_price) + "\' " + " WHERE medicine =  " + "\'" + medicine + "\'" + " AND user_id = " + str(session["user_id"]))
            db.execute("INSERT INTO inventory(user_id,medicine,quantity,cost_price,sell_price,expire_date,buy_date,drugstore_name,no_of_goods) VALUES(" + "\'" + str(session["user_id"]) + "\'" + "," + "\'" + str(medicine) + "\'" + "," + "\'" + str(quantity) + "\'" + "," + "\'" + str(cost_price) + "\'" + "," + "\'" + str(sell_price) + "\'" + "," + "\'" + str(expire_request) + "\'" + "," + "\'" + str(buy_date) + "\'" + "," + "\'" + request.form.get("drugstore_name") + "\'" + "," + "\'" + str(no_of_goods) + "\')")
            db.execute("INSERT INTO expire(user_id,medicine,quantity,no_of_goods,expire_date,drugstore_name,buy_date)VALUES(" + "\'" + str(session["user_id"]) + "\'" + "," + "\'" + request.form.get("medicine") + "\'" + "," + "\'" + request.form.get("quantity") + "\'" + "," + "\'" + request.form.get("no_of_goods") + "\'" + "," + "\'" + request.form.get("expire_date") + "\'" + "," + "\'" + request.form.get("drugstore_name") + "\'" + "," + "\'" + str(buy_date) + "\')")
            db_all.commit()
            return redirect(url_for('inventory'))

        elif m == medicine and drugstore == '':
            cost_price_exist = db.execute("SELECT cost_price FROM inventory WHERE medicine = " + "\'" + medicine + "\'" + " AND user_id = " + str(session["user_id"]))
            sell_price_exist = db.execute("SELECT sell_price FROM inventory WHERE medicine = " + "\'" + medicine + "\'" + " AND user_id = " + str(session["user_id"]))
            print(cost_price_exist)
            print(sell_price_exist)
            for row in cost_price_exist:
                for item in row:
                    cost_price_exist = item
                    break
                break
            for r in sell_price_exist:
                for i in r:
                    sell_price_exist = i
                    break
                break
            if int(sell_price_exist) > int(sell_price):
                sell_price = sell_price_exist
            else:
                db.execute("UPDATE inventory SET sell_price = " + "\'" + str(sell_price) + "\' " + " WHERE medicine =  " + "\'" + medicine + "\'" + " AND user_id = " + str(session["user_id"]))
"""
        db.execute("INSERT INTO inventory(user_id,medicine,quantity,cost_price,sell_price,expire_date,buy_date,drugstore_name,no_of_goods) VALUES(" + "\'" + str(session["user_id"]) + "\'" + "," + "\'" + str(medicine) + "\'" + "," + "\'" + str(quantity) + "\'" + "," + "\'" + str(cost_price) + "\'" + "," + "\'" + str(sell_price) + "\'" + "," + "\'" + str(expire_request) + "\'" + "," + "\'" + str(buy_date) + "\'" + "," + "\'" + request.form.get("drugstore_name") + "\'" + "," + "\'" + str(no_of_goods) + "\')")
        db.execute("INSERT INTO expire(user_id,medicine,quantity,no_of_goods,expire_date,drugstore_name,buy_date)VALUES(" + "\'" + str(session["user_id"]) + "\'" + "," + "\'" + request.form.get("medicine") + "\'" + "," + "\'" + request.form.get("quantity") + "\'" + "," + "\'" + request.form.get("no_of_goods") + "\'" + "," + "\'" + request.form.get("expire_date") + "\'" + "," + "\'" + request.form.get("drugstore_name") + "\'" + "," + "\'" + str(buy_date) + "\')")
        db_all.commit()
        return redirect(url_for('inventory'))
    else:
        return render_template('add_new_goods.html')


@app.route("/logout", methods=["GET", "POST"])
@login_required
def logout():

    """Log user out"""
    if request.method == "POST":

        return redirect(url_for("out"))
    else:
        return render_template("logout.html")


@app.route("/ret", methods=["GET", "POST"])
@login_required
def ret():

    """Log user out"""
    if request.method == "POST":

        return redirect(url_for("sales"))
    else:
        return render_template("logout.html")


@app.route("/out")
def out():
    """Log user out"""
    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect(url_for("login"))


db_all.commit()

if __name__ == '__main__':
    app.run(debug=True)
