
#include<iostream>
#include<cstring>

using namespace std;

template<typename Ty> class Stack{
private:
    int   end;
    Ty* data;
    int max_size;

public:
    Stack(int size){
        end = 0;
        max_size = size;
        data = (Ty*)malloc(sizeof(Ty) * max_size);
    }

    void push(Ty e){
        data[end] = e;
        end++;
    }

    Ty pop(){
        end--;
        return data[end];
    }
    
    bool isEnpty(){
        if(end == 0) return true;
        else return false;
    }

    bool isFull(){
        if(end == max_size) return true;
        else return false;
    }

    ~Stack(){
        free(data);
    }

};


int reversePolishNotation(Stack<int> *stack, string form){
    for(int i=0; form[i] != '\0'; i++){
        char c = form[i];
        switch (c){
            case '+':
                stack->push ( stack->pop() + stack->pop() );
                break;
            case '-':
                stack->push ( -(stack->pop() - stack->pop()) );
                break;
            case '/':
                stack->push ( int(1.0/ (double(stack->pop()) / double(stack->pop()))));
                break;
            case '*':
                stack->push ( stack->pop() * stack->pop() );
                break;
            default:
                stack->push(atoi(&c));
        }
    }
    cout << stack->pop() << endl;;
}

int main(){

    Stack<int> *stack = new Stack<int>(200);
    
    string  form;
    getline(cin,form); // 文字列中の空白スペースも読み込む
    reversePolishNotation(stack, form);

    //cout << "push: ";
    //for(int i=0; form[i] != '\0'; i++){
    //    stack->push(form[i]);
    //    cout << form[i] << " ";
    //}
    //cout << endl;

    //cout << "pop:  ";
    //for(int i=0; !stack->isEnpty(); i++){
    //    cout << stack->pop() << " ";
    //}
    //cout << endl;

    delete(stack);
}