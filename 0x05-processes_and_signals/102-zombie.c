#include "stdio.h"
#include "stdlib.h"
#include "unistd.h"

/**
 * infinite_while - program to run infinitely.
 * Return: void in the end
*/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - 5 zombies babies created on entry
 * Return: 0 on success
*/
int main(void)
{
	int children_processes = 0;
	pid_t pid;

	while (children_processes < 5)
	{
		pid = fork();
		if (!pid)
			break;
		printf("Zombie process created, PID: %i\n", (int)pid);
		children_processes++;
	}
	if (pid != 0)
		infinite_while();
	return (0);
}
