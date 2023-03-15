#include <Python.h>

void print_python_bytes(PyObject *p)
{
	int size;
	char *string;
	int i;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	string = PyBytes_AsString(p);
	size = (int) PyBytes_Size(p);
	printf("  size: %i\n", size);
	printf("  trying string: %s\n", string);
	if (size >= 10)
		size = 9;
	printf("  first %i bytes: ", size + 1);
	for (i = 0; i <= size; i++)
	{
		if (i < size)
			printf("%02x ", string[i]);
		else
			printf("%02x\n", string[i]);
	}

}
		
