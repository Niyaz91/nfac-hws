from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

comments = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        category = request.form['category']
        comments.insert(0, {
            'text': text,
            'category': category
        })
        return redirect(url_for('index'))

    # Пагинация
    page = int(request.args.get('page', 1))
    per_page = 5
    start = (page - 1) * per_page
    end = start + per_page
    total_pages = (len(comments) + per_page - 1) // per_page

    return render_template('index.html',
                           comments=comments[start:end],
                           current_page=page,
                           total_pages=total_pages)

if __name__ == '__main__':
    app.run(debug=True)
