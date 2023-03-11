#include "lists.h"


/**
 * add_nodeint - insert a new node at the begining of a list
 * @head: a pointer to the head of the list
 * @n: the integer to set for the new element
 * Return: a pointer to the new node
 */

listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *node = malloc(sizeof(listint_t));

	if (node == NULL)
		return (NULL);

	node->n = (int) n;
	node->next = *head;
	*head = node;

	return (node);
}

/**
 * is_palindrome - checks if the list is a palindrome
 * @head: a pointer to the head of the list
 * Return: 1 if is palindrome 0 if not
 */

int is_palindrome(listint_t **head)
{
	listint_t *p = *head;
	int i, j, count = 0;
	int arr[5000];

	if (*head == NULL)
		return (1);

	while (p)
	{
		arr[count] = p->n;
		p = p->next;
		count++;
	}
	j = count - 1;
	for (i = 0; i < count / 2; i++, j--)
	{
		if (arr[i] != arr[j])
			return (0);
	}
	
	return (1);
}
