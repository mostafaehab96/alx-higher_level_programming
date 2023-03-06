#include "lists.h"

/**
 * check_cycle - checks if there is a cycle in a linked list
 * @list: a pointer to the list
 * Return: 0 if there is no cycle, 1 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast, *head;

	head = list;
	slow = fast = head;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next;

		if (fast)
			fast = fast->next;
		else
			return (0);

		if (fast == slow)
			return (1);
	}

	return (0);
}
