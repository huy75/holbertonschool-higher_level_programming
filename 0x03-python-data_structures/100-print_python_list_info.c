#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Print list info about Python
 * @p: Pyobjext pointer
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	int idx;
	PyListObject *pObj = (PyListObject *)p;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", pObj->allocated);

	for (idx = 0; idx < Py_SIZE(p); idx++)
	{
		printf("Element %d: %s\n", idx, Py_TYPE(pObj->ob_item[idx])->tp_name);
	}
}
