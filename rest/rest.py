import pdb

import requests, sys


def get_all_movies():
    r = requests.get('http://localhost:8000/api/movies/')
    print('########## Movies list ##########\n')
    print(f'Response code: {r.status_code}')
    for movie in r.json()['movies']:
        print(f'id: {movie["id"]}')
        print(f'Title:    {movie["movie_title"]}')
        print(f'Genre:    {movie["genre"]}')
        print(f'Director: {movie["director"]}')
        print(f'Released: {movie["released"]}')
        print(f'Cast:     {movie["cast"]}')
        print('\n')
    print('\n\n')


def get_movie(uid):
    r = requests.get(f'http://localhost:8000/api/movies/{uid}')
    print('########## Movie ##########\n')
    print(f'Response code: {r.status_code}')
    for movie in r.json()['movie']:
        print(f'id: {movie["id"]}')
        print(f'Title:    {movie["movie_title"]}')
        print(f'Genre:    {movie["genre"]}')
        print(f'Director: {movie["director"]}')
        print(f'Released: {movie["released"]}')
        print(f'Cast:     {movie["cast"]}')
        print('\n')
    print('\n\n')


def create_movie(data):
    r = requests.post('http://localhost:8000/api/movies/',
                      data={'movie_title': data['movie_title'], 'genre': data['genre'], 'director': data['director'],
                            'released': data['released'], 'cast': data['cast']})
    print(r.status_code)
    print(r.json())


def modify_movie(data, uid):
    r = requests.put('http://localhost:8000/api/movies/',
                     data={'id': uid, 'movie_title': data['movie_title'], 'genre': data['genre'],
                           'director': data['director'],
                           'released': data['released'],
                           'cast': data['cast']})
    print(r.status_code)
    print(r.json())


def delete_movie(uid):
    r = requests.delete('http://localhost:8000/api/movies/',
                        data={'id': uid})
    print(r.status_code)


def get_all_actors():
    r = requests.get('http://localhost:8000/api/actors/')
    print('########## Actors list ##########\n')
    print(f'Response code: {r.status_code}')
    for actor in r.json()['actors']:
        print(f'id: {actor["id"]}')
        print(f'Name:    {actor["name"]}')
        print(f'Surname: {actor["surname"]}')
        print('\n')
    print('\n\n')


def get_actor(uid):
    r = requests.get(f'http://localhost:8000/api/actors/{uid}/')
    print('########## Actor ##########\n')
    print(f'Response code: {r.status_code}')
    for actor in r.json()['actor']:
        print(f'id: {actor["id"]}')
        print(f'Name:    {actor["name"]}')
        print(f'Surname: {actor["surname"]}')
        print('\n')
    print('\n\n')


def create_actor(data):
    r = requests.post('http://localhost:8000/api/actors/',
                      data={'name': data['name'], 'surname': data['surname']})
    print(r.status_code)
    print(r.json())


def modify_actor(data, uid):
    r = requests.put('http://localhost:8000/api/actors/',
                     data={'id': uid, 'name': data['name'], 'surname': data['surname']})
    print(r.status_code)
    print(r.json())


def delete_actor(uid):
    r = requests.delete('http://localhost:8000/api/actors/',
                        data={'id': uid})
    print(r.status_code)


def get_all_directors():
    r = requests.get('http://localhost:8000/api/directors/')
    print('########## Directors list ##########\n')
    print(f'Response code: {r.status_code}')
    for director in r.json()['directors']:
        print(f'id: {director["id"]}')
        print(f'Name:    {director["name"]}')
        print(f'Surname: {director["surname"]}')
        print('\n')
    print('\n\n')


def get_director(uid):
    r = requests.get(f'http://localhost:8000/api/directors/{uid}/')
    print('########## Director ##########\n')
    print(f'Response code: {r.status_code}')
    for director in r.json()['director']:
        print(f'id: {director["id"]}')
        print(f'Name:    {director["name"]}')
        print(f'Surname: {director["surname"]}')
        print('\n')
    print('\n\n')


