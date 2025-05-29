import os
import json
import unittest

import ifcopenshell

from .. import ifcjson

class TestIFC2JSONSamples(unittest.TestCase):
    def setUp(self):
        # Resolve paths relative to the project root
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        self.input_dir = os.path.join(project_root, "samples", "input")
        self.output_dir = os.path.join(project_root, "samples", "output")

    def test_ifc_to_json_and_roundtrip(self):
        processed = 0
        for root, dirs, files in os.walk(self.input_dir):
            rel_path = os.path.relpath(root, self.input_dir)
            output_subdir = os.path.join(self.output_dir, rel_path)
            os.makedirs(output_subdir, exist_ok=True)

            for file in files:
                inFilePath = os.path.join(root, file)
                filename, file_extension = os.path.splitext(
                    os.path.basename(inFilePath))
                if file_extension.lower() == '.ifc':
                    processed += 1
                    normalized_ifc_path = os.path.join(
                        output_subdir, filename + '_ifcopenshell.ifc')
                    model = ifcopenshell.open(inFilePath)
                    model.write(normalized_ifc_path)

                    jsonFilePath = os.path.join(
                        output_subdir, filename + '.json')
                    with open(jsonFilePath, 'w') as outfile:
                        json.dump(ifcjson.IFC2JSON4(
                            normalized_ifc_path).spf2Json(), outfile, indent=2)

                    # Check JSON file for required keys and schema version
                    with open(jsonFilePath, 'r') as infile:
                        ifcJson = json.load(infile)
                        self.assertIn('version', ifcJson, "Missing 'version' key in JSON output")
                        self.assertIn('data', ifcJson, "Missing 'data' key in JSON output")
                        self.assertEqual(ifcJson['version'], '0.0.1', f"Unsupported version: {ifcJson['version']} (expected '0.0.1')")

                    # Convert back to SPF
                    ifc_json = ifcjson.JSON2IFC(jsonFilePath)
                    ifc_model = ifc_json.ifcModel()
                    roundtrip_path = os.path.join(
                        output_subdir, filename + '_roundtrip.ifc')
                    ifc_model.write(roundtrip_path)

                    # Basic check: output files exist
                    self.assertTrue(os.path.isfile(normalized_ifc_path))
                    self.assertTrue(os.path.isfile(jsonFilePath))
                    self.assertTrue(os.path.isfile(roundtrip_path))

        self.assertGreater(processed, 0, "No .ifc files found in input directory.")

if __name__ == "__main__":
    unittest.main()