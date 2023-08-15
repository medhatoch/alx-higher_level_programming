#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 * An empty list is considered a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head;
    listint_t *prev = NULL, *temp, *mid = NULL;
    int res = 1; // Assume the list is a palindrome

    if (*head == NULL || (*head)->next == NULL)
        return (res);

    // Find the middle of the linked list
    while (fast != NULL && fast->next != NULL)
    {
        fast = fast->next->next;
        temp = slow;
        slow = slow->next;
        temp->next = prev;
        prev = temp;
    }

    // If the list is odd, move to the next node to exclude the middle element
    if (fast != NULL)
        slow = slow->next;

    mid = slow;
    while (mid != NULL && prev != NULL)
    {
        if (mid->n != prev->n)
        {
            res = 0; // Not a palindrome
            break;
        }
        mid = mid->next;
        prev = prev->next;
    }

    // Revert the changes made to the first half of the list
    temp = NULL;
    while (slow != NULL)
    {
        temp = slow->next;
        slow->next = prev;
        prev = slow;
        slow = temp;
    }
    *head = prev;

    return (res);
}
