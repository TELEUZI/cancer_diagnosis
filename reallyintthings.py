import time
def make_training_set(training_file_name):
    f=open(training_file_name)
    patient_chars=f.read().split("\n")
    i=0
    training_set=[]
    while i<=len(patient_chars)-1:
        char=patient_chars[i].split(",")
        training_set.append(char)
        i+=1      
    return training_set
def train_classifier(training_set_list):
    clasifier_list=[]
    k=0
    while k<=9:
        sum_2, num_2, mean_2=0,0,0
        sum_4, num_4, mean_4=0,0,0
        for i in range (0,len(training_set_list)):
            if training_set_list[i][10]=="2":
                if training_set_list[i][k]!='?':
                    sum_2+=int(training_set_list[i][k])
                    num_2+=1
                    mean_2=sum_2/num_2
            elif training_set_list[i][10]=="4":
                if training_set_list[i][k]!='?':
                    sum_4+=int(training_set_list[i][k])
                    num_4+=1
                    mean_4=sum_4/num_4
        discr_value=(mean_2+mean_4)/2
        clasifier_list.append(discr_value)
        k+=1
    print(clasifier_list)
    return clasifier_list
def make_test_set(test_file_name):
    f=open(test_file_name)
    patient_chars=f.read().split("\n")
    i=0
    test_set=[]
    while i<=len(patient_chars)-1:
        char=patient_chars[i].split(",")
        test_set.append(char)
        i+=1      
    return test_set
def classify_test_set_list(test_set_list, classifier_list):
    for i in range (0,len(test_set_list)):
        b=0
        k=1
        chars=["id",
        "Clump Thickness",
        "Uniformity of Cell Size",
        "Uniformity of Cell Shape",
        "Marginal Adhesion",
        "Single Epithelial Cell Size",
        "Bare Nuclei",
        "Bland Chromatin",
        "Normal Nucleoli",
        "Mitoses"]
        test_set_list[i].append('0')
        while k<=9:
            if (int(test_set_list[i][k])<classifier_list[k]):
                b+=1
                if b==9:
                    test_set_list[i][11]='2'
            else: 
                test_set_list[i].append(chars[k])
            if test_set_list[i][11]!='2':
                test_set_list[i][11]='4'
            k+=1
    return test_set_list
def report_results(result_list):
    accuracy=0
    i=0
    for i in range (0,len(result_list)):
        if (result_list[i][10]==result_list[i][11]=='2')|(result_list[i][10]==result_list[i][11]=='4'):           
            accuracy+=1
            print("Patient number {}: predicted tumor type is {}, real tumor type is the same.".format(result_list[i][0], result_list[i][11] ))
        elif ((result_list[i][10]!=result_list[i][11])): 
            print("Patient number {}: predicted tumor type is {}, real tumor type isn't the same.".format(result_list[i][0], result_list[i][11]))
            print("In spite of high", end=" ")
            for k in range(12,len(result_list[i])):
                if k==len(result_list[i])-1:
                    print(result_list[i][k], end="\n")
                else:
                    print(result_list[i][k], end=", ")
    print ("Accuracy equals to {}%.".format(accuracy))
    print ("Reported the results.")
def submain():
    print("Reading in training data...")
    training_file_name="training_data.txt"
    training_set_list=make_training_set(training_file_name)
    print("Done reading training data. \n")
    print ("Training classifier")
    classifier_list=train_classifier(training_set_list)
    print ("Done training classifier. \n")
    print ("Reading in test data...")
    test_file_name="testing_data.txt"
    test_set_list=make_test_set(test_file_name)
    print("Done reading test data. \n")
    print("Classifying records...")
    result_list=classify_test_set_list(test_set_list, classifier_list)
    print("Done classying. \n")
    report_results(result_list)
    print("Program finished. \n")
def main():
    while True:
        ans=input('''Что вы хотите сделать?
        1)Провести диагностику уже имеющихся пациентов
        2)Проверить нового пациента онлайн
        3)Закрыть программу\n''')
        if ans=="3":
                print ("Спасибо за использование программы, сделанной Жевгением Чуранковым!")
                time.sleep(2) #После выведения надписи проходит 2 секунды перед закрытием программы.
                break #Выходит из главного цикла while
        elif ans=="1":
            submain()
        elif ans=="2":
            chars=["Clump Thickness",
            "Uniformity of Cell Size",
            "Uniformity of Cell Shape",
            "Marginal Adhesion",
            "Single Epithelial Cell Size",
            "Bare Nuclei",
            "Bland Chromatin",
            "Normal Nucleoli",
            "Mitoses"]
            training_file_name="all_data.txt"
            training_set_list=make_training_set(training_file_name)
            print("Done reading training data. \n")
            print ("Training classifier")
            classifier_list=train_classifier(training_set_list)
            k=[]
            ubnormals=[]
            b=0
            for i in range(0,9):
                k.append(input("Введите {} ".format(chars[i])))
                if int(k[i])<classifier_list[i+1]:
                    b+=1
                else:
                    ubnormals.append(chars[i])
            if b==9:
                print("This patient is fully charged!")
            else:
                print("Oh, here we go again.")
                print("Because of bad", end=" ")
                for k in range(0,len(ubnormals)):
                    if k==len(ubnormals)-1:
                        print(ubnormals[k]+" condition", end="\n")
                    else:
                        print(ubnormals[k], end=", ")
        else:
            print ("К сожалению, данный пункт меню не найден! Пожалуйста, введите цифры в промежутке от 1 до 4.")
            continue #Возвращаемся к началу цикла while
main()