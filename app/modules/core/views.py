from flask import Blueprint, render_template, request, redirect, url_for
from .mail import send_email
import requests

core = Blueprint('core', __name__, template_folder='templates')


@core.route('/')
def index():
	return render_template('index.jinja2')


@core.route('/get-maket', methods=['POST'])
def get_maket():
	data = request.get_json()

	email = data['email']
	name = data['name']
	phone = data['phone']

	send_email(subject='Запрос на макет на сайте medalinazakaz.ru', email = email, name = name, phone = phone)
	r = requests.post('https://api.amocore.in/geraldzavod/integration/add/rmoqe6srbh9il3i0shusvrxxvssuywoa', data = {'type': 'get-maket', 'email': email, 'name': name, 'phone': phone})
	return 'OK'


@core.route('/callback', methods=['POST'])
def callback():
	data = request.get_json()

	phone = data['phone']

	r = requests.post('https://api.amocore.in/geraldzavod/integration/add/rmoqe6srbh9il3i0shusvrxxvssuywoa', data = {'type': 'callback', 'phone': phone})
	send_email(subject='Заказ обратного звонка на сайте medalinazakaz.ru', phone = phone)
	return 'OK'


@core.route('/get-art', methods=['POST'])
def get_art():
	data = request.get_json()

	email = data['email']

	send_email(subject='Запрос на эскизы художника на сайте medalinazakaz.ru', email = email)
	r = requests.post('https://api.amocore.in/geraldzavod/integration/add/rmoqe6srbh9il3i0shusvrxxvssuywoa', data = {'type': 'get-art', 'email': email})
	return 'OK'


@core.route('/get-commerce', methods=['POST'])
def get_commerce():
	data = request.get_json()

	email = data['email']
	phone = data['phone']

	send_email(subject='Запрос на коммерческое предложение на сайте medalinazakaz.ru', email = email, phone = phone)
	r = requests.post('https://api.amocore.in/geraldzavod/integration/add/rmoqe6srbh9il3i0shusvrxxvssuywoa', data = {'type': 'get-commerce', 'email': email, 'phone': phone})
	return 'OK'


@core.route('/get-contract', methods=['POST'])
def get_contract():
	data = request.get_json()

	email = data['email']

	send_email(subject='Запрос на шаблон договора на сайте medalinazakaz.ru', email = email)
	r = requests.post('https://api.amocore.in/geraldzavod/integration/add/rmoqe6srbh9il3i0shusvrxxvssuywoa', data = {'type': 'get-contract', 'email': email})
	return 'OK'


@core.route('/send-mail', methods=['POST'])
def send_mail():
	data = request.get_json()

	email = data['email']
	msg = data['msg']

	send_email(subject='Письмо с сайта medalinazakaz.ru', email = email, text = msg)
	r = requests.post('https://api.amocore.in/geraldzavod/integration/add/rmoqe6srbh9il3i0shusvrxxvssuywoa', data = {'type': 'send-mail', 'email': email, 'text': msg})
	return 'OK'


@core.route('/thankyou')
def thankyou():
	return render_template('thankyou.jinja2')
