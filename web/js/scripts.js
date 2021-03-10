/*
    TODO: Переименовать и оптимизировать функцию
*/

function godata() {
	var name = document.getElementById('name').value;
	var url = document.getElementById('url').value;
	var login = document.getElementById('login').value;
	var password = document.getElementById('password').value;
	var info = document.getElementById('info').value;

	if ((name && url && login && password) == "")
		document.getElementById('warning').style.display = 'block';
	else {
		document.getElementById('warning').style.display = 'none';
		eel.data(name, url, login, password, info);
	}
}