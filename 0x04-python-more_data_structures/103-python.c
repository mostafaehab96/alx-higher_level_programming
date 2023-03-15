#include <Python.h>

void print_python_bytes(PyObject *p);

void print_python_list(PyObject *p)
{
	int size = (int)PyList_Size(p);
	int i;
	PyTypeObject *type;
	PyObject *item;
	int allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %i\n", (int) size);
	printf("[*] Allocated = %i\n", allocated);
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		type = Py_TYPE(item);
		printf("Element %i: %s\n", i, type->tp_name);
		if (strcmp(type->tp_name, "bytes") == 0)
			print_python_bytes(item);
	}
}

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
		
