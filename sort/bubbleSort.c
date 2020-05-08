
/*
    平均計算時間：o(n^2)
    最悪計算時間: o(n^2)
*/
#include"stdio.h"

void bubbleSort(int A[], int N){
    int i = 0, j= 0;
    for(i=0; i < N-1; ++i){
        for (j=N-1; j >= i+1; --j){
            if (A[j-1] > A[j]){
                int tmp = A[j];
                A[j] = A[j-1];
                A[j-1] = tmp;
            }
        }
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
    bubbleSort(A, N);
    printf("After: "); trace(A, N);
}