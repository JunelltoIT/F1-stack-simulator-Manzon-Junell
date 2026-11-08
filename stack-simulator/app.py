"""Flask Stack Simulator."""

import os
import secrets

from flask import Flask, flash, redirect, render_template, request, session, url_for

from stack_model import Stack

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or secrets.token_hex(32)


@app.route('/')
def index():
    stack = Stack(session.get('stack', []))
    return render_template(
        'index.html',
        items=stack.items,
        size=stack.size(),
        popped=session.get('removed', []),
        highlight=request.args.get('peek') == '1',
    )


@app.route('/stack', methods=['POST'])
def operate():
    action = request.form.get('action', '')
    value = request.form.get('value', '').strip()
    stack = Stack(session.get('stack', []))
    removed = session.get('removed', [])
    peek = False

    if action == 'push':
        if not value or len(value) > 24:
            flash('Enter 1 to 24 characters.', 'warning')
        elif stack.size() >= 20:
            flash('The stack is full (20 items maximum).', 'warning')
        else:
            stack.push(value)
            flash(f'Pushed {value} onto the top.', 'success')
    elif action == 'pop':
        if stack.is_empty():
            flash('The stack is empty. Nothing to pop.', 'warning')
        else:
            top = stack.pop()
            removed.append(top)
            removed = removed[-20:]
            flash(f'Popped {top} from the top.', 'success')
    elif action == 'peek':
        if stack.is_empty():
            flash('The stack is empty. Nothing to peek.', 'warning')
        else:
            peek = True
            flash(f'Top value: {stack.peek()}.', 'info')
    elif action == 'clear':
        stack.clear()
        removed = []
        flash('Stack cleared.', 'info')
    else:
        flash('Unknown action.', 'warning')

    session['stack'] = stack.items
    session['removed'] = removed
    if peek:
        return redirect(url_for('index', peek=1))
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(port=int(os.environ.get('PORT', '5001')))
