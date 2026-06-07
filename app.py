import stripe
import os

from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
# Don't put any keys in code. Use an environment variable (as shown
# here) or secrets vault to supply keys to your integration.
# See https://docs.stripe.com/keys-best-practices
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

app = Flask(
    __name__,
    static_url_path="",
    template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), "views"),
    static_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), "public"),
)


# Home route
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


# Checkout route
@app.route("/checkout", methods=["GET"])
def checkout():
    # Just hardcoding amounts here to avoid using a database
    item = request.args.get("item")
    title = None
    amount = None
    error = None
    email = request.values.get("email")
    client_secret = None

    if item == "1":
        title = "The Art of Doing Science and Engineering"
        amount = 2300
    elif item == "2":
        title = "The Making of Prince of Persia: Journals 1985-1993"
        amount = 2500
    elif item == "3":
        title = "Working in Public: The Making and Maintenance of Open Source"
        amount = 2800
    else:
        # Included in layout view, feel free to assign error
        error = "No item selected"

    # Create a PaymentIntent with the order amount and currency
    if item and amount:
        try:
            intent = stripe.PaymentIntent.create(amount=amount, currency="sgd")
            client_secret = intent.client_secret
        except stripe.error.StripeError as e:
            error = str(e.user_message)

    return render_template(
        "checkout.html",
        title=title,
        amount=amount,
        client_secret=client_secret,
        publishable_key=os.getenv("STRIPE_PUBLISHABLE_KEY"),
        error=error,
    )


# Success route
@app.route("/success", methods=["GET"])
def success():
    payment_intent_id = request.values.get("payment_intent")
    intent = stripe.PaymentIntent.retrieve(payment_intent_id)
    charge = stripe.Charge.retrieve(intent.latest_charge)
    if charge.description is None:
        description = ""
    else:
        description = charge.description
    return render_template(
        "success.html",
        currency=charge.currency,
        amount=intent.amount / 100,
        description=description,
        email=charge.receipt_email,
        chargeId=charge.id,
        payment_intent_id=payment_intent_id,
    )


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)
