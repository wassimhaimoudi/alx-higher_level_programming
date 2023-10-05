#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to the head of the list
 * @number: number to insert
 *
 * Return: address of the new node, or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *cur = NULL, *new_node = NULL;

	new_node = (listint_t *)malloc(sizeof(listint_t *));
	if (!new_node)
	{
		free(new_node);
		return (NULL);
	}
	new_node->n = number;
	new_node->next = NULL;

	if (!head)
	{
		return (NULL);
	}

	if (!(*head) || number <= (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	cur = *head;
	while (cur->next != NULL && cur->next->n < number && cur->next->n > cur->n)
	{
		cur = cur->next;
	}

	new_node->next = cur->next;
	cur->next = new_node;

	return (new_node);
}
