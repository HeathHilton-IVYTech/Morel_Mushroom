from tkinter import*
import sys
sys.path.append(".")

root=Tk()
root.geometry('500x500')
root.title("Current Issues")

direction = ["North","South","East","West"]

#submitterName = [f.name() for  in range(100)]
#submitterEmail = [f.email() for  in range(100)]
#submitterAddress = [f.address() for _ in range(100)]
#directionchoices = [np.random.choice(direction,1)[0] for  in range(100)]

database = pd.DataFrame(dict(submitterName=submitterName, submitterEmail=submitterEmail, direction = direction_choices))
database.to_csv("submission_form_database.csv", index=False)
database.head()

direction_index_dict = {"North": 0, "South": 1, "East": 2, "West": 3}

def answerCheckBox(driver, df, element_class, user_id):
    direction_answer = df["direction"][user_id]
    direction_answer_index = direction_index_dict[direction_answer]
    driver.find_elements_by_class_name(element_class)[direction_answer_index].click()


    return driver

def submit(driver, element_class):
    driver.find_element_by_xpath(element_class).click()
    return driver