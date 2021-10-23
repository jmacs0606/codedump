#include <stdio.h>
#include <stdlib.h>
int main(){
    struct node{
        int data;
        struct node *next;
    };
    struct node *head;
    printf("Enter length of linked list: ");
    int n;
    scanf("%d",&n);
    struct node *newNode,*temp;
    if(n>0){
        head = (struct node*)malloc(sizeof(struct node));
        if(head==NULL){
            printf("Memory Allocation Error");
            exit(1);
        }
        int data;
        printf("\nEnter data: ");
        int d; scanf("%d",&d);
        head->data = d;
        head->next = NULL;
        temp = head;
        newNode = (struct node*)malloc(sizeof(struct node));
        if(newNode == NULL){
            printf("Memory Allocation Error");
            exit(1);
        }
        printf("\nEnter data: ");
        scanf("%d",&d);
        newNode->data = d;
        newNode->next=NULL;
        temp->next = newNode;
        temp = temp->next;
        printf("Head: %d",head->data);
        printf("current: %d",temp->data);
    }
    
}
