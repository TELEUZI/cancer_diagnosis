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
def report_results(result_list):
    accuracy=0
    i=0
    for i in range (0,len(result_list)):
        if (result_list[i][10]==result_list[i][11]=='2')|(result_list[i][10]==result_list[i][11]=='4'):           
            accuracy+=1
            print("Patient number {}: predicted tumor type is {}, real tumor type is the same.".format(result_list[i][0], result_list[i][10] ))
        elif (result_list[i][10]!=result_list[i][11]): 
            print("Patient number {}: predicted tumor type is {}, real tumor type isn't the same.".format(result_list[i][0], result_list[i][10] ))
    print ("Accuracy equals to {}%.".format(accuracy))
    print ("Reported the results.")
def main():
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
main()