if __name__ == '__main__':
    n = int(input())  # number of students' records
    student_marks = {}

    
    for i in range(n):
        name, *scores = input().split()
        scores = list(map(float, scores))
        student_marks[name] = scores

  
    g = input()

    
    print(round((sum(student_marks[g]) / len(student_marks[g])),2))

    # we can use this :  print("{:.2f}".format(sum(student_marks[g]) ...  to display 2 decimal digit after " , "
