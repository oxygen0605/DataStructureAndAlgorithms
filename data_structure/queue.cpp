
#include<iostream>

using namespace std;

template<typename Ty> class Queue{
private:
    int head;
    int tail;
    int max_size;
    Ty* data;
    
public:
    Queue(int size){
        head = 0;
        tail = 0;
        max_size = size+1; //最後の要素は使用しない。empty, fullを簡単に判定するために利用する
        data = (Ty*)malloc(sizeof(Ty) * (max_size)); 
    }
    ~Queue(){
        free(data);
    }

    void enqueue(Ty e){
        if(isFull()){
            cout << "This queue is full.\n";
            return ;
        }
        data[tail] = e;
        tail = (tail+1) % max_size; // if(tail >= max_size) tail = 0;
    }

    Ty dequeue(){
        if(isEmpty()){
            cout << "This queue is empty\n";
            exit(1);
        }
        Ty e = data[head];
        head = (head+1) % max_size; // if(head >= max_size) head = 0;
        return e;
    }

    bool isEmpty(){
        if(head==tail) return true;
        else return false;
    }

    bool isFull(){
        if( head == (tail+1)%max_size) return true;
        else return false;
    }
};

struct process{
    char name[5];
    int time;
};

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