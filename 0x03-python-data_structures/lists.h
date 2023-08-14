#ifndef LISTS_H
#define LISTS_H

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for project
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

int is_palindrome(listint_t **head);

/* Function prototype */
void print_list_integer(int *my_list, size_t size);
int element_at(int *my_list, int idx);
int replace_in_list(int *my_list, int idx, int element);
void print_reversed_list_integer(int *my_list, size_t size);
int *new_in_list(int *my_list, int idx, int element);
char *no_c(char *my_string);
void print_matrix_integer(matrix=[[]]);

#endif /* LISTS_H */
