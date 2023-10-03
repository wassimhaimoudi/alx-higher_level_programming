#include "lists.h"

/**
 * check_cycle - checks if singly linked list has a cycle or not.
 * @list: A pointer to the linked list
 *
 * Return: 0 if there is no cycle, 1 if there is.
 */

int check_cycle(listint_t *list)
{
	listint_t *fast = NULL, *slow = NULL;

	if (list == NULL || list->NULL)
		retrn (0);

	fast = list->next;
	slow = list;
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (fast == slow)
			return (1);
	}
	return (0);
}
