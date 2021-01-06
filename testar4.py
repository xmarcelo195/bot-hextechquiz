def rodar(driver):
    from time import sleep
    question_ = ""
    try:
        start = driver.find_element_by_class_name('custom-button')
        start.click()
    except:
        print('não da pra clicar')
    else:
        i = []
        while len(i) < 5:
            try:
                question = driver.find_element_by_class_name('question-text').text
                if question != question_:
                    print(question)
                    driver.find_element_by_class_name('choice').click()
                    answers = []

                    answers_site = driver.find_elements_by_class_name('choice')

                    for answer in answers_site:
                        answers.append(answer.text)
                        print(answer.text)
                    with open('qa.txt', 'a+') as f:
                        f.write("{}; {}|{}|{} \n".format(question, answers[0], answers[1], answers[2]))
                    print('pegou')
                    question_ = question
                    i.append(question)
            except:
                sleep(0.5)
            finally:
                sleep(0.5)


    return

