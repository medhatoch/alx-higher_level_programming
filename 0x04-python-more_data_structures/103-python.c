#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Print basic info about a Python list
 * @p: PyObject pointer to the list
 */
void print_python_list(PyObject *p)
{
    PyListObject *list = (PyListObject *)p;
    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t allocated = list->allocated;
    Py_ssize_t i;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", allocated);

    for (i = 0; i < size; i++)
    {
        PyObject *item = PyList_GetItem(p, i);
        const char *type = Py_TYPE(item)->tp_name;

        printf("Element %ld: %s\n", i, type);
        if (strcmp(type, "bytes") == 0)
            print_python_bytes(item);
    }
}

/**
 * print_python_bytes - Print basic info about a Python bytes object
 * @p: PyObject pointer to the bytes object
 */
void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes = (PyBytesObject *)p;
    Py_ssize_t size = PyBytes_Size(p);
    const char *str = PyBytes_AsString(p);
    Py_ssize_t i;

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);

    printf("  first 10 bytes: ");
    for (i = 0; i < size && i < 10; i++)
        printf("%02x%c", (unsigned char)str[i], i < 9 ? ' ' : '\n');
}

