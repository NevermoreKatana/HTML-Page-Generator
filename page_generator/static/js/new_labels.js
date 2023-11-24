function addNewField() {
    var form = document.getElementById('dynamic-form');

    var newFieldContainer = document.createElement('div');
    newFieldContainer.className = 'mb-4 created-field';

    var requestTypeSelect = document.getElementById('request-type');
    var selectedRequestType = requestTypeSelect.options[requestTypeSelect.selectedIndex].value;

    var newRequestInput = createNewInput('text', 'request', selectedRequestType);
    var newAnswerInput = createNewInput('text', 'answer', selectedRequestType);
    var newBodyInput = createNewInput('text', 'body', selectedRequestType);
    var newEPNameInput = createNewInput('text', 'endpoint', selectedRequestType);
    var newNameInput = createNewInput('text', 'name', selectedRequestType);

    newFieldContainer.appendChild(newNameInput);
    newFieldContainer.appendChild(newEPNameInput);
    newFieldContainer.appendChild(newRequestInput);
    newFieldContainer.appendChild(newBodyInput);
    newFieldContainer.appendChild(newAnswerInput);

    form.insertBefore(newFieldContainer, form.lastChild);
}

function createNewInput(type, namePrefix, requestType) {
    // Создаем новое поле ввода
    var newInput = document.createElement('input');
    newInput.type = type;
    newInput.name = getNewFieldName(namePrefix) + '-' + requestType; // Генерируем имя нового поля
    newInput.placeholder = namePrefix.charAt(0).toUpperCase() + namePrefix.slice(1) + ' (' + requestType + ')';
    newInput.required = true;
    newInput.className = 'w-full p-2 border border-gray-300 rounded-md';

    // Добавляем класс для отслеживания созданных полей
    newInput.classList.add('created-field');

    return newInput;
}

function getNewFieldName(namePrefix) {
    var form = document.getElementById('dynamic-form');
    var fieldContainers = form.getElementsByClassName('mb-4 created-field');
    var fieldCount = fieldContainers.length + 1;

    return namePrefix + fieldCount;
}

function removeLastField() {
    var form = document.getElementById('dynamic-form');
    var fieldContainers = form.getElementsByClassName('mb-4 created-field');

    if (fieldContainers.length >= 1) {
        var lastFieldContainer = fieldContainers[fieldContainers.length - 1];

        var createdFields = lastFieldContainer.getElementsByClassName('mb-4 created-field');
        for (var i = createdFields.length - 1; i >= 0; i--) {
            lastFieldContainer.removeChild(createdFields[i]);
        }

        form.removeChild(lastFieldContainer);
    }
}

