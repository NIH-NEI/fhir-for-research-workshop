# FHIR for Eye Health Research Workshop - May 2024

The files in this repository support the May 2024 NEI/ODSHI FHIR for Eye Health Research Workshop.

## Resources

- Slides:
    - [Linear version of slides](https://github.com/NIH-NEI/fhir-for-research-workshop/blob/main/slides/slides.md)
    - [Presentation version of slides](https://nih-nei.github.io/fhir-for-research-workshop/)
- Sample SMART on FHIR CDS architecture: <https://github.com/NIH-NEI/fhir-for-research-smart-example>
    - [Synthetic FHIR data](https://github.com/NIH-NEI/fhir-for-research-smart-example/tree/main/synthetic_data)
    - [Synthetic OCT and fundus images](https://github.com/NIH-NEI/fhir-for-research-smart-example/tree/main/example_pacs/images)

----

## Workshop Jupyter notebook

### Option 1: Running locally

You will need to have Python 3 and git installed on your system already.

1. Clone this repository (`git clone https://github.com/NIH-NEI/fhir-for-research-workshop.git`)
2. Open a Terminal window inside the `fhir-for-research-workshop/` on your system
3. Create a [virtual environment](https://quarto.org/docs/projects/virtual-environments.html): `python3 -m venv python_env`
4. Activate the virtual environment: `source python_env/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`
6. Run Jupyter: `jupyter notebook`
7. Your web browser should automatically open and display the jupyter environment. When it opens, double click on `workshop.ipynb`.

### Option 2: Running on mybinder.org

Click this button to launch the notebook contained in this GitHub project:

<a href="https://mybinder.org/v2/gh/nih-nei/fhir-for-research-workshop/HEAD?labpath=workshop.ipynb" target="_blank"><img src="https://mybinder.org/badge_logo.svg"></a>


----

## License

Copyright 2024 The MITRE Corporation

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

----

MITRE: Approved for Public Release / Case #24-0169