# IFC2JSON_python

Python converter from IFC SPF to JSON

# Getting Started

## Requirements

- ifcopenshell (using conda or in folder ./ifcopenshell)

## Installation ifcopenshell using Conda

1. Download the Conda installer for your OS setup. <https://docs.conda.io/en/latest/miniconda.html>
2. After installing Conda, create an environment for IFC.JSON with:

    ```
    conda create --name ifcjson
    ```

3. Then activate the new environment:

    ```
    conda activate ifcjson
    ```

4. Install ifcopenshell from conda-forge:

    ```
    conda install -c conda-forge ifcopenshell
    ```

## Installation ifcopenshell from direct download

Download a recent copy of ifcopenshell from: <https://builds.ifcopenshell.org/>

## Usage

```
python ifc2json.py -i model.ifc -o model_-_ifcjson4.json -v 4
```

```
optional arguments:
  -h, --help  show this help message and exit
  -i I        input ifc file path
  -o O        output json file path
  -v V        IFC.JSON version, options: "4"(default), "5a"
```

## Importing as a Python package

```bash
pip install git+<https://github.com/IFCJSON-Team/IFC2JSON_python.git>
```

After installing with pip, you can import the package in your Python code:

```python
from ifcjson import ifc2json4, ifc2json5a, mesh, reader, to_ifcopenshell, common
# Example usage:
# from ifcjson.ifc2json4 import some_function
```

## Additional Requirements for Roundtrip and IFC.JSON → IFC SPF Conversion

- The roundtrip tests and the conversion from IFC.JSON to IFC SPF require the `pandas` library.
- By default, the import of `to_ifcopenshell` is commented out in `file_converters/ifcjson/__init__.py` to avoid making `pandas` a minimal dependency.
- If you need this functionality, install pandas and uncomment the relevant line in `__init__.py`:

    ```python
    # from .to_ifcopenshell import JSON2IFC
    ```

    Change to:

    ```python
    from .to_ifcopenshell import JSON2IFC
    ```

- Install pandas with:

    ```
    pip install pandas
    ```

This keeps the minimal install lightweight for users who only need IFC → JSON conversion.

# Running Tests

A test converting a set of sample files is provided to verify the roundtrip conversion from IFC to JSON and back.
This test will process all `.ifc` files in `samples/input/`, write results to `samples/output/`, and check the validity of the conversion.

To run the test, use the following command from your project root:

```
python -m unittest file_converters/tests/test_samples.py
```

- Output files will be written to `samples/output/` and can be committed to version control for reference.
- The test checks for required keys and schema version in the generated JSON files.
- Make sure your input files are placed in `samples/input/`.

---
