$(document).on('click', '.edit', function(e){
    e.preventDefault();
    var id = $(this).data('id');
    $('#name-' + id + ' .text').hide();
    $('#surname-' + id + ' .text').hide();
    $('#age-' + id + ' .text').hide();
    $('#job-' + id + ' .text').hide();
    $('#edit-name-' + id).show();
    $('#edit-surname-' + id).show();
    $('#edit-age-' + id).show();
    // Замените поле ввода на выпадающий список
    $('#edit-job-' + id).replaceWith('<select id="edit-job-' + id + '" class="edit-field"><option value="Трудоустроенный">Трудоустроенный</option><option value="Безработный">Безработный</option></select>');
    $(this).hide();
    $(this).next('.save').show();
});

$(document).on('click', '.save', function(e){
    e.preventDefault();
    var id = $(this).data('id');
    var name = $('#edit-name-' + id).val();
    var surname = $('#edit-surname-' + id).val();
    var age = $('#edit-age-' + id).val();
    var job = $('#edit-job-' + id).val();

    // Здесь вы можете добавить код для сохранения новых данных на сервере
    $.ajax({
        url: '/update/' + id + '/',
        type: 'POST',
        data: {
            'name': name,
            'surname': surname,
            'age': age,
            'job': job,
            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(){
            $('#name-' + id + ' .text').text(name).show();
            $('#surname-' + id + ' .text').text(surname).show();
            $('#age-' + id + ' .text').text(age).show();
            $('#job-' + id + ' .text').text(job).show();
            $('#edit-name-' + id).hide();
            $('#edit-surname-' + id).hide();
            $('#edit-age-' + id).hide();
            // Верните поле ввода после сохранения
            $('#edit-job-' + id).replaceWith('<input type="text" id="edit-job-' + id + '" class="edit-field" value="' + job + '" style="display: none;">');
        }
    });

    $(this).prev('.edit').show();
    $(this).hide();
});

// Функция для подтверждения удаления
function confirmDeletion() {
    var password = prompt('Введите пароль для удаления:');
    if (password === '1234') { // Замените '1234' на ваш фактический пароль
        return confirm('Вы уверены, что хотите удалить этот элемент?');
    } else {
        alert('Неверный пароль!');
        return false;
    }
}

$(document).on('click', '.delete', function(e){
    e.preventDefault();
    if (confirmDeletion()) {
        // Если подтверждение прошло успешно, перенаправьте на URL удаления
        window.location.href = $(this).attr('href');
    }
});

// Получаем ссылку на чекбокс
const checkbox = document.querySelector('input[type="checkbox"]');
// Получаем ссылку на выпадающий список
const select = document.getElementById('job');

// Добавляем обработчик события для чекбокса
checkbox.addEventListener('change', function() {
    // Если чекбокс отмечен, устанавливаем значение "Безработный" в поле job
    if (this.checked) {
        select.value = 'Безработный';
    } else {
        // Если чекбокс не отмечен, возвращаем другое значение (например, "Трудоустроенный")
        select.value = 'Трудоустроенный';
    }
});

// Получаем ссылку на поле ввода возраста
document.querySelector('form').addEventListener('submit', function(event) {
    const ageInput = document.querySelector('input[name="age"]');
    const age = parseInt(ageInput.value);

    if (age < 18 || age > 65) {
        alert('Возраст должен быть от 18 до 65 лет.');
        event.preventDefault(); // Отменяем отправку формы
    }
});


$(document).ready(function() {
    $('#toggleUsersList').click(function() {
        // Переключение видимости только таблицы со списком пользователей
        // Мы предполагаем, что таблица со списком пользователей имеет класс 'users-list'
        $('.users-list').toggle();
        
        // Изменение текста кнопки в зависимости от состояния таблицы
        if ($('.users-list').is(':visible')) {
            $(this).text('Скрыть');
        } else {
            $(this).text('Добавить пользователей');
        }
    });
});


$(document).on('click', '#showLoginForm', function(e){
    e.preventDefault();
    $('#loginForm').show();
    $(this).hide();
});











