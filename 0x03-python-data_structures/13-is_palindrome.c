#include "lists.h"

/**
 * reverse_listint - reverses a listint_t linked list.
 * @head: points to the head of the list.
 * Return: a pointer to the first node of the reversed list.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *next = NULL, *ptr = NULL;

	if (!head || !*head)
		return (NULL);

	ptr = *head;
	*head = NULL;

	while (ptr)
	{
		next = ptr->next;
		ptr->next = *head;
		*head = ptr;
		ptr = next;
	}
	return (*head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head
 * Return: 1 if success, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head, *half = *head;

	if (!*head || !(*head)->next)
		return (1);

	while (half && fast && fast->next)
	{
		half = half->next;
		fast = fast->next->next;
	}
	reverse_listint(&half);

	fast = *head;

	while (fast && half)
	{
		if (fast->n != half->n)
			return (0);
		fast = fast->next;
		half = half->next;
	}
	return (1);
}
