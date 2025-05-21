#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_NAME_LEN 100
#define FILENAME "grades.txt"
#define THRESHOLD 60.0

typedef struct {
    char* name;
    float* grades;
    float average;
} Student;

void calculateAverage(Student* s, int subjectCount) {
    float sum = 0;
    for (int i = 0; i < subjectCount; i++) {
        sum += *(s->grades + i); // pointer arithmetic
    }
    s->average = sum / subjectCount;
}

void freeStudentData(Student* students, int count) {
    for (int i = 0; i < count; i++) {
        free(students[i].name);
        free(students[i].grades);
    }
    free(students);
}

int main() {
    FILE* file = fopen(FILENAME, "r");
    if (!file) {
        printf("Cannot open file '%s'\n", FILENAME);
        return 1;
    }

    int studentCount, subjectCount;
    fscanf(file, "%d %d", &studentCount, &subjectCount);

    Student* students = (Student*)malloc(studentCount * sizeof(Student));
    if (!students) {
        printf("Memory allocation failed.\n");
        fclose(file);
        return 1;
    }

    for (int i = 0; i < studentCount; i++) {
        students[i].name = (char*)malloc(MAX_NAME_LEN * sizeof(char));
        students[i].grades = (float*)malloc(subjectCount * sizeof(float));
        if (!students[i].name || !students[i].grades) {
            printf("Allocation failed.\n");
            fclose(file);
            return 1;
        }

        fscanf(file, "%s", students[i].name);
        for (int j = 0; j < subjectCount; j++) {
            fscanf(file, "%f", (students[i].grades + j)); // pointer to grades
        }
        calculateAverage(&students[i], subjectCount);
    }

    fclose(file);

    printf("\n--- Student Report ---\n");
    for (int i = 0; i < studentCount; i++) {
        Student* s = &students[i]; // pointer to struct
        printf("%s: Avg = %.2f - %s\n",
               s->name,
               s->average,
               s->average >= THRESHOLD ? "Above" : "Below");
    }

    freeStudentData(students, studentCount);
    return 0;
}
