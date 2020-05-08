
/*
    平均計算時間：o(n^2)
    最悪計算時間: o(n^2)
*/

#include"stdio.h"

void selectionSort(int A[], int N){
    int min_j, tmp, i, j;
    for(i=0; i < N; ++i ){
        min_j = i;
        for(j = i+1; j < N; ++j){
            if(A[min_j] > A[j]){
                min_j = j;
         
            }
        }
        tmp = A[i];
        A[i] = A[min_j];
        A[min_j] = tmp;
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
    selectionSort(A, N);
    printf("After: "); trace(A, N);
}