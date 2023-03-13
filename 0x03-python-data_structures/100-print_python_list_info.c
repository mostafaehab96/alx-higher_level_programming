#include <Python.h>

void print_python_list_info(PyObject *p)
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
	}
	

}
