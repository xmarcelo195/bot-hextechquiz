def resolver2(driver, ans):
    from time import sleep

    question_ = ""

    while True:
        try:
            question = driver.find_element_by_class_name('question-text').text
            q1 = driver.find_element_by_xpath("//div[@class='choices']/div[1]")
            q2 = driver.find_element_by_xpath("//div[@class='choices']/div[2]")
            q3 = driver.find_element_by_xpath("//div[@class='choices']/div[3]")

        except:
            sleep(0.01)

        else:
            if question != question_:
                if q1 in ans:
                    q1.click()

                elif q2 in ans:
                    q2.click()

                else:
                    q3.click()
                    
            question_ = question

        finally:
            sleep(0.01)

    return