def create_director(data):
    r = requests.post('http://localhost:8000/api/directors/',
                      data={'name': data['name'], 'surname': data['surname']})
    print(r.status_code)
    print(r.json())


def modify_director(data, uid):
    r = requests.put('http://localhost:8000/api/directors/',
                     data={'id': uid, 'name': data['name'], 'surname': data['surname']})
    print(r.status_code)
    print(r.json())


def delete_director(uid):
    r = requests.delete('http://localhost:8000/api/directors/',
                        data={'id': uid})
    print(r.status_code)


def help():
    print('Usage: rest.py [-OPTION] [ARGUMENT] [DATA] [ID]\n')
    print('[-OPTION]:')
    print('--help : prints command"s help')
    print('-get : makes a GET call to endpoint specified with [ARGUMENT]')
    print('-create : makes a POST call to endpoint specified with [ARGUMENT] and with data specified with [DATA]')
    print('-modify : makes a PUT call to endpoint specified with [ARGUMENT] and with data specified with [DATA] for '
          'existing model specified with [ID].')
    print('-delete : makes a DELETE call to endpoint specified with [ARGUMENT] and with data specified with [DATA] for '
          'existing model specified with [ID]\n')
    print('[ARGUMENT]:')
    print('movies')
    print('actors')
    print('directors\n')
    print('[DATA]:')
    print('Put data in key:value manner separated by commas, e.g.:')
    print('python3 rest.py -create actor name:John,surname:Doe')
    print('Data required for creating movie resource:')
    print(
        'movie_title, genre, director (pass director id or list of ids), released, cast ( pass actor id or list of ids)')
    print('Data required for creating actor and director resource:')
    print('name, surname')
    print('To modify a resource you will need to pass [DATA] and an item id in [ID]')
    print('To delete a resource you will need to pass only id [ID}\n')
    print('To get data of one specified resource you would need to pass parameters:')
    print('rest.py -get [ARGUMENT] [ID]\n')
    print('Examples:')
    print('python3 rest.py -get actors 1')
    print('python3 rest.py -get actors')
    print('python3 rest.py -create actors name:John,surname:Doe')
    print('python3 rest.py -modify actors name:John,surname:Doe 1')
    print('python3 rest.py -delete actors 1')


def get_request_data():
    request_data = sys.argv[3]
    data = {}
    for d in request_data.split(','):
        element = d.split(':')
        data[element[0]] = element[1]
    return data


if sys.argv[1] == '--help':
    help()

elif sys.argv[1] == '-get':
    if len(sys.argv) == 4:
        if sys.argv[2] == 'movies':
            get_movie(sys.argv[3])
        if sys.argv[2] == 'actors':
            get_actor(sys.argv[3])
        if sys.argv[2] == 'directors':
            get_director(sys.argv[3])
    else:
        if sys.argv[2] == 'movies':
            get_all_movies()
        if sys.argv[2] == 'actors':
            get_all_actors()
        if sys.argv[2] == 'directors':
            get_all_directors()

elif sys.argv[1] == '-create':
    if sys.argv[2] == 'movies':
        create_movie(get_request_data())
        get_all_movies()
    if sys.argv[2] == 'actors':
        create_actor(get_request_data())
        get_all_actors()
    if sys.argv[2] == 'directors':
        create_director(get_request_data())
        get_all_directors()

elif sys.argv[1] == '-modify':
    if sys.argv[2] == 'movies':
        modify_movie(get_request_data(), sys.argv[4])
        get_all_movies()
    if sys.argv[2] == 'actors':
        modify_actor(get_request_data(), sys.argv[4])
        get_all_actors()
    if sys.argv[2] == 'directors':
        modify_director(get_request_data(), sys.argv[4])
        get_all_directors()

elif sys.argv[1] == '-delete':
    if sys.argv[2] == 'movies':
        delete_movie(sys.argv[3])
        get_all_movies()
    if sys.argv[2] == 'actors':
        delete_actor(sys.argv[3])
        get_all_actors()
    if sys.argv[2] == 'directors':
        delete_director(sys.argv[3])
        get_all_directors()
