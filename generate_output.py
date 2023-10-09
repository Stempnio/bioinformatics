import importlib
import os

lab_number = input("Enter lab number: ")
lab_name = f"lab{lab_number}"
file_name = input("Enter file name (without .py): ")
method_name = input("Enter method name: ")

input_file_path = os.path.join("inputs", lab_name, f"input_{file_name}.txt")
with open(input_file_path, "r") as file:
    arguments = file.read().strip().split()

module = importlib.import_module(f"{lab_name}.{file_name}")
function = getattr(module, method_name)

result = function(*arguments)

output_folder = f"outputs/{lab_name}"
os.makedirs(output_folder, exist_ok=True)
file_path = os.path.join(output_folder, f"output_{file_name}_{method_name}.txt")

with open(file_path, "w") as file:
    file.write(str(result))

print(f"Result saved in file {file_path}")
