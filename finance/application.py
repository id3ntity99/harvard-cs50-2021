import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd
from datetime import datetime

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")

#Index
@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # Get user's current cash.
    result = db.execute("SELECT cash FROM users WHERE id=:id", id=session["user_id"])
    cash = result[0]['cash']

    # Get portfolio from DB.
    portfolio = db.execute("SELECT stock, quantity FROM portfolio WHERE user_id=:id", id=session['user_id'])

    # If there is no portfolio(If user doesn't buy any stocks)
    if not portfolio:
        return apology("sorry you have no holdings")

    grand_total = cash

    # Manipulate datas to display them.
    for stock in portfolio:
        price = lookup(stock['stock'])['price']
        total = stock['quantity'] * price
        stock.update({'price': price, 'total': total})
        grand_total += total

    return render_template("index.html", stocks=portfolio, cash=cash, total=grand_total, usd=usd)

#Buy
@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        quote = lookup(symbol)
        shares = request.form.get("shares")
        total_cost = int(shares) * quote['price']
        user_cash = db.execute("SELECT cash FROM users WHERE id=:id", id=session['user_id'])
        cash = user_cash[0]['cash']

        # If user doesn't type anythin on input.
        if not symbol:
            return apology("Plz give us a symbol.")

        # If user's input of symbol does not exist.
        if quote == None:
            return apology("there is no such a symbol.")

        # If user's input of symbol does exist.
        else:
            #If user doesn't have enough cash for purchase.
            if total_cost > cash:
                 apology("You don't have enough cash for buying that stock.")

            #If user has enough cash for purchase.
            else:
                 updated_cash = cash - total_cost
                 db.execute("UPDATE users SET cash=:cash WHERE id=:id", cash=updated_cash, id=session["user_id"])

            # Record history of transaction.
            db.execute(
                "INSERT INTO transactions (user_id, stock, quantity, price, date, state) VALUES (:user_id, :stock, :quantity, :price, :date, :state)",
                user_id=session["user_id"], stock=symbol, quantity=shares, price=quote['price'], date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), state="BUY")

            # Get portfolio
            portfolio = db.execute("SELECT quantity FROM portfolio WHERE stock=:stock AND user_id=:id", stock=quote["symbol"], id=session['user_id'])

            #If there is no portfolio, make one.
            if not portfolio:
                db.execute("INSERT INTO portfolio (user_id, stock, quantity) VALUES (:user_id, :stock, :quantity)",
                user_id=session['user_id'],stock=quote["symbol"], quantity=int(shares))

            # If the portfolio already exists.
            else:
                db.execute("UPDATE portfolio SET quantity=quantity+:quantity WHERE stock=:stock AND user_id=:id",
                    quantity=int(shares), stock=quote["symbol"], id=session['user_id']);

        return redirect("/")

    else:
        return render_template("buy.html")
    return apology("TODO")

#History
@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    transactions = db.execute("SELECT * FROM transactions WHERE user_id=:id", id=session['user_id'])
    return render_template("history.html", histories=transactions)

#Login
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    if request.method == "POST":

        if not request.form.get("symbol"):
            return apology("Please enter symbol")
        quote = lookup(request.form.get("symbol"))

        if quote == None:
            return apology("No such a symbol")

        else:
            return render_template("quoted.html", quote=quote, usd=usd)

    else:
        return render_template("quote.html")

#Register
@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":
        # If user doesn't provide username
        if not request.form.get("username"):
            return apology("must provide username", 403)
        # If user doesn't provide password
        elif not request.form.get("password"):
            return apology("must provide password", 403)

    # If request method is "GET"
    else:
        return render_template("register.html")

    # Username that user typed
    username = request.form.get("username")

    # User's password that user typed
    user_passwd = request.form.get("password")

    # Hash for user's password
    passwd_hash = generate_password_hash(user_passwd)


    # Error handling: If user name exists, make exception for ValueError.
    try:
        # Excute sqlite3 command that inserts values to the table.
        db.execute("INSERT INTO users (username, hash) VALUES(?, ?);", username, passwd_hash)
    except ValueError:
        return apology("username already exists.", 403)
    return redirect("/login")
    #return apology("TODO")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        quote = lookup(symbol)
        shares = request.form.get("shares")
        data = db.execute("SELECT * FROM portfolio WHERE stock=:stock AND user_id=:id", stock=symbol, id=session['user_id'])
        #If user doesn't have such a stock.
        if not data:
            return apology("You don't have such a stock.")
        #If user has such a stock.
        else:
            #If user doesn't have such amount of shares.
            if int(shares) > data[0]['quantity']:
                apology("You don't have that much stocks")
            else:
                #If user has such amount of shares.
                result_qty = data[0]['quantity'] - int(shares)
                #Update portfolio(Reduce shares of portfolio as user's input shares)
                db.execute("UPDATE portfolio SET quantity=:qty WHERE user_id=:id AND stock=:symbol", qty=result_qty, id=session['user_id'], symbol=symbol)

                 # Record history of transaction.
                db.execute(
                "INSERT INTO transactions (user_id, stock, quantity, price, date, state) VALUES (:user_id, :stock, :quantity, :price, :date, :state)",
                user_id=session["user_id"], stock=symbol, quantity=shares, price=quote['price'], date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"), state="SELL")


    else:
        return render_template("sell.html")
    return apology("TODO")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
