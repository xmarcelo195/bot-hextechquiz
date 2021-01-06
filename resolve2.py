def resolver(driver, ans, quest):
    from time import sleep

    question_ = ""
    try:
        start = driver.find_element_by_class_name('custom-button')
        start.click()
    except:
        print('não da pra clicar')
    else:
        # i = []
        while True:
            try:
                question = driver.find_element_by_class_name('question-text').text

                try:
                    index = quest.index(question)
                except:
                    driver.find_element_by_class_name('choice').click()

                else:
                    q1 = driver.find_element_by_xpath("//div[@class='choices']/div[1]")
                    q2 = driver.find_element_by_xpath("//div[@class='choices']/div[2]")
                    q3 = driver.find_element_by_xpath("//div[@class='choices']/div[3]")

                    if question != question_:
                        sleep(1)
                        if ans[index] == q1.text:
                            q1.click()
                            i=i+1
                        elif ans[index] == q2.text:
                            q2.click()
                            i=i+1
                        elif ans[index] == q3.text:
                            q3.click()
                            i=i+1
                        else:
                            print('what?')
                            i=i+1
            except:
                sleep(0.1)
            finally:
                sleep(0.01)

    return

