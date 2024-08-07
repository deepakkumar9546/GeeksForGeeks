//{ Driver Code Starts
#include <stdio.h>
#include <stdlib.h>

/* a Node of the doubly linked list */
struct Node {
    int data;
    struct Node *next;
    struct Node *prev;

    Node(int x) {
        data = x;
        next = NULL;
        prev = NULL;
    }
};


// } Driver Code Ends
/* Structure of Node
struct Node
{
  int data;
  struct Node *next;
  struct Node *prev;

  Node(int x){
      data = x;
      next = NULL;
      prev = NULL;
  }

};
*/

class Solution {
  public:
    Node* deleteNode(Node* head, int x) {
       Node* temp=head;
       int cnt=0;
       
       while(temp!=NULL){
           cnt++;
           if(cnt==x) break;
           temp=temp->next;
       }
       
       if(head==NULL){
           return NULL;
       }
       if(head->next==NULL){
           delete head;
           return NULL;
       }
      Node* back=temp->prev;
      Node* front=temp->next;
      
      if(front==NULL){
          back->next=NULL;
          temp->prev=NULL;
          delete temp;
          return head;
      }
      
      else if(back==NULL){
          head=head->next;
          front->prev==NULL;
          temp->next==NULL;
          delete temp;
          return head;
      }
      
      else{
          back->next=front;
          front->prev=back;
          temp->next=NULL;
          temp->prev=NULL;
          delete temp;
          return head;
      }
    }
};

//{ Driver Code Starts.

/* Function to print Nodes in a given doubly linked list
   This function is same as printList() of singly linked lsit */
void printList(struct Node *node) {
    while (node != NULL) {
        printf("%d ", node->data);
        node = node->next;
    }
    printf("\n");
}

/* Drier program to test above functions*/
int main() {
    int t, x, n, i;
    scanf("%d", &t);

    while (t--) {
        /* Start with the empty list */
        struct Node *temp, *head = NULL;
        scanf("%d", &n);

        temp = NULL;

        for (i = 0; i < n; i++) {
            scanf("%d", &x);

            if (head == NULL) {
                head = new Node(x);
                temp = head;
            } else {
                Node *temp1 = new Node(x);
                temp->next = temp1;
                temp1->prev = temp;
                temp = temp->next;
            }
        }

        scanf("%d", &x);

        Solution ob;
        head = ob.deleteNode(head, x);

        printList(head);
        while (head->next != NULL) {
            temp = head;
            head = head->next;
            free(temp);
        }

        free(head);
    }
    return 0;
}

// } Driver Code Ends