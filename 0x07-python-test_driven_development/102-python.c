#define PY_SSIZE_T_CLEAN
#include <Python.h>

void print_python_string(PyObject *p) {
    if (PyUnicode_Check(p)) {
        Py_ssize_t length = PyUnicode_GET_LENGTH(p);
        const char *type = PyUnicode_IS_COMPACT_ASCII(p) ? "compact ascii" : "compact unicode";
        const char *value = PyUnicode_AsUTF8(p);

        printf("[.] string object info\n");
        printf("  type: %s\n", type);
        printf("  length: %zd\n", length);
        printf("  value: %s\n", value);
    } else {
        printf("[.] string object info\n");
        printf("  [ERROR] Invalid String Object\n");
    }
}

int main(void) {
    PyObject *s1 = PyUnicode_DecodeUTF8("The spoon does not exist", 24, NULL);
    PyObject *s2 = PyUnicode_DecodeUTF8("ложка не существует", 19, NULL);
    PyObject *s3 = PyUnicode_DecodeUTF8("La cuillère n'existe pas", 24, NULL);
    PyObject *s4 = PyUnicode_DecodeUTF8("勺子不存在", 5, NULL);
    PyObject *s5 = PyUnicode_DecodeUTF8("숟가락은 존재하지 않는다.", 14, NULL);
    PyObject *s6 = PyUnicode_DecodeUTF8("スプーンは存在しない", 10, NULL);
    PyObject *s7 = PyBytes_FromString("The spoon does not exist");

    print_python_string(s1);
    print_python_string(s2);
    print_python_string(s3);
    print_python_string(s4);
    print_python_string(s5);
    print_python_string(s6);
    print_python_string(s7);

    Py_DECREF(s1);
    Py_DECREF(s2);
    Py_DECREF(s3);
    Py_DECREF(s4);
    Py_DECREF(s5);
    Py_DECREF(s6);
    Py_DECREF(s7);

    return (0);
}
