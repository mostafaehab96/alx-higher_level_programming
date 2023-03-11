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
	listint_t *list = NULL;
	listint_t *p = *head;
	listint_t *t;

	while (p)
	{
		add_nodeint(&list, p->n);
		p = p->next;
	}
	p = *head;
	t = list;
	while (p)
	{
		if (p->n != t->n)
		{
			free_listint(list);
			return (0);
		}
		p = p->next;
		t = t->next;
	}
	free_listint(list);
	return (1);
}
