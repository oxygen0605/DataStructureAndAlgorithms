
// ref: http://www.cc.kyoto-su.ac.jp/~yamada/ap/queue.html#struct
// headとキューの要素数を考えるとisEmptyとisFullの判定が楽になる。

#include<iostream>

using namespace std;

template<typename Ty> class Queue{
private:
    int head;
    int num;
    int size;
    Ty* data;
    
public:
    Queue(int size){
        this->head = 0;
        this->num = 0;
        this->size = size;
        data = (Ty*)malloc(sizeof(Ty) * (size)); 
    }
    ~Queue(){
        free(data);
    }

    void enqueue(Ty e){
        if(isFull()){
            cout << "This queue is full.\n";
            return ;
        }
        int tail = ( head + num ) % size;
        data[tail] = e;
        num++;
    }

    Ty dequeue(){
        if(isEmpty()){
            cout << "This queue is empty\n";
            exit(1);
        }
        Ty e = data[head];
        head = (head+1) % size; // if(head >= size) head = 0;
        num--;
        return e;
    }

    bool isEmpty(){
        if(num <= 0) return true;
        else return false;
    }

    bool isFull(){
        if(num >= size) return true;
        else return false;
    }

    int getHead(){ return head;}
    int getNum(){ return num;}
    int getSize(){ return size;}
    Ty getData(int i){return data[i];}

};

struct process{
    char name[5];
    int time;
};

void queuePrint(Queue<process>* q){
    int head = q->getHead();
    int num  = q->getNum();
    int size = q->getSize();

    printf("queue [");
    for (int i = 0; i < size; i++) {
        if ((head + num <= size && head <= i && i < head + num) 
                ||(head + num > size && (head <= i || i < (head + num) % size))) {
            printf("%4d", q->getData(i).time);  
        } else {
            printf("%4c", '.');       /* queue に入っていないデータは表示しない */
        }
    }
    printf("]\n");
}

int main(){
    
    int n, q;
    cin >> n >> q;
    Queue<struct process>*  queue = new Queue<struct process>(n);

    for(int i=0; i<n; i++){
        struct process pp;
        cin >> pp.name >> pp.time;
        queue->enqueue(pp);
    }

    int elaps_time = 0;
    while(!queue->isEmpty()){
        queuePrint(queue);
        struct process pp = queue->dequeue();
        if(pp.time > q){
            pp.time -= q;
            queue->enqueue(pp);
            elaps_time += q;
        }else{
            elaps_time += pp.time;
            cout << pp.name << " " << elaps_time << endl;
        }
    }
    
    // 使いまわせているか確認用
    //for(int i=0; i<n; i++){
    //    struct process pp;
    //    cin >> pp.name >> pp.time;
    //    queue->enqueue(pp);
    //}

    //elaps_time = 0;
    //while(!queue->isEmpty()){
    //    struct process pp = queue->dequeue();
    //    if(pp.time > q){
    //        pp.time -= q;
    //        queue->enqueue(pp);
    //        elaps_time += q;
    //    }else{
    //        elaps_time += pp.time;
    //        cout << pp.name << " " << elaps_time << endl;
    //    }
    //}
}