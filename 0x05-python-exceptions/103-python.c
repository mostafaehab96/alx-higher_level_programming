#include <Python.h>

void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);


void print_python_list(PyObject *p)
{
	int size;
	int i;
	PyTypeObject *type;
	PyObject *item;
	int allocated;

	setbuf(stdout, NULL);

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	size = (int)PyList_GET_SIZE(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %i\n", (int) size);
	printf("[*] Allocated = %i\n", allocated);
	for (i = 0; i < size; i++)
	{
		item = PyList_GET_ITEM(p, i);
		type = (PyTypeObject *)PyObject_Type(item);
		printf("Element %i: %s\n", i, type->tp_name);
		if (strcmp(type->tp_name, "bytes") == 0)
			print_python_bytes(item);
		else if (strcmp(type->tp_name, "float") == 0)
			print_python_float(item);

	}
}

void print_python_bytes(PyObject *p)
{
	int size;
	char *string;
	int i;
	Py_buffer buffer;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyObject_GetBuffer(p, &buffer, PyBUF_SIMPLE);
	string = (char*) buffer.buf;
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

void print_python_float(PyObject *p)
{
	double value;
	char *string = NULL;

	printf("[.] float object info\n");

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
		
	value = PyFloat_AsDouble(p);
	string =  PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", string);
}

