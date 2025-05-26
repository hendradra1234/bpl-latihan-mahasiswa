
### Preparation
Here are the steps to prepare:

data source: https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance

Setup environment:
#### To Run the prediction via Python run this command:

1. Open a terminal or PowerShell.
2. Run the following command.
- Unix/MacOS
```
python3 -m venv .venv
```
- Windows
```
py -m venv .venv
```
3. Activate the virtual environment by running the following command.
- Unix/MacOS
```
.venv/bin/python
```
- Windows
```
.venv\Scripts\activate
```
4. To Confirm the virtual environment run this following command.
- Unix/MacOS and Windows
```
which python
```
5. Install all required libraries using the following command.
```
pip install -r requirements.txt
```
6. Open main.py then edit input on variable input_dataset.
7. Run prediction by running the following command.
- Unix/MacOS
```
python3 main.py
```
- Windows
```
py main.py
```
8. The prediction results will come out.
9. To Deactivate the Virtual environment use the following command.
```
deactivate
```
#### To Run the prediction via Run the Streamlit app using this command:

1. Open a terminal or PowerShell.
2. You already making venv .venv, so the next step Activate that venv.
3. Activate the virtual environment by running the following command.
- Unix/MacOS
```
.venv/bin/python
```
- Windows
```
.venv\Scripts\activate
```
4. To Confirm the virtual environment run this following command.
- Unix/MacOS and Windows
```
which python
```
5. All of required library already get installed so the next step  Run prediction dashboard by running the following command.
```
py main.py
```
6. The Dashboard will come out and result will be show on Web Browser.
7. To Deactivate the Virtual environment use the following command.
```
deactivate
```