import os

from selene import browser, have


def test_complete_todo():

    browser.open('/automation-practice-form')

    browser.element('#firstName').type('Ekaterina')
    browser.element('#lastName').type('Volf')

    browser.element('#userEmail').type('volfe@gmail.com')

    browser.element('//label[@for="gender-radio-2"]').click()

    browser.element('#userNumber').type('150567834')

    browser.element('#dateOfBirthInput').click()
    browser.element('//*[@class="react-datepicker__year-select"]').click().element('[value = "1987"]').click()
    browser.all('.react-datepicker__month-select>option').element_by(have.exact_text("April")).click()
    #//*[@class='react-datepicker__month-select']/option не сработал, не понятно почему
    browser.element('.react-datepicker__day.react-datepicker__day--016').click()

    browser.element('#subjectsInput').type('Biology').press_tab()

    browser.element('[for="hobbies-checkbox-2"]').click()

    browser.element('#uploadPicture').send_keys(os.path.abspath('guru.png'))

    browser.element('#currentAddress').type('Ryabinovaya st. 13')
    browser.element("#react-select-3-input").type('Haryana').press_enter()
    browser.element('#react-select-4-input').type('Karnal').press_enter()
    browser.element('#submit').click()

    browser.element('.modal-content').element('table').all('tr').all('td').even.should(
        have.exact_texts(
            "Ekaterina Volf",
            "volfe@gmail.com",
            "Female",
            "150567834",
            "16 April,1987",
            "Biology",
            "Reading",
            "guru.png",
            "Ryabinovaya st. 13",
            "Haryana Karnal",
        )
    )