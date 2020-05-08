/*
    平均計算時間：o(n+d)
    最悪計算時間: o(n^2)
*/

#include"stdio.h"

void insertionSort(int A[], int N){
    int i = 0;
    for(i=1; i<N; i++){
        int v = A[i];
        int j=i-1;
        while( j >= 0 && A[j] > v){
            A[j+1] = A[j];
            j--;
        }
        A[j+1] = v;
    }
}

/* output */
void trace(const int A[], const int N){
    int i;
    for (i = 0; i < N; i++) printf("%d ", A[i]);
    printf("\n");
}

int main(){
    int N, i, j;
    int A[100];

    scanf("%d", &N);
    for (i=0; i<N; i++) scanf("%d", &A[i]);
    printf("Before: "); trace(A, N);
    insertionSort(A, N);
    printf("After: "); trace(A, N);
}