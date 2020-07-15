import time
 
 
def make_training_set(training_file_name):
    f = open(training_file_name)
    patient_chars = f.read().split("\n")
    training_set = []
    for i in range(len(patient_chars)):
        char = patient_chars[i].split(",")
        if "?" not in char:
            training_set.append(char)
    return training_set
 

def train_classifier(training_set_list):
    clasifier_list = []
    for l in range(1, 10):
        sum_2, num_2 = 0, 0
        sum_4, num_4 = 0, 0 
        for i in range(len(training_set_list)):
            if training_set_list[i][10] == "2":
                    sum_2 += int(training_set_list[i][l])
                    num_2 += 1
            elif training_set_list[i][10] == "4":
                    sum_4 += int(training_set_list[i][l])
                    num_4 += 1
        discr_value = (sum_2/num_2 + sum_4/num_4)/2
        clasifier_list.append(discr_value)
    return clasifier_list


def make_test_set(test_file_name):
    f = open(test_file_name)
    patient_chars = f.read().split("\n")
    test_set = []
    for i in range(len(patient_chars)):
        char = patient_chars[i].split(",")
        test_set.append(char)
    return test_set


def classify_test_set_list(test_set_list, classifier_list):
    for i in range(0, len(test_set_list)):
        b = 0
        chars = [
                "id",
                "Clump Thickness",
                "Uniformity of Cell Size",
                "Uniformity of Cell Shape",
                "Marginal Adhesion",
                "Single Epithelial Cell Size",
                "Bare Nuclei",
                "Bland Chromatin",
                "Normal Nucleoli",
                "Mitoses"
                ]
        test_set_list[i].append('0')
        for z in range (0, 9):
            if int(test_set_list[i][z+1]) < classifier_list[z]:
                b += 1
                if b == 9:
                    test_set_list[i][11] = '2'
            else:
                test_set_list[i].append(chars[z+1])
            if test_set_list[i][11] != '2':
                test_set_list[i][11] = '4'
    return test_set_list


def report_results(result_list):
    accuracy = 0
    i = 0
    for i in range(0, len(result_list)):
        if (result_list[i][10] == result_list[i][11] == '2') | \
                (result_list[i][10] == result_list[i][11] == '4'):
            accuracy += 1
            print("Patient number {}: predicted tumor type is {}, real tumor type is the same.\
                    ".format(result_list[i][0], result_list[i][11]))
        elif ((result_list[i][10] != result_list[i][11])):
            print("Patient number {}: predicted tumor type is {},real tumor type isn't the same.\
                    ".format(result_list[i][0], result_list[i][11]))
            print("In spite of high", end=" ")
            for k in range(12, len(result_list[i])):
                if k == len(result_list[i])-1:
                    print(result_list[i][k], end="\n")
                else:
                    print(result_list[i][k], end=", ")
    print ("Accuracy equals to {}%.".format(accuracy))
    print ("Reported the results.")


def submain():
    training_file_name = "training_data.txt"
    training_set_list = make_training_set(training_file_name)
    classifier_list = train_classifier(training_set_list)
    test_file_name = "testing_data.txt"
    test_set_list = make_test_set(test_file_name)
    result_list = classify_test_set_list(test_set_list, classifier_list)
    report_results(result_list)


def main():
    while True:
        ans = input('''Что вы хотите сделать?
        1)Провести диагностику уже имеющихся пациентов
        2)Проверить нового пациента онлайн
        3)Закрыть программу\n''')
        if ans == "3":
                print ("Спасибо за использование программы,\
                        сделанной Жевгением Чуранковым!")
                time.sleep(2)
                break
        elif ans == "1":
            submain()
        elif ans == "2":
            chars = [
                    "Clump Thickness",
                    "Uniformity of Cell Size",
                    "Uniformity of Cell Shape",
                    "Marginal Adhesion",
                    "Single Epithelial Cell Size",
                    "Bare Nuclei",
                    "Bland Chromatin",
                    "Normal Nucleoli",
                    "Mitoses"
                ]
            training_file_name = "all_data.txt"
            training_set_list = make_training_set(training_file_name)
            print("Training classifier")
            classifier_list = train_classifier(training_set_list)
            k = []
            ubnormals = []
            b = 0
            for i in range(0, 9):
                k.append(input("Введите {} ".format(chars[i])))
                if int(k[i]) < classifier_list[i+1]:
                    b += 1
                else:
                    ubnormals.append(chars[i])
            if b == 9:
                print("This patient is fully charged!")
            else:
                print("Oh, here we go again.")
                print("Because of bad", end=" ")
                for k in range(0, len(ubnormals)):
                    if k == len(ubnormals)-1:
                        print(ubnormals[k]+" condition", end="\n")
                    else:
                        print(ubnormals[k], end=", ")
        else:
            print ("К сожалению, данный пункт меню не найден!\
            Пожалуйста, введите цифры в промежутке от 1 до 4.")
            continue
main()
