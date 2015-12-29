import os
from flask import *
from game.Game import Game
from game.Exceptions import BlackjackException


app = Flask(__name__)
app.secret_key = os.urandom(24)
PATH_DECK = "/static/deck/"
games = {}
keys = []


def cards_to_html(cards):
    images_row = ""
    text_row = ""
    for card in cards:
        images_row += "<td><center><img src=\"{0}\"/></center></td>".format(PATH_DECK + card.url)
        text_row += "<td><center><font color=\"{1}\">{0}</font></center></td>".format(card.text, card.color)
    table = "<center><table><tr>{0}</tr><tr>{1}</tr></table></center>".format(images_row, text_row)
    return Markup(table)


def get_feed():
    feed = ""
    flashed_messages = get_flashed_messages()
    flashed_messages.reverse()

    if len(flashed_messages) > 15:
        flashed_messages = flashed_messages[:15]
        flashed_messages.append(". . .")

    for message in flashed_messages:
        feed += message + Markup("<br/>")

    flashed_messages.reverse()
    for message in flashed_messages:
        flash(message)

    return feed


@app.route("/")
def homepage():
    try:
        key = session['key']
        G = games[key]
    except KeyError:
        return redirect(url_for("new_session"))

    feed = get_feed()
    score = "{0} - {1}".format(G.player_wins, G.dealer_wins)

    return render_template("index.html", feed=feed,
                                         score=score,
                                         player_hand=cards_to_html(G.player.hand),
                                         dealer_hand=cards_to_html(G.dealer.hand))


@app.route("/__new_session")
def new_session():
    key = os.urandom(12)
    session['key'] = key
    games[key] = Game()
    keys.append(key)

    if len(keys) >= 100:
        key = keys.pop(0)
        games.pop(key)

    flash(Markup("New session."))

    return redirect(url_for("homepage"))


@app.route("/__check")
def check():
    try:
        key = session['key']
        G = games[key]
    except KeyError:
        return redirect(url_for("new_session"))

    if not G.added_to_scoreboard and G.is_end():
        if G.player.is_loser(): message = "<font color=\"red\">{0} lost!</font>".format(G.player.name)
        elif G.dealer.is_loser(): message = "<font color=\"green\">{0} won!</font>".format(G.player.name)
        elif G.player.hand.sum() > G.dealer.hand.sum(): message = "<font color=\"green\">{0} won!</font>".format(G.player.name)
        else: message = "<font color=\"red\">{0} lost!</font>".format(G.player.name)

        flash(Markup(message))

    return redirect(url_for("homepage"))


@app.route("/__hit")
def hit():
    try:
        key = session['key']
        G = games[key]
    except KeyError:
        return redirect(url_for("new_session"))

    try:
        G.hit()
        flash(Markup("You drew a card."))
    except BlackjackException as err:
        flash(Markup(err))

    return redirect(url_for("check"))


@app.route("/__stand")
def stand():
    try:
        key = session['key']
        G = games[key]
    except KeyError:
        return redirect(url_for("new_session"))

    try:
        G.stand()
        flash(Markup("You're standing."))
    except BlackjackException as err:
        flash(Markup(err))

    return redirect(url_for("check"))


@app.route("/__reveal")
def reveal():
    try:
        key = session['key']
        G = games[key]
    except KeyError:
        return redirect(url_for("new_session"))

    try:
        move = G.deal()
        message = ""
        if move == "hit": message = "Dealer drew a card."
        if move == "stand": message = "Dealer is standing."
        flash(Markup(message))
        print(move)
    except BlackjackException as err:
        flash(Markup(err))

    return redirect(url_for("check"))


@app.route("/__reset")
def reset():
    try:
        key = session['key']
        G = games[key]
    except KeyError:
        return redirect(url_for("new_session"))

    G.reset()
    flash(Markup("New game."))

    return redirect(url_for("homepage"))


if __name__ == "__main__":
    app.run(debug=True)
