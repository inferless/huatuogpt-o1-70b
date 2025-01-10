INPUT_SCHEMA = {
    "prompt": {
        'datatype': 'STRING',
        'required': True,
        'shape': [1],
        'example': ["How to stop a cough?"]
    },
    "min_length": {
        'datatype': 'INT64',
        'required': False,
        'shape': [1],
        'example': [0]
    },
    "max_length": {
        'datatype': 'INT64',
        'required': False,
        'shape': [1],
        'example': [128]
    },
    "temperature": {
        'datatype': 'FP64',
        'required': False,
        'shape': [1],
        'example': [0.7]
    },
    "top_p": {
        'datatype': 'FP64',
        'required': False,
        'shape': [1],
        'example': [1.0]
    },
    "top_k": {
        'datatype': 'INT64',
        'required': False,
        'shape': [1],
        'example': [50]
    },
    "length_penalty": {
        'datatype': 'FP64',
        'required': False,
        'shape': [1],
        'example': [1.0]
    },
    "repetition_penalty": {
        'datatype': 'FP64',
        'required': False,
        'shape': [1],
        'example': [1.0]
    },
    "early_stopping": {
        'datatype': 'BOOL',
        'required': False,
        'shape': [1],
        'example': [False]
    },
    "max_new_tokens": {
        'datatype': 'INT64',
        'required': False,
        'shape': [1],
        'example': [128]
    },
    "min_new_tokens": {
        'datatype': 'INT64',
        'required': False,
        'shape': [1],
        'example': [20]
    },
    "do_sample": {
        'datatype': 'BOOL',
        'required': False,
        'shape': [1],
        'example': [False]
    },
    "num_beams": {
        'datatype': 'INT64',
        'required': False,
        'shape': [1],
        'example': [1]
    },

}
