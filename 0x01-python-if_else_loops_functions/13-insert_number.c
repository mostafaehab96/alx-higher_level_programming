#include "lists.h"

/**
 * insert_node - inserts a node in a sorted list
 * @head: a pointer to the head of the list
 * @number: the number to be assigned to the new node
 * Return: the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *p = NULL;
	listint_t *c = *head;
	listint_t *new;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	while (c != NULL)
	{
		if (c->n > number)
			break;
		p = c;
		c = c->next;
	}
	new->n = number;
	if (p == NULL)
	{
		new->next = c;
		*head = new;
		return (new);
	}
	p->next = new;
	new->next = c;

	return (new);
}

