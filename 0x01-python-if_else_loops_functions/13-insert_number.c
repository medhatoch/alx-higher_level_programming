#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
* insert_node - inserts a number into a sorted singly linked list
* @head: pointer to the pointer of the first node of the list
* @number: the value to insert
* Return: the address of the new node, or NULL if it failed
*/
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new_node = malloc(sizeof(listint_t));
listint_t *current = *head;

if (!new_node)
return (NULL);

new_node->n = number;
new_node->next = NULL;

if (!current || current->n >= number)
{
new_node->next = current;
*head = new_node;
return (new_node);
}

while (current->next && current->next->n < number)
current = current->next;

new_node->next = current->next;
current->next = new_node;

return (new_node);
}

