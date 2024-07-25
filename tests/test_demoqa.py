import os

from selene import browser, have


def test_complete_todo():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Ekaterina')
    browser.element('#lastName').type('Volf')
    browser.element('#userEmail').type('volfe@gmail.com')
    browser.element('[for="gender-radio-2"]').click()
    browser.element('#userNumber').type('1505678349')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select option[value="3"]').click()
    browser.element('.react-datepicker__year-select option[value="1987"]').click()
    browser.element('.react-datepicker__day.react-datepicker__day--016').click()
    browser.element('#subjectsInput').type('Biology').press_tab()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('guru.png'))
    browser.element('#currentAddress').type('Ryabinovaya st. 13')
    browser.element("#react-select-3-input").type('Haryana').press_enter()
    browser.element('#react-select-4-input').type('Karnal').press_enter()
    browser.element('#submit').click()
    browser.element('.modal-content').element('table').all('tr').all('td').even.should(have.exact_texts(
            "Ekaterina Volf",
            "volfe@gmail.com",
            "Female",
            "1505678349",
            "16 April,1987",
            "Biology",
            "Reading",
            "guru.png",
            "Ryabinovaya st. 13",
            "Haryana Karnal",
        )
    )
