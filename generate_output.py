import importlib
import os


def get_user_input():
    lab_number = input("Enter lab number: ")
    lab_name = f"lab{lab_number}"
    file_name = input("Enter file name (without .py): ")
    method_name = input("Enter method name: ")

    return lab_name, file_name, method_name


def read_arguments(lab_name, file_name):
    input_file_path = os.path.join("inputs", lab_name, f"input_{file_name}.txt")
    with open(input_file_path, "r") as file:
        arguments = file.read().strip().split()

    return arguments


def execute_function(module_path, method_name, arguments):
    module = importlib.import_module(module_path)
    function = getattr(module, method_name)
    result = function(*arguments)

    return result


def save_output(lab_name, file_name, method_name, result):
    output_folder = f"outputs/{lab_name}"
    os.makedirs(output_folder, exist_ok=True)
    file_path = os.path.join(output_folder, f"output_{file_name}_{method_name}.txt")

    with open(file_path, "w") as file:
        file.write(str(result))

    print(f"Result saved in file {file_path}")


def main():
    lab_name, file_name, method_name = get_user_input()
    arguments = read_arguments(lab_name, file_name)

    module_path = f"{lab_name}.{file_name}"
    result = execute_function(module_path, method_name, arguments)
    save_output(lab_name, file_name, method_name, result)


if __name__ == "__main__":
    main()
