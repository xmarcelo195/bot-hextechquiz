from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get('https://join.stagecast.se/api/web/code/3563/04dO2ncpyaG9dJwGR7Ep16pxowAYPejZd0bE')
sleep(15)


print('iniciando')
frame = driver.find_element_by_id("frame")
driver.switch_to.frame(frame)
#             close = driver.find_elements_by_class_name('button-close')


question_ = ""
path_answer = "//div[@class='choice.selected.disabled.is-correct' or @class='choice.disabled.is-correct']"
while True:
    print('primeiro while')
    try:
        print('tryantesdobotao')
        start = driver.find_element_by_class_name('custom-button')
        print('try depois do botao')
        start.click()
        i=0

        while i<5:
            print('while i5')
            try:
                question = driver.find_element_by_class_name('question-text').text

                if question != question_:
                    print(question)
                    driver.find_element_by_class_name('choice').click()
                    answers = []

                    answers_site = driver.find_elements_by_class_name('choice')
                    sleep(0.5)
                    for answer in answers_site:
                        answers.append(answer.text)
                        print(answer.text)
                    with open('qa.txt', 'a+') as f:
                        f.write("{}, {}|{}|{} \n".format(question, answers[0], answers[1], answers[2]))
                    print('pegou')
                    question_ = question
                    i=i+1
            except:
                sleep(0.1)
    except:
        sleep(1)
