def format_linter_error(error: dict) -> dict:
    error["line"] = error.pop["line_number"]
    error["column"] = error.pop["column_number"]
    error["message"] = error.pop["text"]
    error["name"] = error.pop["code"]
    del error["physical_line"]
    del error["store and decorate numbers: {', '.join(items)}!\""]
    error["source"] = "flake8"
    ###d[new_key] = d.pop(old_key)
    return


def format_single_linter_file(file_path: str, errors: list) -> dict:
    # write your code here
    pass


def format_linter_report(linter_report: dict) -> list:
    # write your code here
    pass



errors = [
    {"errors": [], "path": "./test_source_code_2.py", "status": "passed"},
    {
        "errors": [
            {
                "line": 18,
                "column": 80,
                "message": "line too long (99 > 79 characters)",
                "name": "E501",
                "source": "flake8",
            },
            {
                "line": 18,
                "column": 100,
                "message": "no newline at end of file",
                "name": "W292",
                "source": "flake8",
            },
        ],
        "path": "./source_code_2.py",
        "status": "failed",
    },
    {
        "errors": [
            {
                "line": 3,
                "column": 74,
                "message": "multiple statements on one line (semicolon)",
                "name": "E702",
                "source": "flake8",
            },
            {
                "line": 3,
                "column": 80,
                "message": "line too long (97 > 79 characters)",
                "name": "E501",
                "source": "flake8",
            },
            {
                "line": 15,
                "column": 1,
                "message": "expected 2 blank lines, found 1",
                "name": "E302",
                "source": "flake8",
            },
            {
                "line": 27,
                "column": 1,
                "message": "too many blank lines (6)",
                "name": "E303",
                "source": "flake8",
            },
            {
                "line": 31,
                "column": 80,
                "message": "line too long (99 > 79 characters)",
                "name": "E501",
                "source": "flake8",
            },
        ],
        "path": "./source_code_1.py",
        "status": "failed",
    },
    {
        "errors": [
            {
                "line": 4,
                "column": 1,
                "message": "expected 2 blank lines, found 1",
                "name": "E302",
                "source": "flake8",
            },
            {
                "line": 32,
                "column": 80,
                "message": "line too long (84 > 79 characters)",
                "name": "E501",
                "source": "flake8",
            },
            {
                "line": 112,
                "column": 6,
                "message": "no newline at end of file",
                "name": "W292",
                "source": "flake8",
            },
        ],
        "path": "./test_source_code_1.py",
        "status": "failed",
    },
]