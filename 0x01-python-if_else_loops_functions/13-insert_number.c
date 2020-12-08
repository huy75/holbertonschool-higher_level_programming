#include "lists.h"

/**
 * insert_node - inserts a new node into a sorted singly list
 * @head: points to the head of the list
 * @number: the value of the new node
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode, *ptr;

	if (!head)
		return (NULL);

	ptr = *head;

	newNode = malloc(sizeof(listint_t));
	if (!newNode)
		return (NULL);

	newNode->n = number;
	newNode->next = NULL;

	while (ptr->next && ptr->next->n < newNode->n)
		ptr = ptr->next;

	if (ptr->next)
	{
		newNode->next = ptr->next;
		ptr->next = newNode;
	}
	else
	{
		ptr->next = newNode;
	}
	return (newNode);

}
