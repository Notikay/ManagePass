/*
	TODO: Добавить функции проверки на корректность данных
*/

function sendData() {
	var data = {};
	var warning = document.getElementById('warning');
	var form_data = new FormData(document.getElementById("save-form"));

	for (let [key, value] of form_data.entries()) {
		if (value == "" && key != 'info') {
			warning.style.display = 'block';
			break;
		};
		data[key] = value;
	};
	
	if (Object.keys(data).length == 5) {
		warning.style.display = 'none';
		eel.getData(data);
	};
};