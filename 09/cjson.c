#include <Python.h>

void process_json_load(PyObject *dict, char *json_string){
    char *json_copy = strdup(json_string);
    char * token = strtok(json_copy, ",");
    while (token != NULL){
        char * key;
        char * value;

        // Getting key
        char * delim_ptr = strchr(token, ':');
        key = malloc(sizeof(char) * (delim_ptr - token - 2));
        strncpy(key, token + 2, (delim_ptr - token - 3));
        key[(delim_ptr - token - 3)] = '\0';

        // Getting value
        char * delim_ptr2 = strrchr(token, ' ');
        value = malloc(sizeof(char) * (strlen((delim_ptr2 + 1)) + 1));
        strncpy(value, delim_ptr2 + 1, strlen(delim_ptr2));
        if (value[strlen(value) - 1] == '}'){
            value[strlen(value) - 1] = '\0';
        }
        else{
            value[strlen(value)] = '\0';
        }

        // Trying to make digit from string for value
        char * endPtr = NULL;
        int value_ = (int) strtod(value, &endPtr);

        // Making python objects
        PyObject * k;
        PyObject * val;

        if (!(k = PyUnicode_FromString(key))){
            printf("ERROR: Failed to build string value\n");
        }
        if (value_ == 0){
            value[strlen(value) - 1] = '\0';
            if (!(val = PyUnicode_FromString(value + 1))){
                printf("ERROR: Failed to build string value\n");
            }
        }
        else{
            if (!(val = Py_BuildValue("i", value_))){
                printf("ERROR: Failed to build int value\n");
            }
        }

        if (PyDict_SetItem(dict, k, val) < 0) {
            printf("ERROR: Failed to set item\n");
        }

        free(key);
        free(value);

        token = strtok(NULL, ",");
    }
    free(json_copy);
}

char * memcheck(char * iter, size_t neededSize, char * out) {
    size_t currentSize = strlen(iter);
    if (neededSize > currentSize) {
        char * tmp = malloc(sizeof(char) * (strlen(out) + neededSize));
        strcpy(tmp, out);
        if (tmp == NULL) {
            printf("Malloc Error\n");
            return NULL;
        }
        free(out);
        return tmp;
    }
    return out;
}

char * process_json_dumps(PyObject * dict_obj){
    // Pythonic key and value
    PyObject * key;
    PyObject * value;
    Py_ssize_t pos = 0;

    // Parse them to C style object and prepare JSON string
    char * out = malloc(sizeof(char) * 16);
    if (!out) return NULL;
    strcpy(out, "{");
    char * iter = out + 1;
    size_t outSize = 16;

    while (PyDict_Next(dict_obj, &pos, &key, &value)) {
        const char * c_key = NULL;
        const char * c_value = NULL;

        // Key parsing
        if (PyUnicode_Check(key)) {
            c_key = PyUnicode_AsUTF8(key);
        }
        else{
            printf("ERROR: Failed  to parse dict key to string\n");
            free(out);
            return NULL;
        }

        // Value parsing
        if (PyLong_Check(value)) {
            PyObject *str_obj = PyObject_Str(value);
            if (str_obj != NULL) {
                c_value = PyUnicode_AsUTF8(str_obj);
                Py_DECREF(str_obj);
            }
        }
        else if (PyUnicode_Check(value)){
            c_value = PyUnicode_AsUTF8(value);
        }
        else{
            printf("ERROR: Failed  to parse dict value to string\n");
            free(out);
            return NULL;
        }

        // Allocate additional memory
        size_t old_pos = iter - out;
        size_t neededSize = strlen(c_key) + strlen(c_value) + 6; // Extra space for quotes, colon, comma and possible null-terminator
        out = memcheck(iter, neededSize, out);
        if (!out) {
            return NULL;
        }
        iter = out + old_pos;

        // Adding key to the output string (Part 1)
        if (*(iter - 1) != '{'){
            *iter++ = ',';
            *iter++ = ' ';
        }

        // Adding key (Part 2)
        *iter++ = '"';
        strcpy(iter, c_key);
        iter += strlen(c_key);
        *iter++ = '"';
        *iter++ = ':';
        *iter++ = ' ';

        // Adding value to the output string
        char * endPtr;
        long val = strtol(c_value, &endPtr, 10); // Check if the value is a digit
        if (c_value == endPtr){
            *iter++ = '"';
            strcpy(iter, c_value);
            iter += strlen(c_value);
            *iter++ = '"';
            *iter = '}';
        }
        else{
            strcpy(iter, c_value);
            iter += strlen(c_value);
            *iter = '}';
        }

    }
    *(iter + 1) = '\0';
    return out;
}

static PyObject * loads(PyObject *self, PyObject *args){
    // Creating Python dict
    PyObject * dict;
    if (!(dict = PyDict_New())){
        printf("ERROR: Failed to create Dict Object\n");
        return NULL;
    }

    // Parsing json string
    char * json_string = NULL;
    if (!PyArg_ParseTuple(args, "s", &json_string)){
        printf("ERROR: Failed to parse arguments");
        return NULL;
    }

    process_json_load(dict, json_string);

    return dict;
}

static PyObject * dumps(PyObject *self, PyObject *args){
    // Creating Python string
    PyObject* dict_obj;

    // Is argument is dict
    if (!PyArg_ParseTuple(args, "O!", &PyDict_Type, &dict_obj)) {
        return NULL;
    }

    char * out = process_json_dumps(dict_obj);

    return Py_BuildValue("s", out);
}

// An array of structures of PyMethodDef type. Where we should provide a name of method, it's signature, flags and specification.
// It has NULL terminated element at the end
static PyMethodDef methods[] = {
        {"loads", loads, METH_VARARGS, "A function that loads json-string"},
        {"dumps", dumps, METH_VARARGS, "A function that dumps pythonic dict"},
        {NULL, NULL, 0, NULL}
};

// Module description (.m_name here is the name of the module that we tend to import in python script!)
static PyModuleDef module = {
        PyModuleDef_HEAD_INIT,
        "cjson",
        "Module which provides serialization and deserialization of JSON",
        -1,
        methods
};

// MODULE INITIALIZER
PyMODINIT_FUNC PyInit_cjson(void){
    return PyModule_Create(&module);
}