#include <Python.h>

void print_python_list(PyObject *p) {
    PyListObject *list = (PyListObject *)p;
    Py_ssize_t size = PyList_Size(p);

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", list->allocated);

    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject *element = PyList_GetItem(p, i);
        printf("Element %zd: %s\n", i, Py_TYPE(element)->tp_name);
    }
}

void print_python_bytes(PyObject *p) {
    PyBytesObject *bytes = (PyBytesObject *)p;
    Py_ssize_t size = PyBytes_GET_SIZE(p);

    printf("[.] bytes object info\n");
    printf("  size: %zd\n", size);

    if (size > 10) {
        size = 10;
    }

    printf("  trying string: %s\n", PyBytes_AsString(p));
    printf("  first %zd bytes: ", size);
    for (Py_ssize_t i = 0; i < size; i++) {
        printf("%02x ", (unsigned char)PyBytes_AS_STRING(p)[i]);
    }
    printf("\n");
}

void print_python_float(PyObject *p) {
    PyFloatObject *flt = (PyFloatObject *)p;
    double value = PyFloat_AS_DOUBLE(p);

    printf("[.] float object info\n");
    printf("  value: %lf\n", value);
}
