#include "lists.h"


/**
 * palindrome- checks if a linked list is a palindrome by recursion
 * the idea is to trace the list to it's end first by recursion while
 * maintaining the head and then compare the begining with the end
 * if one of the numbers didn't match then it's not a palindrome
 * @left: a pointer to the head (left side) of the list
 * @right: a pointer to the right side of the list
 * Return: 1 if it's a palindrome 0 if not
 */
int palindrome(listint_t **left, listint_t *right)
{
	int check;

	if (right == NULL)
		return (1);

	check = palindrome(left, right->next);

	if (check == 0)
		return (0);

	check = (*left)->n == right->n;
	*left = (*left)->next;

	return (check);
}

/**
 * is_palindrome - uses the function palindrome
 * @head: a pointer to a head of a linked list
 * Return: 1 if palindrome 0 if not
 */
int is_palindrome(listint_t **head)
{
	return (palindrome(head, *head));
}
