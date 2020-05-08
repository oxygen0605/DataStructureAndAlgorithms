#include<iostream>
#include<cstring>

using namespace std;

template<typename Ty> class List{
private:    

    Ty key;
    List<Ty>* prev;
    List<Ty>* next;

public:

    List(Ty k){
        key = k;
        prev = this;
        next = this;
    }

    List<Ty>* insertX(Ty x){ //今回は先頭にxを追加
        if(prev == this){
            List<Ty>* l = new List<Ty>(x);
            this->prev = l;
            l->next = this;
            return l;
        }
        else{
            this->prev->insertX(x);
        }
    }

    void deleteX(Ty x){ //今回は一番最初にヒットしたkeyをもつlistを削除する。
        if(this->key == x){
            this->prev->next = this->next;
            this->next->prev = this->prev;
            delete this; //自分自身を消す。
        }
        else{
            next->deleteX(x);
        }
    }

    void deleteFirst(){
        ;        
    }

    void deleteLast(){
        ;
    }

    Ty getKey(){
        return key;
    }

    List<Ty>* getNextList(){
        return next;
    }
};

int main(){
    int n, x;
    char command[100];
    cin >> n;
    
    cin >> command >> x;
    List<int>* l = new List<int>(x);
    List<int>* head = l;
    for(int i=1; i<n; i++){
        cin >> command >> x;
        if (strcmp(command,"insert") == 0){
            head = head->insertX(x);
        }else if(strcmp(command,"delete") == 0){
            head->deleteX(x);
        }
    }

    while(head != head->getNextList()){
        cout << head->getKey() << " ";
        head = head->getNextList();
    }
    cout << head->getKey() << " ";
    cout << endl;

    return 0;
}