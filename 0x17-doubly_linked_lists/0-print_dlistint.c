#include "lists.h"

/**
 * print_dlistint - prints a doubly linked list
 * @h: the head of the list
 * Return: the size of the list
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t count;

	while (h)
	{
		printf("%i\n", h->n);
		h = h->next;
		count++;
	}

	return (count);
}


