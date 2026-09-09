import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

def run_notebook():
    base_dir = os.path.dirname(__file__)
    nb_path = os.path.join(base_dir, 'eda_retail_sales.ipynb')
    
    print(f"Reading notebook from {nb_path}...")
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
        
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    
    print("Executing notebook code cells (rendering charts and statistics)...")
    ep.preprocess(nb, {'metadata': {'path': base_dir}})
    
    output_nb_path = os.path.join(base_dir, 'eda_retail_sales.ipynb')
    with open(output_nb_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
        
    print(f"Notebook successfully executed and saved with all pre-rendered cell outputs at:\n{output_nb_path}")

if __name__ == '__main__':
    run_notebook()
