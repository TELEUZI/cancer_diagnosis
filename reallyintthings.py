def make_training_set(training_file_name): #из файла с пациентами разделяем каждого пациента и их характеристики и собираем в список d (там 599 пациентов)
    f=open(training_file_name)
    k=f.read().split("\n")
    i=0
    d=[]
    while i<=598:
        m=k[i].split(",")
        d.append(m)
        i+=1      
    return d
def train_classifier(training_set_list): #считаем средние значения каждого параметра для больных и для здоровых, а после их среднее арифметическое
    a=[]
    k=0
    while k<=9:
        s=0
        s1=0
        n=0
        n1=0
        f=0
        f1=0
        for i in range (0,599):
            if training_set_list[i][10]=="2":
                if training_set_list[i][k]!='?':
                    s+=int(training_set_list[i][k])
                    n+=1
                    f=s/n
            elif training_set_list[i][10]=="4":
                if training_set_list[i][k]!='?':
                    s1+=int(training_set_list[i][k])
                    n1+=1
                    f1=s1/n1
        z=(f+f1)/2
        a.append(z)
        k+=1
    return a
def make_test_set(test_file_name): #делаем список тестируемых поцынтов (их 100)
    f=open(test_file_name)
    k=f.read().split("\n")
    i=0
    d=[]
    while i<=99:
        m=k[i].split(",")
        d.append(m)
        i+=1      
    return d
def classify_test_set_list(test_set_list, classifier_list): #собственно, сверяем значения каждого параметра с эталонными (совсем не очевидная часть, скорее всего)
    a=0
    for i in range (0,100):
        b=0
        k=1
        test_set_list[i].append('0')
        while k<=9:
            if (int(test_set_list[i][k])<classifier_list[k]):
                b+=1
                if b==9:
                    test_set_list[i][11]='2'
            if test_set_list[i][11]!='2':
                test_set_list[i][11]='4'
            k+=1
    return test_set_list
def report_results(result_list): # выводим результаты
    a=0
    i=0
    for i in range (0,100):
        if (result_list[i][10]==result_list[i][11]=='2')|(result_list[i][10]==result_list[i][11]=='4'):           
            a+=1
            print("Patient number {}: predicted tumor type is {}, real tumor type is the same.".format(result_list[i][0], result_list[i][10] ))
        elif (result_list[i][10]!=result_list[i][11]): 
            print("Patient number {}: predicted tumor type is {}, real tumor type isn't the same.".format(result_list[i][0], result_list[i][10] ))
    print ("Accuracy equals to {}.".format(a))
    print ("Reported the results.")
def main(): #вызываем здесь функции
    print("Reading in training data...")
    training_file_name="1.txt"
    training_set_list=make_training_set(training_file_name)
    print("Done reading training data. \n")
    print ("Training classifier")
    classifier_list=train_classifier(training_set_list)
    print ("Done training classifier. \n")
    print ("Reading in test data...")
    test_file_name="2.txt"
    test_set_list=make_test_set(test_file_name)
    print("Done reading test data. \n")
    print("Classifying records...")
    result_list=classify_test_set_list(test_set_list, classifier_list)
    print("Done classying. \n")
    report_results(result_list)
    print("Program finished. \n")
main()
