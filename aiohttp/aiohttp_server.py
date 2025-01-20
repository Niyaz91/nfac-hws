from aiohttp import web

from aiohttp.pagination import page_size

movies = [
    { 'id': '1', 'title': 'The Shawshank Redemption', 'year': 1994, 'genre': 'Drama', 'rating': '4.95', },
    { 'id': '2', 'title': 'The Godfather', 'year': 1972, 'genre': 'Crime, Drama', 'rating': '4.88', },
    { 'id': '3', 'title': 'Inception', 'year': 2010, 'genre': 'Sci-Fi, Action', 'rating': '4.79', },
    { 'id': '4', 'title': 'Interstellar', 'year': 2014, 'genre': 'Sci-Fi, Drama', 'rating': '4.84', },
    { 'id': '5', 'title': 'Parasite', 'year': 2019, 'genre': 'Thriller, Drama', 'rating': '4.91', },
    { 'id': '6', 'title': 'The Dark Knight', 'year': 2008, 'genre': 'Action, Crime, Drama', 'rating': '4.89', },
    { 'id': '7', 'title': 'Pulp Fiction', 'year': 1994, 'genre': 'Crime, Drama', 'rating': '4.86', },
    { 'id': '8', 'title': 'The Lord of the Rings: The Return of the King', 'year': 2003, 'genre': 'Fantasy, Adventure', 'rating': '4.93', },
    { 'id': '9', 'title': 'Forrest Gump', 'year': 1994, 'genre': 'Drama, Romance', 'rating': '4.80', },
    { 'id': '10', 'title': 'Fight Club', 'year': 1999, 'genre': 'Drama, Thriller', 'rating': '4.78', },
]


async def handle(request):
    return web.json_response({'movies': movies})

async def popular(request):
    sorted_movies = sorted(movies, key=lambda x: x['rating'], reverse=True)
    return web.json_response(paginate(movies, page_size, page_number))

def paginate(items, page_size, page_number):
    start_index = (page_number - 1) * page_size
    end_index = start_index + page_size
    return items[start_index:end_index]


app = web.Application()
app.add_routes([web.get('/', handle), web.get('/popular',popular)])


if __name__ == '__main__':
    web.run_app(app, port=8080)